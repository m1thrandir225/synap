from fastapi import Depends
from sqlalchemy.orm import Session
from ..repositories import TagRepository
from db import get_db  # Assuming you have a function to get the DB session

def get_tag_repository(db: Session = Depends(get_db)) -> TagRepository:
    return TagRepository(db)