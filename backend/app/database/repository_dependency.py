from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repositories.RecommendationInteractionRepository import RecommendationInteractionRepository

def get_recommendation_interaction_repo(db: Session = Depends(get_db)) -> RecommendationInteractionRepository:
    return RecommendationInteractionRepository(db)
