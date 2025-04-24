from fastapi import Depends
from sqlalchemy.orm import Session
from db import get_db  # Assuming you have a function that provides a DB session
from ..repositories.CourseRepository import CourseRepository

def get_course_repository(db: Session = Depends(get_db)) -> CourseRepository:
    return CourseRepository(db)
