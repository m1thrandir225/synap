from datetime import datetime
from typing import List, Optional
from uuid import UUID
import uuid

from fastapi import HTTPException
from app.database import Note
from app.repositories import NoteRepository
from app.models import CreateNoteDTO, UpdateNoteDTO, NoteDTO, CourseDTO


class NoteService:
    def __init__(self, note_repo: NoteRepository):
        self.repository = note_repo

    def _to_dto(self, note: Note):
        return NoteDTO.model_validate(note)

    def create_note(self, note_data: CreateNoteDTO, user_id: UUID) -> NoteDTO:
        existing_note: List[Note] = self.repository.get_notes_by_name(note_data.title)
        if existing_note:
            raise ValueError(f"the note with title: {note_data.title} already exists.")

        note_data_dump = note_data.model_dump()
        note_data_dump["id"] = uuid.uuid4()
        note_data_dump["user_id"] = user_id
        note_data_dump["created_at"] = datetime.now()
        note_data_dump["updated_at"] = datetime.now()
        created_note: Note = self.repository.create_note(note_data_dump)
        return self._to_dto(note=created_note)

    def get_note_by_id(self, note_id: UUID) -> Optional[NoteDTO]:
        note: Optional[Note] = self.repository.get_note_by_id(note_id)

        if not note:
            raise HTTPException(status_code=404, detail="Note was not found")

        return self._to_dto(note)

    def get_notes_by_name(self, name: str) -> List[NoteDTO]:
        notes: List[Note] = self.repository.get_notes_by_name(name)

        dtos = [self._to_dto(note) for note in notes]
        return dtos

    def get_notes_by_user_id(self, user_id: UUID) -> List[NoteDTO]:
        notes: List[Note] = self.repository.get_notes_by_user_id(user_id)
        dtos = [self._to_dto(note) for note in notes]
        return dtos

    def get_notes_by_course_id(self, course_id: UUID) -> List[NoteDTO]:
        notes: List[Note] = self.repository.get_notes_by_course_id(course_id)
        dtos = [self._to_dto(note) for note in notes]

        return dtos

    def update_note(self, note_id: UUID, note_data: UpdateNoteDTO) -> Optional[NoteDTO]:
        note_data_dump = note_data.model_dump(exclude_unset=True)
        note_data_dump["updated_at"] = datetime.now()
        note: Optional[Note] = self.repository.update_note(note_id, note_data_dump)

        if not note:
            raise HTTPException(
                status_code=500, detail="There was an error updating your note details."
            )
        return self._to_dto(note)

    def delete_note(self, note_id: UUID) -> bool:
        return self.repository.delete_note(note_id)
