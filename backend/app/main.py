from fastapi import FastAPI
from app.routers import example_router, authentication_router
from app.routers import file_router
app = FastAPI()

app.include_router(example_router.router)
app.include_router(authentication_router.router)
app.include_router(file_router.router)


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/status")
def health_status():
    return {"status": "healthy"}
