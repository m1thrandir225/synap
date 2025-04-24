from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repositories import LectureRepository

def get_lecture_repository(db: Session = Depends(get_db)) -> LectureRepository:
    return LectureRepository(db)