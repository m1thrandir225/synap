from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from uuid import UUID
from datetime import datetime
from database import Note


class NoteRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_note(
        self, note_data: dict
    ) -> Note:
        note = Note(
            **note_data
        )
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)
        return note

    def get_note_by_id(self, note_id: UUID) -> Optional[Note]:
        return self.db.query(Note).filter(Note.id == note_id).first()

    def get_notes_by_user_id(self, user_id: UUID) -> List[Note]:
        return self.db.query(Note).filter(Note.user_id == user_id).all()

    def get_notes_by_course_id(self, course_id: UUID) -> List[Note]:
        return self.db.query(Note).filter(Note.course_id == course_id).all()

    def update_note(
        self, note_id: UUID, note_data: dict
    ) -> Optional[Note]:
        note = self.get_note_by_id(note_id)
        for key, value in note_data.items():
            setattr(note, key, value)
        self.db.commit()
        self.db.refresh(note)
        return note

    def delete_note(self, note_id: UUID) -> bool:
        note = self.db.query(Note).filter(Note.id == note_id).first()
        if note:
            self.db.delete(note)
            self.db.commit()
            return True
        return False
