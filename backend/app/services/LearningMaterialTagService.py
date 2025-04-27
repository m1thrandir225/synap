from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from ..database.models.learning_material_tag import LearningMaterialTag
from ..repositories.LearningMaterialTagRepository import LearningMaterialTagRepository


class LearningMaterialTagService:
    def __init__(self, db: Session):
        self.repository = LearningMaterialTagRepository(db)

    def get_tags_by_learning_material(self, learning_material_id: UUID) -> List[LearningMaterialTag]:
        return self.repository.get_by_learning_material_id(learning_material_id)

    def get_learning_materials_by_tag(self, tag_id: UUID) -> List[LearningMaterialTag]:
        return self.repository.get_by_tag_id(tag_id)

    def add_tag_to_learning_material(self, learning_material_id: UUID, tag_id: UUID) -> LearningMaterialTag:
        return self.repository.create(learning_material_id, tag_id)

    def remove_tags_from_learning_material(self, learning_material_id: UUID):
        self.repository.delete_by_learning_material_id(learning_material_id)

    def remove_learning_materials_from_tag(self, tag_id: UUID):
        self.repository.delete_by_tag_id(tag_id)

    def remove_tag_from_learning_material(self, learning_material_id: UUID, tag_id: UUID):
        self.repository.delete(learning_material_id, tag_id)
