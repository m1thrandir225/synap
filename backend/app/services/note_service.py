from datetime import datetime
from typing import List, Optional
from uuid import UUID
import uuid
from app.database import Note
from app.repositories import NoteRepository
from app.models import CreateNoteDTO, UpdateNoteDTO, NoteDTO, CourseDTO


class NoteService:
    def __init__(self, note_repo: NoteRepository):
        self.repository = note_repo

    def _to_dto(self, note: Note | None):
        if note is None:
            return None
        return NoteDTO(
            title=note.title,
            course=CourseDTO(id=note.course.id,
                             description=note.course.description, 
                             name=note.course.name,
                             user_id=note.course.user_id,
                             created_at=note.course.created_at,
                             updated_at=note.course.updated_at,
                             notes=[],
                             uploaded_files=[], #or uploaded_files=note.course.uploaded_files kako sakas
                             summaries=[]),     #or summaries=note.course.summaries kako sakas
            id=note.id,
            user_id=note.user_id,
            course_id=note.course.id,
            content=note.content,
            created_at=note.created_at,
            updated_at=note.updated_at
        )
    
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

    #REDUNDANT, the get_notes_by_user_id already returns all of the notes created by the current user.
    # def get_all_notes(self) -> List[NoteDTO]:
    #     notes: list[Note] = self.repository.get_all_notes()
    #     notes_dto = []
    #     for note in notes:
    #         notes_dto.append(self._to_dto(note=note))
    #     return notes_dto

    def get_note_by_id(self, note_id: UUID) -> Optional[NoteDTO]:
        note: Optional[Note] = self.repository.get_note_by_id(note_id)
        return self._to_dto(note=note)

    def get_notes_by_name(self, name: str) -> List[NoteDTO]:
        notes: List[Note] = self.repository.get_notes_by_name(name)
        note_dto = []
        for n in notes:
            note_dto.append(self._to_dto(note=n))
        return note_dto
    
    def get_notes_by_user_id(self, user_id: UUID) -> List[NoteDTO]:
        notes: List[Note] = self.repository.get_notes_by_user_id(user_id)
        note_dto = []
        for n in notes:
            note_dto.append(self._to_dto(note=n))
        return note_dto

    def get_notes_by_course_id(self, course_id: UUID) -> List[NoteDTO]:
        notes: List[Note] = self.repository.get_notes_by_course_id(course_id)
        note_dto = []
        for n in notes:
            note_dto.append(self._to_dto(note=n))
        return note_dto

    def update_note(self, note_id: UUID, note_data: UpdateNoteDTO) -> Optional[NoteDTO]:
        note_data_dump = note_data.model_dump(exclude_unset=True)
        note_data_dump["updated_at"] = datetime.now()
        note: Optional[Note] = self.repository.update_note(note_id, note_data_dump)
        return self._to_dto(note=note)

    def delete_note(self, note_id: UUID) -> bool:
        return self.repository.delete_note(note_id)
