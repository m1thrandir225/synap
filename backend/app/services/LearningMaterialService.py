from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from ..repositories.learning_material import LearningMaterialRepository
from ..schemas import LearningMaterialCreate, LearningMaterialUpdate
from ..database.models.learning_material import LearningMaterial

class LearningMaterialService:
    def __init__(self, db: Session):
        self.repository = LearningMaterialRepository(db)

    def create_learning_material(self, learning_material_data: LearningMaterialCreate) -> LearningMaterial:
        return self.repository.create_learning_material(learning_material_data)

    def get_learning_material_by_id(self, learning_material_id: UUID) -> Optional[LearningMaterial]:
        return self.repository.get_learning_material(learning_material_id)

    def list_learning_materials(self, skip: int = 0, limit: int = 100) -> List[LearningMaterial]:
        return self.repository.get_learning_materials(skip=skip, limit=limit)

    def update_learning_material(self, learning_material_id: UUID, learning_material_update: LearningMaterialUpdate) -> Optional[LearningMaterial]:
        return self.repository.update_learning_material(learning_material_id, learning_material_update)

    def delete_learning_material(self, learning_material_id: UUID) -> bool:
        return self.repository.delete_learning_material(learning_material_id)
