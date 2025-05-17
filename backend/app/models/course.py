from typing import ForwardRef, List, Optional
from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime
from .summarization import UploadedFileDTO, SummarizationBase
from .note import CourseNoteDTO


class CourseBase(BaseModel):
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateCourseDTO(CourseBase):
    pass


class UpdateCourseDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class CourseDTO(CourseBase):
    id: UUID4
    user_id: UUID4
    created_at: datetime
    updated_at: datetime
    notes: List[CourseNoteDTO]
    uploaded_files: List[UploadedFileDTO]
    summaries: Optional[List[SummarizationBase]]


CourseDTO.model_rebuild()
