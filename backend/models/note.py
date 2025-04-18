from typing import Optional
from pydantic import BaseModel, ConfigDict, UUID4


class NoteBase(BaseModel):
    title: str
    content: str
    course_id: UUID4

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateNoteDTO(NoteBase):
    pass


class UpdateNoteDTO(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    course_id: Optional[str] = None


class NoteResponse(NoteBase):
    # all fields +
    user_id: UUID4
    created_at: str
    updated_at: str
    # TODO: include relationships
