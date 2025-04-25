from fastapi import Depends
from sqlalchemy.orm import Session
from db import get_db  
from ..repositories import UserRepository, TagRepository, FileTagRepository, SummarizationRepository
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
  
def get_file_tag_repository(db: Session = Depends(get_db)) -> FileTagRepository:
    return FileTagRepository(db)
  
def get_summarization_repository(db: Session = Depends(get_db)) -> SummarizationRepository:
    return SummarizationRepository(db)
