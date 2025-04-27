from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from ..database.models.recommendation_interaction import RecommendationInteraction
from ..repositories.recommendation_interaction_repository import RecommendationInteractionRepository

class RecommendationInteractionService:
    def __init__(self, db: Session):
        self.repository = RecommendationInteractionRepository(db)

    def create_interaction(self, user_id: UUID, recommendation_id: UUID, interaction_type: str) -> RecommendationInteraction:
        return self.repository.create(user_id, recommendation_id, interaction_type)

    def get_interaction_by_id(self, interaction_id: UUID) -> Optional[RecommendationInteraction]:
        return self.repository.get_by_id(interaction_id)

    def get_interactions_by_user(self, user_id: UUID) -> List[RecommendationInteraction]:
        return self.repository.get_by_user_id(user_id)

    def get_interactions_by_recommendation(self, recommendation_id: UUID) -> List[RecommendationInteraction]:
        return self.repository.get_by_recommendation_id(recommendation_id)

    def update_interaction(self, interaction_id: UUID, new_interaction_type: str) -> Optional[RecommendationInteraction]:
        return self.repository.update_interaction_type(interaction_id, new_interaction_type)

    def delete_interaction(self, interaction_id: UUID) -> bool:
        return self.repository.delete(interaction_id)
