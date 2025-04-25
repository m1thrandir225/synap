from fastapi import FastAPI
from app.routers import example_router, authentication_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include external router
app.include_router(example_router.router)
app.include_router(authentication_router.router)


# sample code for routes
@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/status")
def health_status():
    return {"status": "healthy"}
