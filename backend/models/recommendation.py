from datetime import datetime
from typing import List, Optional
from pydantic import UUID4, BaseModel, ConfigDict
from .recommendation_interaction import RecommendationInteractionDTO


class RecommendationBase(BaseModel):
    file_id: UUID4
    learning_material_id: UUID4

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateRecommendationDTO(RecommendationBase):
    pass


class UpdateRecommendationDTO(BaseModel):
    file_id: Optional[str] = None
    learning_material_id: Optional[str] = None


class RecommendationDTO(RecommendationBase):
    id: UUID4
    relevance_score: float
    interactions: List[RecommendationInteractionDTO]

    created_at: datetime
