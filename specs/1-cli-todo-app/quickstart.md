# Quickstart Guide: CLI Todo App

## Getting Started

1. Ensure Python 3.8+ is installed on your system
2. Clone or download the todo_console application
3. Navigate to the application directory
4. Run the application using: `python main.py`

## Basic Usage

When the application starts, you'll see a menu with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit

### Adding a Task
1. Select option 1 from the menu
2. Enter the task title when prompted
3. Optionally enter a task description
4. The system will confirm the task has been added with a unique ID

### Viewing Tasks
1. Select option 2 from the menu
2. All tasks will be displayed with their ID, title, description, and completion status

### Updating a Task
1. Select option 3 from the menu
2. Enter the task ID you want to update
3. Optionally enter a new title and/or description
4. The system will confirm the task has been updated

### Deleting a Task
1. Select option 4 from the menu
2. Enter the task ID you want to delete
3. The system will confirm the task has been deleted

### Marking a Task Complete
1. Select option 5 from the menu
2. Enter the task ID you want to mark complete
3. The system will toggle the completion status and confirm the change

### Exiting the Application
1. Select option 6 from the menu
2. The application will close

## Error Handling

- If you enter an invalid task ID, the system will display an error message
- If you enter an invalid menu option, the system will prompt you again
- All errors are handled gracefully without crashing the application