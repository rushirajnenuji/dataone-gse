from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# Workflow model
class Workflow:
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    # Optionally, add a serialize method
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

# In-memory store for workflows
workflows_db = []

# Create a sample workflow
sample_workflow1 = Workflow(id=1, name="Tiling", description="Convert large vector/raster data to smaller tiles")
sample_workflow2 = Workflow(id=2, name="Rasterization", description="Convert vector data to raster format")
sample_workflow3 = Workflow(id=3, name="3D Tiles", description="Display vector data in 3D Tiles format")

# Add sample workflows to the in-memory database
workflows_db.append(sample_workflow1)
workflows_db.append(sample_workflow2)
workflows_db.append(sample_workflow3)


# Endpoint to get all workflows
@router.get("/", response_model=List[dict])
async def get_workflows():
    return [workflow.serialize() for workflow in workflows_db]

# Endpoint to get a single workflow by ID
@router.get("/{workflow_id}", response_model=dict)
async def get_workflow(workflow_id: int):
    for workflow in workflows_db:
        if workflow.id == workflow_id:
            return workflow.serialize()
    raise HTTPException(status_code=404, detail="Workflow not found")
