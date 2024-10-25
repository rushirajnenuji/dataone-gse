from fastapi import FastAPI
from app.api.v1.workflows import router as workflows_router

app = FastAPI(title="Workflow Management API")

# Include the workflows router
app.include_router(workflows_router, prefix="/api/v1/workflows")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Workflow Management API"}
