from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repositories import RecommendationRepository

def get_recommendation_repository(db: Session = Depends(get_db)) -> RecommendationRepository:
    return RecommendationRepository(db)