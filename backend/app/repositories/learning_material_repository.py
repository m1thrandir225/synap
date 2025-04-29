from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from database import LearningMaterial

from models import CreateLearningMaterialDTO, UpdateLearningMaterialDTO


class LearningMaterialRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_learning_material(
        self, learning_material: LearningMaterialCreate
    ) -> LearningMaterial:
        db_learning_material = LearningMaterial(
            title=learning_material.title,
            description=learning_material.description,
            url=learning_material.url,
            material_type=learning_material.material_type,
        )
        self.db.add(db_learning_material)
        self.db.commit()
        self.db.refresh(db_learning_material)
        return db_learning_material

    def get_learning_material(
        self, learning_material_id: UUID
    ) -> Optional[LearningMaterial]:
        return (
            self.db.query(LearningMaterial)
            .filter(LearningMaterial.id == learning_material_id)
            .first()
        )

    def get_learning_materials(
        self, skip: int = 0, limit: int = 100
    ) -> List[LearningMaterial]:
        return self.db.query(LearningMaterial).offset(skip).limit(limit).all()

    def update_learning_material(
        self,
        learning_material_id: UUID,
        learning_material_update: LearningMaterialUpdate,
    ) -> Optional[LearningMaterial]:
        db_learning_material = (
            self.db.query(LearningMaterial)
            .filter(LearningMaterial.id == learning_material_id)
            .first()
        )
        if db_learning_material:
            for key, value in learning_material_update.dict(exclude_unset=True).items():
                setattr(db_learning_material, key, value)
            self.db.commit()
            self.db.refresh(db_learning_material)
            return db_learning_material
        return None

    def delete_learning_material(self, learning_material_id: UUID) -> bool:
        db_learning_material = (
            self.db.query(LearningMaterial)
            .filter(LearningMaterial.id == learning_material_id)
            .first()
        )
        if db_learning_material:
            self.db.delete(db_learning_material)
            self.db.commit()
            return True
        return False
