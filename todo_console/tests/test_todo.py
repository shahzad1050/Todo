"""
Unit tests for the CLI Todo Application.

This module contains unit tests for the core functionality of the todo application.
"""
import unittest
from todo import Task, TaskManager


class TestTask(unittest.TestCase):
    """Test cases for the Task class."""

    def test_create_task_valid(self):
        """Test creating a valid task."""
        task = Task(1, "Test task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertIsNone(task.description)
        self.assertFalse(task.completed)

    def test_create_task_with_description(self):
        """Test creating a task with description."""
        task = Task(1, "Test task", "Test description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)

    def test_create_task_completed(self):
        """Test creating a completed task."""
        task = Task(1, "Test task", completed=True)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertTrue(task.completed)

    def test_create_task_invalid_id(self):
        """Test creating a task with invalid ID."""
        with self.assertRaises(ValueError):
            Task(0, "Test task")

        with self.assertRaises(ValueError):
            Task(-1, "Test task")

        with self.assertRaises(ValueError):
            Task("invalid", "Test task")

    def test_create_task_invalid_title(self):
        """Test creating a task with invalid title."""
        with self.assertRaises(ValueError):
            Task(1, "")

        with self.assertRaises(ValueError):
            Task(1, "   ")

        with self.assertRaises(ValueError):
            Task(1, None)

    def test_task_repr(self):
        """Test string representation of a task."""
        task = Task(1, "Test task", "Test description")
        repr_str = repr(task)
        self.assertIn("Task", repr_str)
        self.assertIn("id=1", repr_str)
        self.assertIn("title='Test task'", repr_str)

    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(1, "Test task", "Test description", completed=True)
        task_dict = task.to_dict()
        self.assertEqual(task_dict['id'], 1)
        self.assertEqual(task_dict['title'], "Test task")
        self.assertEqual(task_dict['description'], "Test description")
        self.assertTrue(task_dict['completed'])


class TestTaskManager(unittest.TestCase):
    """Test cases for the TaskManager class."""

    def setUp(self):
        """Set up a fresh TaskManager for each test."""
        self.manager = TaskManager()

    def test_initial_state(self):
        """Test initial state of TaskManager."""
        self.assertEqual(len(self.manager.tasks), 0)
        self.assertEqual(self.manager.next_id, 1)

    def test_add_task(self):
        """Test adding a task."""
        task = self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertFalse(task.completed)

    def test_add_task_with_description(self):
        """Test adding a task with description."""
        task = self.manager.add_task("Test task", "Test description")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")

    def test_add_task_invalid_title(self):
        """Test adding a task with invalid title."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")

        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_view_tasks_empty(self):
        """Test viewing tasks when the list is empty."""
        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 0)

    def test_view_tasks_with_tasks(self):
        """Test viewing tasks when the list has tasks."""
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")

        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[1].id, 2)

    def test_get_task_found(self):
        """Test getting an existing task."""
        added_task = self.manager.add_task("Test task")
        retrieved_task = self.manager.get_task(1)

        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, added_task.id)
        self.assertEqual(retrieved_task.title, added_task.title)

    def test_get_task_not_found(self):
        """Test getting a non-existing task."""
        result = self.manager.get_task(999)
        self.assertIsNone(result)

    def test_update_task_title(self):
        """Test updating a task's title."""
        task = self.manager.add_task("Original task")

        updated_task = self.manager.update_task(1, "Updated task")
        self.assertEqual(updated_task.title, "Updated task")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_update_task_description(self):
        """Test updating a task's description."""
        task = self.manager.add_task("Test task", "Original description")

        updated_task = self.manager.update_task(1, description="Updated description")
        self.assertEqual(updated_task.description, "Updated description")

    def test_update_task_both(self):
        """Test updating both title and description."""
        task = self.manager.add_task("Original task", "Original description")

        updated_task = self.manager.update_task(1, "Updated task", "Updated description")
        self.assertEqual(updated_task.title, "Updated task")
        self.assertEqual(updated_task.description, "Updated description")

    def test_update_task_invalid_id(self):
        """Test updating a non-existing task."""
        with self.assertRaises(ValueError):
            self.manager.update_task(999, "New title")

    def test_update_task_invalid_title(self):
        """Test updating a task with invalid title."""
        self.manager.add_task("Test task")

        with self.assertRaises(ValueError):
            self.manager.update_task(1, "")

    def test_delete_task(self):
        """Test deleting an existing task."""
        task = self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)

        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_delete_task_invalid_id(self):
        """Test deleting a non-existing task."""
        with self.assertRaises(ValueError):
            self.manager.delete_task(999)

    def test_toggle_task_completion(self):
        """Test toggling task completion status."""
        task = self.manager.add_task("Test task")
        self.assertFalse(task.completed)

        # Toggle to completed
        toggled_task = self.manager.toggle_task_completion(1)
        self.assertTrue(toggled_task.completed)

        # Toggle back to incomplete
        toggled_task = self.manager.toggle_task_completion(1)
        self.assertFalse(toggled_task.completed)

    def test_toggle_task_completion_invalid_id(self):
        """Test toggling completion for non-existing task."""
        with self.assertRaises(ValueError):
            self.manager.toggle_task_completion(999)


class TestTaskManagerIntegration(unittest.TestCase):
    """Integration tests for the TaskManager."""

    def setUp(self):
        """Set up a fresh TaskManager for each test."""
        self.manager = TaskManager()

    def test_full_workflow(self):
        """Test a full workflow of operations."""
        # Add multiple tasks
        task1 = self.manager.add_task("Task 1", "First task")
        task2 = self.manager.add_task("Task 2", "Second task")
        task3 = self.manager.add_task("Task 3")

        # Verify tasks were added
        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")
        self.assertEqual(tasks[2].title, "Task 3")

        # Update a task
        updated_task = self.manager.update_task(2, "Updated Task 2", "Updated description")
        self.assertEqual(updated_task.title, "Updated Task 2")
        self.assertEqual(updated_task.description, "Updated description")

        # Toggle completion
        completed_task = self.manager.toggle_task_completion(1)
        self.assertTrue(completed_task.completed)

        # Delete a task
        self.manager.delete_task(3)
        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 2)

        # Verify remaining tasks
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[1].id, 2)


if __name__ == '__main__':
    unittest.main()