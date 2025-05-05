from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.database import RecommendationInteraction
from app.repositories import RecommendationInteractionRepository
from app.models import (
    CreateRecommendationInteractionDTO,
    UpdateRecommendationInteractionDTO,
)


class RecommendationInteractionService:
    def __init__(self, inte_repo: RecommendationInteractionRepository):
        self.repository = inte_repo

    def create_interaction(
        self, ri_data: CreateRecommendationInteractionDTO
    ) -> RecommendationInteraction:
        return self.repository.create(ri_data.dict())

    def get_interaction_by_id(
        self, interaction_id: UUID
    ) -> Optional[RecommendationInteraction]:
        return self.repository.get_by_id(interaction_id)

    def get_interactions_by_user(
        self, user_id: UUID
    ) -> List[RecommendationInteraction]:
        return self.repository.get_by_user_id(user_id)

    def get_interactions_by_recommendation(
        self, recommendation_id: UUID
    ) -> List[RecommendationInteraction]:
        return self.repository.get_by_recommendation_id(recommendation_id)

    def update_interaction(
        self, interaction_id: UUID, ri_data: UpdateRecommendationInteractionDTO
    ) -> Optional[RecommendationInteraction]:
        return self.repository.update_interaction_type(
            interaction_id, ri_data.dict(exclude_unset=True)
        )

    def delete_interaction(self, interaction_id: UUID) -> bool:
        return self.repository.delete(interaction_id)
