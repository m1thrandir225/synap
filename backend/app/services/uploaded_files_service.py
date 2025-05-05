from typing import List
from uuid import UUID
from fastapi import HTTPException
from app.models.uploaded_file import (
    UploadedFileDTO,
    UploadedFileBase,
    UpdateUploadedFileDTO,
)
from app.repositories import UploadedFileRepository


class UploadedFileService:
    def __init__(self, file_repo: UploadedFileRepository):
        self.file_repo = file_repo

    def get_uploaded_file(self, file_id: UUID) -> UploadedFileDTO:
        uploaded_file = self.file_repo.get_by_id(file_id)
        if not uploaded_file:
            raise HTTPException(status_code=404, detail="File not found")
        return UploadedFileDTO.model_validate(uploaded_file)  # Convert ORM to DTO

    def get_uploaded_files_by_user(self, user_id: UUID) -> List[UploadedFileDTO]:
        uploaded_files = self.file_repo.get_by_user_id(user_id)
        return [
            UploadedFileDTO.model_validate(file) for file in uploaded_files
        ]  # Convert ORM to DTO

    def get_uploaded_files_by_course(self, course_id: UUID) -> List[UploadedFileDTO]:
        uploaded_files = self.file_repo.get_by_course_id(course_id)
        return [
            UploadedFileDTO.model_validate(file) for file in uploaded_files
        ]  # Convert ORM to DTO

    def create_uploaded_file(self, file_data: UploadedFileBase) -> UploadedFileDTO:
        uploaded_file = self.file_repo.create(file_data.model_dump())
        return UploadedFileDTO.model_validate(uploaded_file)  # Convert ORM to DTO

    def update_uploaded_file(
        self, file_id: UUID, file_data: UpdateUploadedFileDTO
    ) -> UploadedFileDTO:
        updated_file = self.file_repo.update(
            file_id, file_data.model_dump(exclude_unset=True)
        )
        if not updated_file:
            raise HTTPException(status_code=404, detail="File not found")
        return UploadedFileDTO.model_validate(updated_file)  # Convert ORM to DTO

    def delete_uploaded_file(self, file_id: UUID) -> dict:
        if not self.file_repo.delete(file_id):
            raise HTTPException(status_code=404, detail="File not found")
        return {"message": f"File with ID {file_id} has been successfully deleted."}

    def get_files_by_tag(self, tag_name: str) -> List[UploadedFileDTO]:
        uploaded_files = self.file_repo.get_files_by_tag(tag_name)
        return [
            UploadedFileDTO.model_validate(file) for file in uploaded_files
        ]  # Convert ORM to DTO

    def get_files_by_recommendation(
        self, recommendation_id: UUID
    ) -> List[UploadedFileDTO]:
        uploaded_files = self.file_repo.get_files_by_recommendation(recommendation_id)
        return [
            UploadedFileDTO.model_validate(file) for file in uploaded_files
        ]  # Convert ORM to DTO

    def get_files_by_course_and_user(
        self, course_id: UUID, user_id: UUID
    ) -> List[UploadedFileDTO]:
        uploaded_files = self.file_repo.get_files_by_course_and_user(course_id, user_id)
        return [
            UploadedFileDTO.model_validate(file) for file in uploaded_files
        ]  # Convert ORM to DTO
