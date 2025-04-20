from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel, ConfigDict


class RecommendationInteractionBase(BaseModel):
    user_id: UUID4
    recommendation_id: UUID4
    interaction_type: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateRecommendationInteractionDTO(RecommendationInteractionBase):
    pass


class UpdateRecommendationInteractionDTO(BaseModel):
    interaction_type: Optional[str] = None


class RecommendationInteractionDTO(RecommendationInteractionBase):
    id: UUID4
    created_at: datetime
