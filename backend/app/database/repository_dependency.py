from fastapi import Depends
from sqlalchemy.orm import Session
from db import get_db
from ..repositories import UserRepository

# Dependency functions for repositories

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)