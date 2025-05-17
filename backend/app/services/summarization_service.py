import datetime
from typing import List, Dict, Any
from uuid import UUID
from fastapi import HTTPException
from app.database import Summarization
from .openai_service import OpenAIService
from .learning_material_service import LearningMaterialService
from .recommendation_service import RecommendationService
from app.repositories import SummarizationRepository
from app.storage_provider import LocalStorageProvider
from app.models import (
    SummarizationBase,
    CreateLearningMaterialDTO,
    OpenAIServiceResponse,
    SummarizationDTO,
    UploadedFileDTO
)

class SummarizationService:
    def __init__(
        self,
        summarization_repository: SummarizationRepository,
        openai_service: OpenAIService,
        learning_material_service: LearningMaterialService,
        recommendation_service: RecommendationService,
        storage_service: LocalStorageProvider,
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
            name=summarization_name,
        )

        topics = ai_response.topics
        materials_data = self.openai_service.get_learning_materials_for_topics(topics)

        for material in materials_data:
            required_keys = {"title", "description", "material_type", "url"}
            if not required_keys.issubset(material):
                continue
            try:
                learning_material = (
                    self.learning_material_service.create_learning_material(
                        CreateLearningMaterialDTO(
                            title=material["title"],
                            description=material["description"],
                            material_type=material["material_type"],
                        ),
                        material["url"],
                    )
                )

                self.recommendation_service.create_recommendation(
                    file_id=file_id,
                    learning_material_id=learning_material.id,
                    relevance_score=material["relevance_score"],
                )
            except Exception as e:
                print(f"Failed to process material: {material}, error: {e}")

        return self.summarization_repository.create(summarization_data)  # type: ignore

    def create_manual_summary(self, summary_data: Dict[str, Any]) -> Summarization:
        """Creates a summary from provided data (e.g., for testing or manual input)."""
        db_summarization_data = SummarizationBase(**summary_data)
        return self.summarization_repository.create(db_summarization_data)  # type: ignore

    def get_all_summaries(self, user_id: UUID) -> List[SummarizationBase]:
        summaries = self.summarization_repository.get_all(user_id=user_id)

        if not summaries:
            raise HTTPException(status_code=404, detail="Not Found")
        summary_dto: List[SummarizationBase] = []
        for summary in summaries:
            dto = SummarizationBase.model_validate(summary)
            summary_dto.append(dto)

        return summary_dto   


    def get_summary_by_id(self, summary_id: UUID) -> SummarizationDTO:
        summary = self.summarization_repository.get_by_id(summary_id)

        if not summary :
            raise HTTPException(status_code=404, detail="Not found")
        
        recommendations = self.recommendation_service.get_recommendations_for_file(summary.file_id) # type: ignore
        uploaded_file_dto = UploadedFileDTO.model_validate(summary.file)

        dto = {
            "id": summary.id,
            "file_id": summary.file_id,
            "summary_text": summary.summary_text,
            "ai_model_used": summary.ai_model_used,
            "created_at": summary.created_at,
            "updated_at": summary.updated_at,
            "name": summary.name,
            "recommendations": recommendations,
            "file": uploaded_file_dto,
        }

        return SummarizationDTO.model_validate(dto) 
