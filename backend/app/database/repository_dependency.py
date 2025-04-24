from fastapi import Depends
from ..repositories import SummarizationRepository
from sqlalchemy.orm import Session
from db import get_db  # Assuming you have a function to get the DB session

def get_summarization_repository(db: Session = Depends(get_db)) -> SummarizationRepository:
    return SummarizationRepository(db)
