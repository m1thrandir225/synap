from fastapi import Depends
from sqlalchemy.orm import Session
from db import get_db
from ..repositories import UserRepository
from ..repositories.UploadedFilesRepository import UploadedFileRepository

# Dependency functions for repositories
def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_uploaded_file_repository(db: Session = Depends(get_db)) -> UploadedFileRepository:
    return UploadedFileRepository(db)

