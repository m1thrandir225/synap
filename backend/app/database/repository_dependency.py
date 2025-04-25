from fastapi import Depends
from sqlalchemy.orm import Session
from ..repositories import UserRepository, TagRepository
from ..repositories.UploadedFilesRepository import UploadedFileRepository
from ..repositories.CourseRepository import CourseRepository

# Dependency functions for repositories
def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)
  
def get_uploaded_file_repository(db: Session = Depends(get_db)) -> UploadedFileRepository:
    return UploadedFileRepository(db)
  
def get_course_repository(db: Session = Depends(get_db)) -> CourseRepository:
    return CourseRepository(db)
def get_tag_repository(db: Session = Depends(get_db)) -> TagRepository:
    return TagRepository(db)

