from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from ..repositories.learning_material import LearningMaterialRepository
from ..schemas import LearningMaterialCreate, LearningMaterialUpdate
from ..database.models.learning_material import LearningMaterial
from models import CreateLearningMaterialDTO, UpdateLearningMaterialDTO

class LearningMaterialService:
    def __init__(self, lm: LearningMaterialRepository):
        self.repository = lm

    def create_learning_material(self, lm_data: CreateLearningMaterialDTO) -> LearningMaterial:
        return self.repository.create_learning_material(lm_data.dict())

    def get_learning_material_by_id(self, learning_material_id: UUID) -> Optional[LearningMaterial]:
        return self.repository.get_learning_material(learning_material_id)

    def list_learning_materials(self, skip: int = 0, limit: int = 100) -> List[LearningMaterial]:
        return self.repository.get_learning_materials(skip=skip, limit=limit)

    def update_learning_material(self, learning_material_id: UUID, lm_data: UpdateLearningMaterialDTO) -> Optional[LearningMaterial]:
        return self.repository.update_learning_material(learning_material_id, lm_data.dict(exclude_unset=True))

    def delete_learning_material(self, learning_material_id: UUID) -> bool:
        return self.repository.delete_learning_material(learning_material_id)
