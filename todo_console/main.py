#!/usr/bin/env python3
"""
CLI Todo Application - Main Entry Point

This is the main entry point for the CLI Todo application.
It provides a menu-driven interface for managing tasks.
"""

from todo_console.todo import TaskManager


def main():
    """Main function to run the CLI Todo application."""
    print("Welcome to the CLI Todo Application!")
    task_manager = TaskManager()

    while True:
        print("\n--- Todo Application Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_task_ui(task_manager)
        elif choice == "2":
            view_tasks_ui(task_manager)
        elif choice == "3":
            update_task_ui(task_manager)
        elif choice == "4":
            delete_task_ui(task_manager)
        elif choice == "5":
            mark_task_complete_ui(task_manager)
        elif choice == "6":
            print("Thank you for using the CLI Todo Application!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")


def add_task_ui(task_manager):
    """UI for adding a task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title is required!")
        return

    description = input("Enter task description (optional): ").strip()
    if not description:
        description = None

    try:
        task = task_manager.add_task(title, description)
        print(f"Task added successfully! ID: {task.id}, Title: {task.title}")
    except Exception as e:
        print(f"Error adding task: {e}")


def view_tasks_ui(task_manager):
    """UI for viewing all tasks."""
    tasks = task_manager.view_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "✓" if task.completed else "○"
        desc = f" - {task.description}" if task.description else ""
        print(f"{status} [{task.id}] {task.title}{desc}")


def update_task_ui(task_manager):
    """UI for updating a task."""
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return

    # Check if task exists
    tasks = task_manager.view_tasks()
    task_exists = any(task.id == task_id for task in tasks)
    if not task_exists:
        print(f"Task with ID {task_id} not found.")
        return

    new_title = input("Enter new title (or press Enter to skip): ").strip()
    new_description = input("Enter new description (or press Enter to skip): ").strip()

    # Use None if empty string was entered
    if not new_title:
        new_title = None
    if not new_description:
        new_description = None

    try:
        updated_task = task_manager.update_task(task_id, new_title, new_description)
        print(f"Task updated successfully! ID: {updated_task.id}, Title: {updated_task.title}")
    except Exception as e:
        print(f"Error updating task: {e}")


def delete_task_ui(task_manager):
    """UI for deleting a task."""
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return

    # Check if task exists
    tasks = task_manager.view_tasks()
    task_exists = any(task.id == task_id for task in tasks)
    if not task_exists:
        print(f"Task with ID {task_id} not found.")
        return

    confirm = input(f"Are you sure you want to delete task {task_id}? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        try:
            task_manager.delete_task(task_id)
            print(f"Task {task_id} deleted successfully!")
        except Exception as e:
            print(f"Error deleting task: {e}")
    else:
        print("Deletion cancelled.")


def mark_task_complete_ui(task_manager):
    """UI for marking a task as complete."""
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return

    # Check if task exists
    tasks = task_manager.view_tasks()
    task_exists = any(task.id == task_id for task in tasks)
    if not task_exists:
        print(f"Task with ID {task_id} not found.")
        return

    try:
        updated_task = task_manager.toggle_task_completion(task_id)
        status = "completed" if updated_task.completed else "incomplete"
        print(f"Task {task_id} marked as {status}!")
    except Exception as e:
        print(f"Error updating task: {e}")


if __name__ == "__main__":
    main()