from typing import List
from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import FileTag
from app.repositories import FileTagRepository


class FileTagService:
    def __init__(self, file_tag: FileTagRepository):
        self.file_tag_repo = file_tag

    def get_file_tag(self, file_id: UUID, tag_id: UUID) -> FileTag:
        file_tag = self.file_tag_repo.get_by_ids(file_id, tag_id)
        if not file_tag:
            raise HTTPException(
                status_code=404, detail="File-tag association not found"
            )
        return FileTag.model_validate(file_tag)  # Convert ORM to DTO

    def get_tags_by_file(self, file_id: UUID) -> List[FileTag]:
        file_tags = self.file_tag_repo.get_tags_by_file(file_id)
        return [FileTag.model_validate(tag) for tag in file_tags]  # Convert ORM to DTO

    def get_files_by_tag(self, tag_id: UUID) -> List[FileTag]:
        files = self.file_tag_repo.get_files_by_tag(tag_id)
        return [FileTag.model_validate(file) for file in files]  # Convert ORM to DTO

    def create_file_tag(self, file_tag_data: FileTag) -> FileTag:
        # Create the association in the repository
        file_tag = self.file_tag_repo.create(
            file_tag_data.file_id, file_tag_data.tag_id
        )
        return FileTag.model_validate(file_tag)  # Convert ORM to DTO

    def delete_file_tag(self, file_tag_data: FileTag) -> dict:
        if not self.file_tag_repo.delete(file_tag_data.file_id, file_tag_data.tag_id):
            raise HTTPException(
                status_code=404, detail="File-tag association not found"
            )
        return {
            "message": f"File-tag association with file ID {file_tag_data.file_id} and tag ID {file_tag_data.tag_id} has been successfully deleted."
        }
