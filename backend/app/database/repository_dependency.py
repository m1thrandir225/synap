from fastapi import Depends
from sqlalchemy.orm import Session
from ..repositories.LearningMaterialTagRepository import LearningMaterialTagRepository
from ..database.db import get_db

def get_learning_material_tag_repository(db: Session = Depends(get_db)) -> LearningMaterialTagRepository:
    return LearningMaterialTagRepository(db)
