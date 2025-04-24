from sqlalchemy.orm import Session
from fastapi import Depends
from ..database.db import get_db  # Import your session maker function
from ..repositories import NoteRepository


# Dependency function to get the repository
def get_note_repository(db: Session = Depends(get_db)) -> NoteRepository:
    return NoteRepository(db)
