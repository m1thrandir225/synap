from fastapi import FastAPI
from app.routers import example_router, authentication_router, file_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api/v1")

origins = ["http://localhost:3001"]

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include external routers
app.include_router(example_router.router)
app.include_router(authentication_router.router)
app.include_router(file_router.router)


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/status")
def health_status():
    return {"status": "healthy"}
