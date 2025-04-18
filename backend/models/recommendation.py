from typing import Optional
from pydantic import BaseModel, ConfigDict


class RecommendationBase(BaseModel):
    file_id: str
    learning_material_id: str


class CreateRecommendationDTO(RecommendationBase):
    pass


class UpdateRecommendationDTO(BaseModel):
    file_id: Optional[str] = None
    learning_material_id: Optional[str] = None


class RecommendationDTO(RecommendationBase):
    id: str
    relevance_score: float
    created_at: str
