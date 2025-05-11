from fastapi import APIRouter
from app.database.db import get_db

router = APIRouter(prefix="/example_router", tags=["example_router"])


@router.get("/")
def example():
    return {"text": "hello from example router"}
