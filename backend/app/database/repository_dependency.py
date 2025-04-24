from fastapi import Depends
from ..repositories.UploadedFilesRepository import UploadedFileRepository
from sqlalchemy.orm import Session
from database import get_db 

def get_uploaded_file_repository(db: Session = Depends(get_db)) -> UploadedFileRepository:
    return UploadedFileRepository(db)
