from fastapi import Depends
from sqlalchemy.orm import Session
from ..repositories.LearningMaterialRepository import LearningMaterialRepository
from ..database.db import get_db

def get_learning_material_repository(db: Session = Depends(get_db)) -> LearningMaterialRepository:
    return LearningMaterialRepository(db)