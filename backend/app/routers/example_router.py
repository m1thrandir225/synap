from fastapi import APIRouter

router = APIRouter(prefix="/example_router", tags=["example_router"])


# http://localhost:3000/example_router
@router.get("/")
def example():
    return {"text": "hello from example router"}
