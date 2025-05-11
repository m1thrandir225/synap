from fastapi import FastAPI
from app.routers import authentication_router, file_router, note_router, course_router, summarization_router, example_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api/v1")

origins = ["http://localhost:3001"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication_router.router)
app.include_router(file_router.router)
app.include_router(note_router.router)
app.include_router(course_router.router)
app.include_router(summarization_router.router)
app.include_router(example_router.router)


@app.get("/status")
def health_status():
    return {"status": "healthy"}
