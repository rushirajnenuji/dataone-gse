### DataONE GeoSpatial Engine 

```markdown
# DataONE Geospatial Engine

The DataONE Geospatial Engine is a scalable workflow service built with FastAPI, designed to manage and display geospatial workflows. This project aims to facilitate the integration and processing of geospatial data, leveraging modern technologies and best practices.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rushirajnenuji/dataone-geospatial-engine.git
   cd dataone-geospatial-engine
   ```

2. **Navigate to the Project Directory**:
   Ensure you are in the root directory where `pyproject.toml` is located.

3. **Install Dependencies**:
   You can use Poetry to install the required dependencies. Make sure your virtual environment is activated (if using one):
   ```bash
   poetry install
   ```

4. **Activate the Virtual Environment** (optional):
   If you are using Poetry, you can activate the environment with:
   ```bash
   poetry shell
   ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload
```

- **`src.app.main:app`**: This specifies the path to the FastAPI application.
- **`--host 0.0.0.0`**: Allows the application to be accessible from any IP address.
- **`--port 8000`**: The port on which the application will run.
- **`--reload`**: Enables auto-reload during development.

Once the application is running, you can access it at [http://localhost:8000](http://localhost:8000).

## API Endpoints

### Base URL
- `/api/v1/workflows` - Base endpoint for managing workflows.

### Endpoints
- **GET /api/v1/workflows/**: Retrieve a list of all workflows.
- **GET /api/v1/workflows/{workflow_id}**: Retrieve a specific workflow by ID.

### Example Usage

To retrieve a specific workflow, send a GET request to `/api/v1/workflows/{workflow_id}` where `{workflow_id}` is the ID of the workflow you want to retrieve. Here's an example using `curl`:

```bash
curl -X GET "http://localhost:8000/api/v1/workflows/1" -H "accept: application/json"
```

This will return the details of the workflow with ID 1.

## Contributing

We [welcome contributions](https://github.com/rushirajnenuji/dataone-gse/blob/main/CONTRIBUTING.md) in many forms, including code, graphics, documentation, bug reports, testing, etc. Use the [discussion list](https://github.com/rushirajnenuji/dataone-gse/issues) to discuss these contributions with us.

## License

[Apache License](https://github.com/rushirajnenuji/dataone-gse/blob/main/LICENSE)