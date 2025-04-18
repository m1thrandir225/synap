from typing import Optional
from pydantic import BaseModel, ConfigDict


class LectureBase(BaseModel):
    name: str
    summarization_id: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateLectureDTO(LectureBase):
    pass


class UpdateLectureDTO(BaseModel):
    name: Optional[str] = None
    summarization_id: Optional[str] = None


class LectureDTO(LectureBase):
    id: str
    created_at: str
