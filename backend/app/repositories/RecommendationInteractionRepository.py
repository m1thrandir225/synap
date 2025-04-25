from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models import RecommendationInteraction

class RecommendationInteractionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: UUID, recommendation_id: UUID, interaction_type: str) -> RecommendationInteraction:
        try:
            new_interaction = RecommendationInteraction(
                user_id=user_id,
                recommendation_id=recommendation_id,
                interaction_type=interaction_type
            )
            self.db.add(new_interaction)
            self.db.commit()
            self.db.refresh(new_interaction)
            return new_interaction
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def get_by_id(self, interaction_id: UUID) -> Optional[RecommendationInteraction]:
        return self.db.query(RecommendationInteraction).filter(RecommendationInteraction.id == interaction_id).first()

    def get_by_user_id(self, user_id: UUID) -> List[RecommendationInteraction]:
        return self.db.query(RecommendationInteraction).filter(RecommendationInteraction.user_id == user_id).all()

    def get_by_recommendation_id(self, recommendation_id: UUID) -> List[RecommendationInteraction]:
        return self.db.query(RecommendationInteraction).filter(RecommendationInteraction.recommendation_id == recommendation_id).all()

    def update_interaction_type(self, interaction_id: UUID, new_interaction_type: str) -> Optional[RecommendationInteraction]:
        interaction = self.get_by_id(interaction_id)
        if interaction:
            interaction.interaction_type = new_interaction_type
            self.db.commit()
            self.db.refresh(interaction)
            return interaction
        return None

    def delete(self, interaction_id: UUID) -> bool:
        interaction = self.get_by_id(interaction_id)
        if interaction:
            self.db.delete(interaction)
            self.db.commit()
            return True
        return False
