from typing import List, Optional
from uuid import UUID
from app.repositories import LearningMaterialRepository
from app.database import LearningMaterial
from app.models import CreateLearningMaterialDTO, UpdateLearningMaterialDTO, LearningMaterialDTO, RecommendationDTO
from datetime import datetime

class LearningMaterialService:
    def __init__(self, lm: LearningMaterialRepository):
        self.repository = lm

    def _to_dto(self, lm: LearningMaterial | None):
        recommendations: List[RecommendationDTO] = []
        for rec in lm.recommendations:
            recommendations.append(
                RecommendationDTO(
                    id=rec.id,
                    file_id=rec.file_id,
                    learning_material_id=rec.learning_material_id,
                    relevance_score=rec.relevance_score,
                    created_at=rec.created_at
            )
        )
        return LearningMaterialDTO(
            title=lm.title,
            description=lm.description,
            material_type=lm.material_type,
            id=lm.id,
            url=lm.url,
            created_at=lm.created_at,
            recommendations=recommendations
        )
    def create_learning_material(
        self, lm_data: CreateLearningMaterialDTO, url: str
    ) -> LearningMaterialDTO:
        lm_model_dump = lm_data.model_dump()
        lm_model_dump["created_at"] = datetime.now()
        lm_model_dump["url"] = url
        created_lm: LearningMaterial = self.repository.create_learning_material(lm_model_dump)
        return self._to_dto(created_lm)

    def get_learning_material_by_id(
        self, learning_material_id: UUID
    ) -> Optional[LearningMaterialDTO]:
        return self.repository.get_learning_material(learning_material_id)

    def list_learning_materials(
        self, skip: int = 0, limit: int = 100
    ) -> List[LearningMaterialDTO]:
        lm: List[LearningMaterial] = self.repository.get_learning_materials(skip=skip, limit=limit)
        lm_data = []
        for l in lm:
            lm_data.append(self._to_dto(lm=l))
        return lm_data

    def update_learning_material(
        self, learning_material_id: UUID, lm_data: UpdateLearningMaterialDTO
    ) -> Optional[LearningMaterialDTO]:
        return self.repository.update_learning_material(
            learning_material_id, lm_data.dict(exclude_unset=True)
        )

    def delete_learning_material(self, learning_material_id: UUID) -> bool:
        return self.repository.delete_learning_material(learning_material_id)
