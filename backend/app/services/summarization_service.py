import datetime
from typing import List, Dict, Any
from uuid import UUID
from app.database import Summarization
from .openai_service import OpenAIService
from .learning_material_service import LearningMaterialService
from .recommendation_service import RecommendationService
from app.repositories import SummarizationRepository
from app.storage_provider import LocalStorageProvider
from app.models import SummarizationBase, CreateLearningMaterialDTO, OpenAIServiceResponse

class SummarizationService:
    def __init__(
        self,
        summarization_repository: SummarizationRepository,
        openai_service: OpenAIService,
        learning_material_service: LearningMaterialService,
        recommendation_service: RecommendationService,
        storage_service: LocalStorageProvider
    ):
        self.summarization_repository = summarization_repository
        self.openai_service = openai_service
        self.learning_material_service = learning_material_service
        self.recommendation_service = recommendation_service
        self.storage_service = storage_service

    async def summarize_file_and_store(self, filename: str, file_id: UUID, openai_id: str, summarization_name: str, original_filename: str | None = None) -> Summarization:
        """
        Retrieves a file, gets its summary from OpenAI, and stores it.
        'filename' is the name in storage, 'original_filename' is for record keeping.
        """
        if not original_filename:
            original_filename = filename

        ai_response: OpenAIServiceResponse = self.openai_service.get_summary_and_topics(openai_id=openai_id)

        summarization_data = SummarizationBase(
            file_id=file_id,
            summary_text=ai_response.summarization,
            ai_model_used="gpt-4.1-2025-04-14",
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            name=summarization_name
        )

        topics = ai_response.topics
        materials_data = self.openai_service.get_learning_materials_for_topics(topics)

        for material in materials_data:
            required_keys = {"title", "description", "material_type", "url"}
            if not required_keys.issubset(material):
                continue
            try:
                learning_material = self.learning_material_service.create_learning_material(
                    CreateLearningMaterialDTO(
                        title=material["title"],
                        description=material["description"],
                        material_type=material["material_type"]
                    ),
                    material["url"]
                )

                self.recommendation_service.create_recommendation(
                    file_id=file_id,
                    learning_material_id=learning_material.id,
                    relevance_score=material["relevance_score"]
                )
            except Exception as e:
                print(f"Failed to process material: {material}, error: {e}")

        return self.summarization_repository.create(summarization_data) # type: ignore

    async def create_manual_summary(self, summary_data: Dict[str, Any]) -> Summarization:
        """Creates a summary from provided data (e.g., for testing or manual input)."""
        db_summarization_data = SummarizationBase(**summary_data)
        return self.summarization_repository.create(db_summarization_data) # type: ignore

    async def get_all_summaries(self) -> List[Summarization]:
        return self.summarization_repository.get_all()

    async def get_summary_by_id(self, summary_id: UUID) -> Summarization | None:
        return self.summarization_repository.get_by_id(summary_id)
