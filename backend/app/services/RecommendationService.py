from uuid import UUID
from sqlalchemy.orm import Session
from ..repositories.recommendation_repository import RecommendationRepository
from ..database.models.recommendation import Recommendation

class RecommendationService:
    def __init__(self, recom_repo: RecommendationRepository):
        self.recommendation_repository = recom_repo

    def create_recommendation(self, file_id: UUID, learning_material_id: UUID, relevance_score: float) -> Recommendation:
        return self.recommendation_repository.create_recommendation(file_id, learning_material_id, relevance_score)

    def get_recommendation(self, recommendation_id: UUID) -> Recommendation | None:
        return self.recommendation_repository.get_recommendation_by_id(recommendation_id)

    def get_recommendations_for_file(self, file_id: UUID) -> list[Recommendation]:
        return self.recommendation_repository.get_recommendations_by_file_id(file_id)

    def get_recommendations_for_learning_material(self, learning_material_id: UUID) -> list[Recommendation]:
        return self.recommendation_repository.get_recommendations_by_learning_material_id(learning_material_id)

    def update_relevance_score(self, recommendation_id: UUID, relevance_score: float) -> Recommendation | None:
        return self.recommendation_repository.update_recommendation_relevance(recommendation_id, relevance_score)

    def delete_recommendation(self, recommendation_id: UUID) -> bool:
        return self.recommendation_repository.delete_recommendation(recommendation_id)

    def rank_recommendations(self, recommendations: list[Recommendation]) -> list[Recommendation]:
        return sorted(recommendations, key=lambda rec: rec.relevance_score, reverse=True)

    def get_top_recommendations(self, file_id: UUID, top_n: int = 5) -> list[Recommendation]:
        recommendations = self.get_recommendations_for_file(file_id)
        return self.rank_recommendations(recommendations)[:top_n]
