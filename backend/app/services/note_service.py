from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from ..models import Note
from ..repositories import NoteRepository
from models import CreateNoteDTO, UpdateNoteDTO

class NoteService:
    def __init__(self, note_repo: NoteRepository):
        self.repository = note_repo

    def create_note(
        self, note_data: CreateNoteDTO
    ) -> Note:
        return self.repository.create_note(note_data.dict())

    def get_all_notes(self) -> List[Note]:
        return self.repository.get_all_notes()
    
    def get_note_by_id(self, note_id: UUID) -> Optional[Note]:
        return self.repository.get_note_by_id(note_id)

    def get_notes_by_user_id(self, user_id: UUID) -> List[Note]:
        return self.repository.get_notes_by_user_id(user_id)

    def get_notes_by_course_id(self, course_id: UUID) -> List[Note]:
        return self.repository.get_notes_by_course_id(course_id)

    def update_note(
        self, note_id: UUID, note_data: UpdateNoteDTO
    ) -> Optional[Note]:
        return self.repository.update_note(note_id, note_data.dict(exclude_unset=True))

    def delete_note(self, note_id: UUID) -> bool:
        return self.repository.delete_note(note_id)
