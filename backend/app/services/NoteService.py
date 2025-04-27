from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from ..models import Note
from ..repositories import NoteRepository


class NoteService:
    def __init__(self, db: Session):
        self.repository = NoteRepository(db)

    def create_note(
        self, title: str, content: str, user_id: UUID, course_id: UUID
    ) -> Note:
        return self.repository.create_note(title, content, user_id, course_id)

    def get_note_by_id(self, note_id: UUID) -> Optional[Note]:
        return self.repository.get_note_by_id(note_id)

    def get_notes_by_user_id(self, user_id: UUID) -> List[Note]:
        return self.repository.get_notes_by_user_id(user_id)

    def get_notes_by_course_id(self, course_id: UUID) -> List[Note]:
        return self.repository.get_notes_by_course_id(course_id)

    def update_note(
        self, note_id: UUID, title: Optional[str] = None, content: Optional[str] = None
    ) -> Optional[Note]:
        return self.repository.update_note(note_id, title, content)

    def delete_note(self, note_id: UUID) -> bool:
        return self.repository.delete_note(note_id)
