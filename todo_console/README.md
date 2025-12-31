# CLI Todo Application

A simple command-line interface (CLI) application for managing todo tasks.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- In-memory storage (tasks are not persisted between sessions)

## Requirements

- Python 3.8 or higher

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. The application is ready to run (no additional dependencies required)

## Usage

To run the application:

```bash
python main.py
```

The application provides a menu-driven interface:

1. **Add Task** - Create a new task with a title and optional description
2. **View Tasks** - Display all tasks with their status (completed/incomplete)
3. **Update Task** - Modify an existing task's title or description
4. **Delete Task** - Remove a task from your list
5. **Mark Task Complete** - Toggle the completion status of a task
6. **Exit** - Close the application

## Project Structure

```
todo_console/
├── main.py          # Entry point and CLI interface
├── todo.py          # Core logic and data models
├── utils.py         # Utility functions
├── tests/
│   └── test_todo.py # Unit tests
└── README.md        # This file
```

## Testing

To run the unit tests:

```bash
python -m unittest tests.test_todo.py
```

Or run all tests in the tests directory:

```bash
python -m unittest discover tests/
```

## Architecture

The application follows a modular design:

- `main.py`: Handles user interface and input/output
- `todo.py`: Contains the core business logic with `Task` and `TaskManager` classes
- `utils.py`: Contains helper functions
- `tests/`: Contains unit tests for the core functionality

## Data Model

- **Task**: Represents a single todo item with:
  - `id`: Unique integer identifier
  - `title`: Required string title
  - `description`: Optional string description
  - `completed`: Boolean completion status

- **TaskManager**: Manages a collection of tasks in memory with methods for:
  - Adding tasks
  - Viewing tasks
  - Updating tasks
  - Deleting tasks
  - Toggling completion status