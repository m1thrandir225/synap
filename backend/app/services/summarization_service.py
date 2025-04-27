from typing import List, Optional
from uuid import UUID
from database import Lecture
from sqlalchemy.orm import Session

from repositories import SummarizationRepository
from models import SummarizationDTO, UploadedFileDTO

class SummarizationService:
    def __init__(self, summarization_repo: SummarizationRepository):
        self.summarization_repo = summarization_repo

    def get_by_id(self, summarization_id: UUID) -> Optional[SummarizationDTO]:
        summarization = self.summarization_repo.get_by_id(summarization_id)
        if summarization:
            # Convert to DTO (assuming you have a method for this)
            return SummarizationDTO.model_validate(summarization)
        return None

    def get_by_file_id(self, file_id: UUID) -> Optional[SummarizationDTO]:
        summarization = self.summarization_repo.get_by_file_id(file_id)
        if summarization:
            return SummarizationDTO.model_validate(summarization)
        return None

    def get_all(self) -> List[SummarizationDTO]:
        summarizations = self.summarization_repo.get_all()
        return [SummarizationDTO.model_validate(s) for s in summarizations]

    def create(self, summarization_data: dict) -> Optional[SummarizationDTO]:
        summarization = self.summarization_repo.create(summarization_data)
        if summarization:
            return SummarizationDTO.model_validate(summarization)
        return None

    def update(self, summarization_id: UUID, summarization_data: dict) -> Optional[SummarizationDTO]:
        summarization = self.summarization_repo.update(summarization_id, summarization_data)
        if summarization:
            return SummarizationDTO.model_validate(summarization)
        return None

    def delete(self, summarization_id: UUID) -> bool:
        return self.summarization_repo.delete(summarization_id)

    def get_file_by_summarization(self, summarization_id: UUID) -> Optional[UploadedFileDTO]:
        uploaded_file = self.summarization_repo.get_file_by_summarization(summarization_id)
        if uploaded_file:
            return UploadedFileDTO.model_validate(uploaded_file)
        return None

    def get_lecture_by_summarization(self, summarization_id: UUID) -> Optional[Lecture]:
        return self.summarization_repo.get_lecture_by_summarization(summarization_id)
