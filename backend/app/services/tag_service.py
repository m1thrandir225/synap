from typing import List
from uuid import UUID
from fastapi import HTTPException
from app.models import TagDTO, CreateTagDTO, UpdateTagDTO
from app.repositories import TagRepository


class TagService:
    def __init__(self, tag_repo: TagRepository):
        self.tag_repo = tag_repo

    def get_tag(self, tag_id: UUID) -> TagDTO:
        tag = self.tag_repo.get_by_id(tag_id)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return TagDTO.model_validate(tag)  # Convert ORM to DTO

    def get_tag_by_name(self, name: str) -> TagDTO:
        tag = self.tag_repo.get_by_name(name)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return TagDTO.model_validate(tag)  # Convert ORM to DTO

    def get_all_tags(self) -> List[TagDTO]:
        tags = self.tag_repo.get_all()
        return [TagDTO.model_validate(tag) for tag in tags]  # Convert ORM to DTO

    def create_tag(self, tag_data: CreateTagDTO) -> TagDTO:
        # Convert the DTO data to dict and pass it to the repository
        tag = self.tag_repo.create(tag_data.dict())
        return TagDTO.model_validate(tag)  # Convert ORM to DTO

    def update_tag(self, tag_id: UUID, tag_data: UpdateTagDTO) -> TagDTO:
        updated_tag = self.tag_repo.update(tag_id, tag_data.dict(exclude_unset=True))
        if not updated_tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return TagDTO.model_validate(updated_tag)  # Convert ORM to DTO

    def delete_tag(self, tag_id: UUID) -> dict:
        if not self.tag_repo.delete(tag_id):
            raise HTTPException(status_code=404, detail="Tag not found")
        return {"message": f"Tag has been successfully deleted."}

    def get_files_by_tag(self, tag_id: UUID) -> List[TagDTO]:
        files = self.tag_repo.get_files_by_tag(tag_id)
        return [TagDTO.model_validate(file) for file in files]  # Convert ORM to DTO

    def get_learning_materials_by_tag(self, tag_id: UUID) -> List[TagDTO]:
        learning_materials = self.tag_repo.get_learning_materials_by_tag(tag_id)
        return [
            TagDTO.model_validate(material) for material in learning_materials
        ]  # Convert ORM to DTO
