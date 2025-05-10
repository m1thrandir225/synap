from typing import List, Dict, Any
from uuid import UUID

from fastapi import Depends
from app.services.openai_service import OpenAIService
from app.repositories import SummarizationRepository
from app.models.summarisation_response import OpenAIServiceResponse
from app.database import Summarization
from app.storage_provider import LocalStorageProvider
from app.models import SummarizationBase
from app.dependencies import get_openai_service, get_summarization_repository

class SummarizationService:
    def __init__(
        self,
        summarization_repo: SummarizationRepository,
        openai_service: OpenAIService,
        storage_service: LocalStorageProvider,
    ):
        self.summarization_repo = summarization_repo
        self.openai_service = openai_service
        self.storage_service = storage_service

    async def summarize_file_and_store(self, filename: str, file_id: UUID, original_filename: str = None) -> Summarization:
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
        )


        # TODO: Create recommendations here.
        # topics=ai_response.topics,


        return self.summarization_repo.create(summarization_data)

    async def create_manual_summary(self, summary_data: Dict[str, Any]) -> Summarization:
        """Creates a summary from provided data (e.g., for testing or manual input)."""
        db_summarization_data = SummarizationBase(**summary_data)
        return self.summarization_repo.create(db_summarization_data)

    async def get_all_summaries(self) -> List[Summarization]:
        return self.summarization_repo.get_all()

    async def get_summary_by_id(self, summary_id: int) -> Summarization | None:
        return self.summarization_repo.get_by_id(summary_id)

def get_summarization_service(
    repository: SummarizationRepository = Depends(get_summarization_repository),
    openai_service: OpenAIService = Depends(get_openai_service),
    storage_service: LocalStorageProvider = Depends(LocalStorageProvider)
) -> SummarizationService:
    return SummarizationService(
        summarization_repository=repository,
        openai_service=openai_service,
        storage_service=storage_service
    )