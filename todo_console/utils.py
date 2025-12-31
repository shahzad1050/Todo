"""
CLI Todo Application - Utility Functions

This module contains utility functions for the todo application.
"""


def validate_task_title(title):
    """
    Validate a task title.

    Args:
        title (str): The title to validate

    Returns:
        bool: True if the title is valid, False otherwise
    """
    if not isinstance(title, str):
        return False
    if not title.strip():
        return False
    return True


def format_task_display(task):
    """
    Format a task for display.

    Args:
        task (Task): The task object to format

    Returns:
        str: Formatted string representation of the task
    """
    status = "✓" if task.completed else "○"
    desc = f" - {task.description}" if task.description else ""
    return f"{status} [{task.id}] {task.title}{desc}"


def get_next_id(tasks):
    """
    Get the next available ID based on the current tasks.

    Args:
        tasks (list): List of current Task objects

    Returns:
        int: The next available ID
    """
    if not tasks:
        return 1
    # Find the highest ID and add 1
    max_id = max(task.id for task in tasks) if tasks else 0
    return max_id + 1