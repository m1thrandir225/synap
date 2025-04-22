from fastapi import FastAPI
from backend.routers import example_router, authentication_router
app = FastAPI()

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
