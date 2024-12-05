from hera.workflows import Workflow, Steps, models as m, Artifact, Container, WorkflowsService, HTTPArtifact, WorkflowStatus
from typing import List

# Function to create a container with mounted volume and specified arguments
def _get_container(name: str, image: str, command: List[str], args: List[str], mount_path: str) -> Container:
    return Container(
        name=name,
        image=image,
        command=command,
        args=args,
        volume_mounts=[m.VolumeMount(name="workflow-pvc", mount_path=mount_path)],
    )

# Define workflow context
with Workflow(
    generate_name="ogdc-recipe-ice-basins-pdg-",
    entrypoint="main",
    namespace="qgnet",
    service_account_name="qgnet",
    labels={
        "workflows.argoproj.io/archive-strategy": "false"
    },
    annotations={
        "workflows.argoproj.io/description": "This workflow creates PDG visualization tiles for the QGreenland ice basins layer."
    },
    volumes=[
        m.Volume(name="workflow-pvc", persistent_volume_claim={"claim_name": "workflow-pvc"})
    ],
    workflows_service=WorkflowsService(host="http://localhost:2746", verify_ssl=False)
) as wf:
    
    # Define the create-pdg-dir {input,output} container
    create_dir = _get_container(
        name="create-pdg-dir",
        image="busybox",
        command=["sh", "-c"],
        args=["mkdir -p {/mnt/workflow/output/staged,/mnt/workflow/input}"],
        mount_path="/mnt/workflow"
    )
    
    # Define the tiling container with inputs and outputs
    tiling_task = Container(
        name="staging",
        image="ghcr.io/rushirajnenuji/viz-staging:latest",
        command=["python"],
        args=["/mnt/workflow/runner.py"],
        inputs=[
            HTTPArtifact(
                name="viz-config-json",
                path="/mnt/workflow/config.json",
                url="https://gist.githubusercontent.com/rushirajnenuji/ad3a735e543c78483e4796386a34be35/raw/ee71e9b80c7c292e3b0315ac55596921c91b8b87/config.json"
                ),
            HTTPArtifact(
                name="pdgstaging-runner",
                path="/mnt/workflow/runner.py",
                url="https://gist.githubusercontent.com/rushirajnenuji/ad3a735e543c78483e4796386a34be35/raw/f53b687613df4053c6e506d2f5608fb9f288ab51/runner.py"
            ),
            HTTPArtifact(
                name="ice_basins_gpkg",
                path="/mnt/workflow/input/ice_basins.gpkg",
                url="https://github.com/rushirajnenuji/dataone-gse/raw/refs/heads/feature-argo-devk8s-deploy/gse-workflows/data/Ice_Basins.gpkg"
            )

        ],
        outputs=[Artifact(name="staging-output", path="/mnt/workflow/output/staged")],
        volume_mounts=[m.VolumeMount(name="workflow-pvc", mount_path="/mnt/workflow")]
    )

    # Define the main steps with create-output-dir and stage tasks
    with Steps(name="main") as main_steps:
        create_dir(name="create-pdg-dir")
        tiling_task(name="staging", dependencies=[create_dir])

# Workflow submission
wf.create()
