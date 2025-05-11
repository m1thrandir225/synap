from sqlalchemy.orm import Session
from sqlalchemy import func
from uuid import UUID
from app.database import Recommendation


class RecommendationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_recommendation(self, recom_data: dict) -> Recommendation:
        recommendation = Recommendation(**recom_data)
        self.db.add(recommendation)
        self.db.commit()
        self.db.refresh(recommendation)
        return recommendation

    def get_recommendation_by_id(self, recommendation_id: UUID) -> Recommendation | None:
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
        self, recommendation_id: UUID, recom_data: dict
    ) -> Recommendation | None:
        recommendation = self.get_recommendation_by_id(recommendation_id)
        for key, value in recom_data.items():
            setattr(recommendation, key, value)
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
