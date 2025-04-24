from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from ..database.models.learning_material_tag import LearningMaterialTag  # Adjust import as per your project structure
from uuid import UUID


class LearningMaterialTagRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_learning_material_id(
            self, learning_material_id: UUID
    ) -> List[LearningMaterialTag]:
        return (
            self.db.execute(
                select(LearningMaterialTag).filter(LearningMaterialTag.learning_material_id == learning_material_id)
            )
            .scalars()
            .all()
        )

    def get_by_tag_id(self, tag_id: UUID) -> List[LearningMaterialTag]:
        return (
            self.db.execute(
                select(LearningMaterialTag).filter(LearningMaterialTag.tag_id == tag_id)
            )
            .scalars()
            .all()
        )

    def create(
            self, learning_material_id: UUID, tag_id: UUID
    ) -> LearningMaterialTag:
        learning_material_tag = LearningMaterialTag(
            learning_material_id=learning_material_id, tag_id=tag_id
        )
        self.db.add(learning_material_tag)
        self.db.commit()
        self.db.refresh(learning_material_tag)
        return learning_material_tag

    def delete_by_learning_material_id(self, learning_material_id: UUID):
        self.db.execute(
            delete(LearningMaterialTag).filter(LearningMaterialTag.learning_material_id == learning_material_id)
        )
        self.db.commit()

    def delete_by_tag_id(self, tag_id: UUID):
        self.db.execute(
            delete(LearningMaterialTag).filter(LearningMaterialTag.tag_id == tag_id)
        )
        self.db.commit()

    def delete(self, learning_material_id: UUID, tag_id: UUID):
        self.db.execute(
            delete(LearningMaterialTag)
            .filter(
                LearningMaterialTag.learning_material_id == learning_material_id,
                LearningMaterialTag.tag_id == tag_id,
            )
        )
        self.db.commit()
