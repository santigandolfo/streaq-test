# Streaq Priority Test

This repository serves as a simple test environment to demonstrate how Streaq manages task priorities in a distributed task queue system. The project consists of a FastAPI web application that enqueues tasks with different priority levels (low, mid, high) and a worker that processes these tasks based on their priorities.

## Project Structure

- `web.py`: FastAPI application that exposes the task enqueuing endpoint
- `worker.py`: Worker configuration and task definitions
- `docker-compose.yml`: Docker Compose configuration for running the entire stack
- `Dockerfile`: Container definition for the web and worker services

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Project

1. Build the Docker images:

```bash
docker compose build
```

2. Start all services using Docker Compose:

```bash
docker compose up
```

This will start:
- Web server on port 8000
- Streaq worker (with UI) on port 8001
- Redis instance on port 6379

### Testing Task Priorities

To enqueue a batch of test tasks with different priorities, send a GET request to the `/enqueue-tasks` endpoint:

```bash
curl http://localhost:8000/enqueue-tasks
```

This will enqueue:
- 100 tasks with low priority
- 100 tasks with mid priority
- 100 tasks with high priority

### Monitoring Tasks

You can monitor task execution and priorities through the Streaq UI:

1. Open your browser
2. Navigate to [http://localhost:8001](http://localhost:8001)
3. The UI will show you the task queue, priorities, and execution status
