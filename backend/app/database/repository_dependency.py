from fastapi import Depends
from ..repositories import FileTagRepository
from sqlalchemy.orm import Session
from db import get_db  # Assuming you have a function to get the DB session

def get_file_tag_repository(db: Session = Depends(get_db)) -> FileTagRepository:
    return FileTagRepository(db)
