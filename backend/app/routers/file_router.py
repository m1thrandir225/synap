import os
import uuid
from fastapi import APIRouter, UploadFile, Depends, HTTPException, status
from fastapi.responses import FileResponse
from typing import Annotated, List
from pydantic import BaseModel
from app.dependencies import (
    get_current_token,
    get_current_user,
    get_uploaded_files_service,
)
from app.log import get_logger
from app.storage_provider import LocalStorageProvider, get_local_storage_provider
from app.services import UploadedFileService
from app.models import CreateUploadedFile, UploadedFileDTO
from app.database import User
from fastapi import Form


log = get_logger(__name__)


class FileInfo(BaseModel):
    filename: str


router = APIRouter(
    prefix="/files", tags=["Files"], dependencies=[Depends(get_current_token)]
)


@router.get("/", response_model=List[FileInfo])
async def list_user_files(
    storage_provider: LocalStorageProvider = Depends(get_local_storage_provider),
):
    """
    Lists all files stored for the current authenticated user.
    Requires authentication because LocalStorageProvider depends on the user.
    """
    filenames = storage_provider.list_files()
    return [{"filename": name} for name in filenames]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_file(
    # file: Annotated[UploadFile, Form()],
    file: UploadFile,
    course_id: Annotated[str, Form()],
    storage_provider: LocalStorageProvider = Depends(get_local_storage_provider),
    file_service: UploadedFileService = Depends(get_uploaded_files_service),
    user: User = Depends(get_current_user),
):
    """
    Uploads a new file for the current authenticated user.
    Requires authentication.
    """
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No filename provided"
        )

    try:
        contents = await file.read()
        file_size_bytes = len(contents)
        await file.seek(0)

        _filename, file_extension = os.path.splitext(file.filename)
        file_type = file_extension.lower() if file_extension else ""

        mime_type = (
            file.content_type if file.content_type else "application/octet-stream"
        )

        saved_filename = await storage_provider.store_file(file, filename=file.filename)

        file_path = f"{router.prefix}/{saved_filename}"

        uploaded_file_data = CreateUploadedFile(
            user_id=user.id,
            course_id=uuid.UUID(course_id),
            file_name=file.filename,
            file_path=file_path,
            file_type=file_type,
            file_size=str(file_size_bytes),
            mime_type=mime_type,
        )

        uploaded_file: UploadedFileDTO =  file_service.create_uploaded_file(file_data=uploaded_file_data)

        return uploaded_file
    
    except Exception as e:
        log.error("Failed to do something", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload file",
        )


@router.get("/{filename}")
async def get_file(
    filename: str,
    storage_provider: LocalStorageProvider = Depends(get_local_storage_provider),
):
    """
    Retrieves a specific file for the current authenticated user.
    Requires authentication.
    """
    file_path = storage_provider.get_file_path(filename)

    if not file_path.is_file():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )

    return FileResponse(file_path)


@router.delete("/{filename}")
async def delete_file(
    filename: str,
    storage_provider: LocalStorageProvider = Depends(get_local_storage_provider),
):
    """
    Deletes a specific file for the current authenticated user.
    Requires authentication.
    """
    file_path = storage_provider.get_file_path(filename)

    if not file_path.is_file():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )

    try:
        storage_provider.delete_file(filename)
        return {"message": f"File '{filename}' deleted successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete file",
        )
