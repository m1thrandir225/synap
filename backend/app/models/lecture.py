from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel, ConfigDict
from .summarization import SummarizationDTO


class LectureBase(BaseModel):
    name: str
    summarization_id: UUID4

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateLectureDTO(LectureBase):
    id: Optional[UUID4] = None


class UpdateLectureDTO(BaseModel):
    name: Optional[str] = None
    summarization_id: Optional[str] = None


class LectureDTO(LectureBase):
    id: UUID4
    created_at: datetime

    summarization: SummarizationDTO
