from uuid import UUID
from app.repositories import RecommendationRepository
from app.database import Recommendation, LearningMaterial
from app.models import CreateRecommendationDTO, UpdateRecommendationDTO, RecommendationDTO
from datetime import datetime

class RecommendationService:
    def __init__(self, recom_repo: RecommendationRepository):
        self.recommendation_repository = recom_repo

    def _to_dto(self, recommendation: Recommendation | None):
        return RecommendationDTO(
            id=recommendation.id,
            file_id=recommendation.file_id,
            learning_material_id=recommendation.learning_material_id,
            relevance_score=recommendation.relevance_score,
            created_at=recommendation.created_at
    )

    def _calculate_score(self, query: str, learning_material_text: str) -> float:
        query_words = set(query.lower().split())
        lm_words = set(learning_material_text.lower().split())
        if not query_words:
            return 0.0
        return len(query_words & lm_words) / len(query_words)
    
    def create_recommendation(
    self,
    file_id: UUID,
    learning_material: LearningMaterial,
    query: str
) -> RecommendationDTO:
        learning_material_text = f"{learning_material.title} {learning_material.description}"
        relevance_score = self._calculate_score(query, learning_material_text)

        rec_data = {
        "file_id": file_id,
        "learning_material_id": learning_material.id,
        "created_at": datetime.now(),
        "relevance_score": relevance_score
        }

        created = self.recommendation_repository.create_recommendation(rec_data)

        # Here's where _to_dto matters:
        return self._to_dto(created)


    def get_recommendation(self, recommendation_id: UUID) -> Recommendation | None:
        return self.recommendation_repository.get_recommendation_by_id(
            recommendation_id
        )

    def get_recommendations_for_file(self, file_id: UUID) -> list[RecommendationDTO]:
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

    def _rank_recommendations(
        self, recommendations: list[Recommendation]
    ) -> list[Recommendation]:
        return sorted(recommendations, key=lambda rec: rec.relevance_score ,reverse=True
        )

    def get_top_recommendations(
        self, file_id: UUID, top_n: int = 5
    ) -> list[Recommendation]:
        recommendations = self.get_recommendations_for_file(file_id)
        return self.__rank_recommendations(recommendations)[:top_n]
