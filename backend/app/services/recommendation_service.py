from uuid import UUID
from app.repositories import RecommendationRepository
from app.database import Recommendation
from app.models import CreateRecommendationDTO, UpdateRecommendationDTO


class RecommendationService:
    def __init__(self, recom_repo: RecommendationRepository):
        self.recommendation_repository = recom_repo

    def create_recommendation(
        self, recom_data: CreateRecommendationDTO
    ) -> Recommendation:
        return self.recommendation_repository.create_recommendation(recom_data.model_dump())

    def get_recommendation(self, recommendation_id: UUID) -> Recommendation | None:
        return self.recommendation_repository.get_recommendation_by_id(
            recommendation_id
        )

    def get_recommendations_for_file(self, file_id: UUID) -> list[Recommendation]:
        return self.recommendation_repository.get_recommendations_by_file_id(file_id)

    def get_recommendations_for_learning_material(
        self, learning_material_id: UUID
    ) -> list[Recommendation]:
        return (
            self.recommendation_repository.get_recommendations_by_learning_material_id(
                learning_material_id
            )
        )

    def update_relevance_score(
        self, recommendation_id: UUID, recom_data: UpdateRecommendationDTO
    ) -> Recommendation | None:
        return self.recommendation_repository.update_recommendation_relevance(
            recommendation_id, recom_data.dict(exclude_unset=True)
        )

    def delete_recommendation(self, recommendation_id: UUID) -> bool:
        return self.recommendation_repository.delete_recommendation(recommendation_id)

    def __rank_recommendations(
        self, recommendations: list[Recommendation]
    ) -> list[Recommendation]:
        return sorted(recommendations, key=lambda rec: rec.relevance_score ,reverse=True
        ) # type: ignore

    def get_top_recommendations(
        self, file_id: UUID, top_n: int = 5
    ) -> list[Recommendation]:
        recommendations = self.get_recommendations_for_file(file_id)
        return self.__rank_recommendations(recommendations)[:top_n]
