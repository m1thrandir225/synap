from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, UUID4


class NoteBase(BaseModel):
    title: str
    content: str
    course_id: UUID4

    model_config = ConfigDict(from_attributes=True)


class CreateNoteDTO(NoteBase):
    pass


class UpdateNoteDTO(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    course_id: Optional[UUID4] = None


class NoteDTO(NoteBase):
    id: UUID4
    user_id: UUID4
    created_at: datetime
    updated_at: datetime
    course_id: UUID4


class CourseNoteDTO(NoteBase):
    id: UUID4
    user_id: UUID4
    created_at: datetime
    updated_at: datetime
