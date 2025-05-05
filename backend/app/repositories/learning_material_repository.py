from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from app.database import LearningMaterial
from sqlalchemy import func


class LearningMaterialRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_learning_material(self, lm_data: dict) -> LearningMaterial:
        db_learning_material = LearningMaterial(**lm_data)
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
        lm_data: dict,
    ) -> Optional[LearningMaterial]:
        db_learning_material = self.get_learning_material(learning_material_id)
        if db_learning_material:
            for key, value in lm_data.items():
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
