# Data Model: CLI Todo App

## Task Entity

### Attributes
- **id** (int): Unique identifier for the task, auto-incremented
- **title** (str): Required string representing the task
- **description** (str): Optional string with additional details
- **completed** (bool): Boolean indicating completion status, defaults to False

### Validation Rules
- ID must be unique across all tasks
- Title must be a non-empty string
- Description can be empty or null
- Completed must be a boolean value

### State Transitions
- New task: completed=False (default)
- Marked complete: completed=False → completed=True
- Marked incomplete: completed=True → completed=False

## TaskList Container

### Attributes
- **tasks** (list): List of Task objects stored in memory
- **next_id** (int): Counter for generating unique IDs, starts at 1

### Operations
- Add task: inserts new Task object to the list
- Remove task: removes Task object by ID
- Update task: modifies Task object by ID
- Toggle completion: changes completed status by ID
- Get all tasks: returns list of all Task objects
- Get task by ID: returns specific Task object or None if not found