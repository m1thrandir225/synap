from typing import Optional
from pydantic import BaseModel, ConfigDict


class RecommendationInteractionBase(BaseModel):
    user_id: str
    recommendation_id: str
    interaction_type: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateRecommendationInteractionDTO(RecommendationInteractionBase):
    pass


class UpdateRecommendationInteractionDTO(BaseModel):
    interaction_type: Optional[str] = None


class RecommendationInteractionDTO(RecommendationInteractionBase):
    id: str
    created_at: str
