from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import RecommendationInteraction
from sqlalchemy import func

class RecommendationInteractionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self, ri_data: dict
    ) -> RecommendationInteraction:
        try:
            new_interaction = RecommendationInteraction(
               **ri_data
            )
            self.db.add(new_interaction)
            self.db.commit()
            self.db.refresh(new_interaction)
            return new_interaction
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def get_by_id(self, interaction_id: UUID) -> Optional[RecommendationInteraction]:
        return (
            self.db.query(RecommendationInteraction)
            .filter(RecommendationInteraction.id == interaction_id)
            .first()
        )

    def get_by_user_id(self, user_id: UUID) -> List[RecommendationInteraction]:
        return (
            self.db.query(RecommendationInteraction)
            .filter(RecommendationInteraction.user_id == user_id)
            .all()
        )

    def get_by_recommendation_id(
        self, recommendation_id: UUID
    ) -> List[RecommendationInteraction]:
        return (
            self.db.query(RecommendationInteraction)
            .filter(RecommendationInteraction.recommendation_id == recommendation_id)
            .all()
        )

    def update_interaction_type(
        self, interaction_id: UUID, ri_data: dict
    ) -> Optional[RecommendationInteraction]:
        interaction = self.get_by_id(interaction_id)
        for key, value in ri_data.items():
            setattr(interaction, key, value)
        self.db.commit()
        self.db.refresh(interaction)
        return interaction

    def delete(self, interaction_id: UUID) -> bool:
        interaction = self.get_by_id(interaction_id)
        if interaction:
            self.db.delete(interaction)
            self.db.commit()
            return True
        return False
