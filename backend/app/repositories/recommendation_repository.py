from sqlalchemy.orm import Session
from uuid import UUID
from database import Recommendation


class RecommendationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_recommendation(
        self, file_id: UUID, learning_material_id: UUID, relevance_score: float
    ) -> Recommendation:
        recommendation = Recommendation(
            file_id=file_id,
            learning_material_id=learning_material_id,
            relevance_score=relevance_score,
        )
        self.db.add(recommendation)
        self.db.commit()
        self.db.refresh(recommendation)
        return recommendation

    def get_recommendation_by_id(self, recommendation_id: UUID) -> Recommendation:
        return (
            self.db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

    def get_recommendations_by_file_id(self, file_id: UUID) -> list[Recommendation]:
        return (
            self.db.query(Recommendation)
            .filter(Recommendation.file_id == file_id)
            .all()
        )

    def get_recommendations_by_learning_material_id(
        self, learning_material_id: UUID
    ) -> list[Recommendation]:
        return (
            self.db.query(Recommendation)
            .filter(Recommendation.learning_material_id == learning_material_id)
            .all()
        )

    def update_recommendation_relevance(
        self, recommendation_id: UUID, relevance_score: float
    ) -> Recommendation:
        recommendation = (
            self.db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )
        if recommendation:
            recommendation.relevance_score = relevance_score
            self.db.commit()
            self.db.refresh(recommendation)
        return recommendation

    def delete_recommendation(self, recommendation_id: UUID) -> bool:
        recommendation = (
            self.db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )
        if recommendation:
            self.db.delete(recommendation)
            self.db.commit()
            return True
        return False
