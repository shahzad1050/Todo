# API Contracts: CLI Todo App

## Task Operations

### Add Task
- **Function**: `add_task(title: str, description: str = None) -> dict`
- **Input**:
  - title (required): string, non-empty
  - description (optional): string
- **Output**:
  - Success: `{"id": int, "title": str, "description": str, "completed": bool, "status": "created"}`
  - Error: `{"error": str, "status": "error"}`
- **Behavior**: Creates a new task with unique ID and returns the task object

### View Tasks
- **Function**: `view_tasks() -> list`
- **Input**: None
- **Output**: List of task objects with id, title, description, and completed status
- **Behavior**: Returns all tasks in the in-memory storage

### Get Task by ID
- **Function**: `get_task(task_id: int) -> dict`
- **Input**: task_id (required): integer
- **Output**:
  - Success: `{"id": int, "title": str, "description": str, "completed": bool}`
  - Error: `{"error": str, "status": "error"}`
- **Behavior**: Returns a specific task by ID or error if not found

### Update Task
- **Function**: `update_task(task_id: int, title: str = None, description: str = None) -> dict`
- **Input**:
  - task_id (required): integer
  - title (optional): string
  - description (optional): string
- **Output**:
  - Success: `{"id": int, "title": str, "description": str, "completed": bool, "status": "updated"}`
  - Error: `{"error": str, "status": "error"}`
- **Behavior**: Updates specified fields of a task and returns updated task object

### Delete Task
- **Function**: `delete_task(task_id: int) -> dict`
- **Input**: task_id (required): integer
- **Output**:
  - Success: `{"id": int, "status": "deleted"}`
  - Error: `{"error": str, "status": "error"}`
- **Behavior**: Removes task from storage and returns confirmation

### Toggle Task Completion
- **Function**: `toggle_task_completion(task_id: int) -> dict`
- **Input**: task_id (required): integer
- **Output**:
  - Success: `{"id": int, "completed": bool, "status": "updated"}`
  - Error: `{"error": str, "status": "error"}`
- **Behavior**: Toggles the completed status of a task and returns updated status