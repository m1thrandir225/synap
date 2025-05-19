import os
from typing import BinaryIO
from uuid import UUID

from fastapi import HTTPException, UploadFile
from openai import OpenAI

from app.config import settings
from app.models import CreateUploadedFile, PresignedUrlDTO, UploadedFileDTO
from app.repositories import UploadedFileRepository
from app.s3_storage_provider import S3StorageProvider
from app.services import UploadedFileService


class FileService:
    def __init__(self, repo:  UploadedFileRepository, uploaded_file_service: UploadedFileService ,s3_provider: S3StorageProvider):
        self.s3_provider = s3_provider
        self.repo = repo
        self.uploaded_files_service =  uploaded_file_service

    def _get_s3_filename_from_db_path(self, full_s3_path: str) -> str:
        if full_s3_path.startswith(self.s3_provider.user_prefix):
            return full_s3_path[len(self.s3_provider.user_prefix):]
        print(f"Warning s3 path: {full_s3_path} does not match user prefix {self.s3_provider.user_prefix}")

        return full_s3_path.split("/")[-1]
    
    async def upload_file_and_create_record(
            self,
            fast_api_upload_file: UploadFile,
            user_id: UUID,
            course_id: UUID,
            openai_id: str | None = None,
    ) -> UploadedFileDTO:
        if not fast_api_upload_file.filename:
            raise HTTPException(status_code=400, detail="File has no filename.")
        file_size = fast_api_upload_file.size
        if file_size is None:
            temp_content = await fast_api_upload_file.read()
            file_size = len(temp_content)
            await fast_api_upload_file.seek(0)
            if file_size == 0: print(f"Warning: File {fast_api_upload_file.filename} is empty.")
        try:
            s3_stored_filename_relative = await self.s3_provider.store_file(file=fast_api_upload_file)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to store file in S3: {str(e)}")
        
        full_s3_object_key = self.s3_provider.get_full_s3_key_for_file(s3_stored_filename_relative)

        original_filename = fast_api_upload_file.filename

        _root, file_ext = os.path.splitext(original_filename)

        try:
            openai_id = await self.upload_to_openai(original_filename, fast_api_upload_file.file)
        except Exception as e:
            raise Exception

        upload_file_dict = CreateUploadedFile(
            file_name=original_filename,
            file_path=full_s3_object_key,
            file_type=file_ext.lower(),
            file_size=file_size,
            mime_type=fast_api_upload_file.content_type or "application/octet-stream",
            user_id=user_id,
            openai_id=openai_id,
            course_id=course_id
        )

        try:
            db_file = self.uploaded_files_service.create_uploaded_file(upload_file_dict)
            return UploadedFileDTO.model_validate(db_file)
        except Exception as e:
            print(f"Error saving file to DB: {e}")
            try:
                await self.s3_provider.delete_file(s3_stored_filename_relative)
            except Exception as s3_del_e:
                print(f"Failed cleanup for S3 file {s3_stored_filename_relative} after DB error: {s3_del_e}")
            raise HTTPException(status_code=500, detail="Failed to save file metadata.")



    
    async def get_file_download_url(self, file_id: UUID, user_id: UUID) -> PresignedUrlDTO:
        db_file = self.repo.get_by_id(file_id)
        if not db_file:
            raise HTTPException(status_code=404, detail="File not found")
        s3_filename_relative = self._get_s3_filename_from_db_path(str(db_file.file_path))

        url = self.s3_provider.generate_presigned_url(s3_filename_relative)
        if not url:
            raise HTTPException(status_code=500, detail="Could not generate a presigned url")

        return PresignedUrlDTO(url=url, filename=str(db_file.file_name))

    async def delete_file_record_and_s3_object(self, file_id: UUID, user_id: UUID) -> dict[str, str] | None:
        db_file = self.repo.get_by_id(file_id)
        if not db_file:
            raise HTTPException(status_code=404, detail="File not found")
        s3_filename_relative = self._get_s3_filename_from_db_path(str(db_file.file_path))

        try:
            await self.s3_provider.delete_file(s3_filename_relative)
 
        except Exception as e:
            print(f"Error deleting file {s3_filename_relative} from S3, but will attempt to delete from db")
        
        if not self.repo.delete(db_file.id):
            raise HTTPException(status_code=500, detail="Error deleting file")
        
        return { "message": "Sucessfuly delete file!" }

    async def upload_to_openai(self, filename: str, filedata: BinaryIO) -> str | None:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        try:
            response = client.files.create(
                file=(filename, filedata),
                purpose="user_data"
            )

            return response.id
        except Exception as e:
            print(f"Failed to upload file to open_ai")
            raise HTTPException(status_code=500, detail="Failed file upload")