import datetime
from typing import List, Dict, Any
from uuid import UUID

from fastapi import Depends
from app.database import Summarization
from app.services.openai_service import OpenAIService
from app.services.learning_material_service import LearningMaterialService
from app.services.recommendation_service import RecommendationService
from app.storage_provider import get_local_storage_provider

from app.repositories import SummarizationRepository
from app.storage_provider import LocalStorageProvider

from app.models import SummarizationBase, CreateLearningMaterialDTO
from app.dependencies import  get_learning_material_service, get_openai_service, get_summarization_repository, get_recommendation_service
from app.models.summarization import OpenAIServiceResponse

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

    async def summarize_file_and_store(self, filename: str, file_id: UUID, summarization_name: str, original_filename: str = None) -> Summarization:
        """
        Retrieves a file, gets its summary from OpenAI, and stores it.
        'filename' is the name in storage, 'original_filename' is for record keeping.
        """
        if not original_filename:
            original_filename = filename

        base64_content = self.storage_service.get_file_base64(filename)

        ai_response: OpenAIServiceResponse = self.openai_service.get_summary_and_topics_from_base64_content(
            filename=original_filename,
            base64_content=base64_content
        )

        summarization_data = SummarizationBase(
            file_id=file_id,
            summary_text=ai_response.summarization,
            ai_model_used="gpt-4.1-2025-04-14",
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            name=summarization_name
        )
        # self.summarization_repository.create(summarization_data)

        topics = ai_response.topics
        materials_data = self.openai_service.get_learning_materials_for_topics(topics)

        
        for material in materials_data:
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
                learning_material=learning_material,
                query=ai_response.query  # must be set from OpenAIService
            )

        return self.summarization_repository.create(summarization_data)

    async def create_manual_summary(self, summary_data: Dict[str, Any]) -> Summarization:
        """Creates a summary from provided data (e.g., for testing or manual input)."""
        db_summarization_data = SummarizationBase(**summary_data)
        return self.summarization_repository.create(db_summarization_data)

    async def get_all_summaries(self) -> List[Summarization]:
        return self.summarization_repository.get_all()

    async def get_summary_by_id(self, summary_id: UUID) -> Summarization | None:
        return self.summarization_repository.get_by_id(summary_id)

def get_summarization_service(
    summarization_repository: SummarizationRepository = Depends(get_summarization_repository),
    openai_service: OpenAIService = Depends(get_openai_service),
    learning_material_service: LearningMaterialService = Depends(get_learning_material_service),
    recommendation_service: RecommendationService = Depends(get_recommendation_service),
    storage_service: LocalStorageProvider = Depends(get_local_storage_provider),
) -> SummarizationService:
    return SummarizationService(
        summarization_repository=summarization_repository, 
        openai_service=openai_service,
        learning_material_service=learning_material_service,
        recommendation_service=recommendation_service,
        storage_service=storage_service     
    )