---
id: 1
title: Create CLI Todo Spec
stage: spec
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: 1-cli-todo-app
branch: 1-cli-todo-app
user: user
command: /sp.specify
labels: [specification, todo-app, cli, python]
links:
  spec: specs/1-cli-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-cli-todo-app/spec.md
 - specs/1-cli-todo-app/checklists/requirements.md
tests:
 - none
---

## Prompt

```
prompt /sp.specify
Phase: I – In-Memory Python CLI Todo App
Reference Constitution: /sp.constitution

Project Objective:
Build a command-line Todo application that allows a single user to manage tasks in memory. The app must implement all basic features: Add, Delete, Update, View, and Mark Complete. Follow the Agentic Dev Stack workflow and do not write manual code.

Feature Specifications:

1. Add Task
   - Input: Task title (required), Task description (optional)
   - Output: Task object with unique ID, title, description, completed=False
   - Behavior: Adds task to in-memory task list
   - Response: Friendly confirmation message

2. Delete Task
   - Input: Task ID
   - Output: Task object with status='deleted'
   - Behavior: Remove task from in-memory list
   - Response: Friendly confirmation message or error if ID not found

3. Update Task
   - Input: Task ID, title (optional), description (optional)
   - Output: Task object with updated fields, status='updated'
   - Behavior: Modify task in memory
   - Response: Friendly confirmation message or error if ID not found

4. View Task List
   - Input: None
   - Output: List of all tasks with fields: id, title, description, completed
   - Behavior: Display all tasks in a readable format

5. Mark as Complete
   - Input: Task ID
   - Output: Task object with completed toggled
   - Behavior: Toggle completion status
   - Response: Friendly confirmation message or error if ID not found

Requirements:
- Python project structure: modular code (e.g., main.py, todo.py)
- Tasks stored in-memory (list or dictionary)
- Unique task IDs
- Error handling for invalid IDs or inputs
- Basic CLI interface using print/input
- Include minimal unit tests to validate fn for testing all features
- Include comments only for clarity if necessary
- Include simple test cases for each feature

End of Spec
```

## Response snapshot

Created a comprehensive feature specification for the CLI Todo application. The specification includes:

- 5 user stories covering all required functionality (Add, View, Mark Complete, Update, Delete tasks)
- Detailed acceptance scenarios for each user story
- 12 functional requirements based on the feature description
- Key entity definition for the Task object
- Success criteria with measurable outcomes
- Edge cases identified

The specification follows the constitution requirements for spec-driven development and is ready for the planning phase. A quality checklist was also created and validated to ensure the specification meets all requirements.

## Outcome

- ✅ Impact: Complete feature specification created for CLI Todo app
- 🧪 Tests: No tests required for specification creation
- 📁 Files: 2 files created (spec.md and requirements checklist)
- 🔁 Next prompts: Ready for /sp.plan to create implementation plan
- 🧠 Reflection: Specification follows all constitution requirements and is ready for planning

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to planning phase with /sp.plan