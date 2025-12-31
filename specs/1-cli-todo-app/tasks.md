---
description: "Task list for CLI Todo App implementation"
---

# Tasks: CLI Todo App

**Input**: Design documents from `/specs/1-cli-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in todo_console/
- [X] T002 Initialize Python project with basic dependencies
- [X] T003 [P] Create main.py entry point file in todo_console/main.py
- [X] T004 [P] Create todo.py file for core logic in todo_console/todo.py
- [X] T005 [P] Create utils.py file for helper functions in todo_console/utils.py
- [X] T006 [P] Create tests directory and test_todo.py file in todo_console/tests/test_todo.py
- [X] T007 Create README.md with project description in todo_console/README.md

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T008 Setup Task class with fields: id, title, description, completed in todo_console/todo.py
- [X] T009 [P] Implement TaskList class for in-memory storage in todo_console/todo.py
- [X] T010 [P] Implement ID generation system (auto-increment) in todo_console/todo.py
- [X] T011 Create basic validation for Task fields in todo_console/todo.py
- [X] T012 Setup basic CLI menu structure in todo_console/main.py
- [X] T013 Configure error handling infrastructure in todo_console/todo.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks to their todo list with required title and optional description

**Independent Test**: Can be fully tested by adding a task with a title and optional description, and verifying it appears in the task list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T014 [P] [US1] Unit test for add_task() function in todo_console/tests/test_todo.py
- [X] T015 [P] [US1] Test adding task with title only in todo_console/tests/test_todo.py
- [X] T016 [P] [US1] Test adding task with title and description in todo_console/tests/test_todo.py

### Implementation for User Story 1

- [X] T017 [P] [US1] Implement add_task() function in todo_console/todo.py
- [X] T018 [US1] Add CLI menu option for adding tasks in todo_console/main.py
- [X] T019 [US1] Implement user input handling for add task in todo_console/main.py
- [X] T020 [US1] Add validation for required title field in todo_console/todo.py
- [X] T021 [US1] Add friendly confirmation message for task creation in todo_console/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Enable users to view all their tasks with ID, title, description, and completion status

**Independent Test**: Can be fully tested by adding tasks and then viewing the complete task list with all fields displayed.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T022 [P] [US2] Unit test for view_tasks() function in todo_console/tests/test_todo.py
- [X] T023 [P] [US2] Test viewing empty task list in todo_console/tests/test_todo.py
- [X] T024 [P] [US2] Test viewing multiple tasks with different statuses in todo_console/tests/test_todo.py

### Implementation for User Story 2

- [X] T025 [P] [US2] Implement view_tasks() function in todo_console/todo.py
- [X] T026 [US2] Add CLI menu option for viewing tasks in todo_console/main.py
- [X] T027 [US2] Implement formatted display of tasks in todo_console/main.py
- [X] T028 [US2] Ensure all required fields (ID, title, description, completion status) are displayed in todo_console/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Mark Task Complete (Priority: P2)

**Goal**: Enable users to mark tasks as complete to track their progress

**Independent Test**: Can be fully tested by marking a task as complete and verifying its status updates.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T029 [P] [US3] Unit test for toggle_task_completion() function in todo_console/tests/test_todo.py
- [X] T030 [P] [US3] Test toggling completion status from False to True in todo_console/tests/test_todo.py
- [X] T031 [P] [US3] Test toggling completion status from True to False in todo_console/tests/test_todo.py

### Implementation for User Story 3

- [X] T032 [P] [US3] Implement toggle_task_completion() function in todo_console/todo.py
- [X] T033 [US3] Add CLI menu option for marking tasks complete in todo_console/main.py
- [X] T034 [US3] Implement user input handling for task ID in todo_console/main.py
- [X] T035 [US3] Add error handling for invalid task IDs in todo_console/todo.py
- [X] T036 [US3] Add friendly confirmation message for status change in todo_console/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---
## Phase 6: User Story 4 - Update Task (Priority: P3)

**Goal**: Enable users to update task details to maintain accurate task information

**Independent Test**: Can be fully tested by updating a task's title or description and verifying the changes persist.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T037 [P] [US4] Unit test for update_task() function in todo_console/tests/test_todo.py
- [X] T038 [P] [US4] Test updating task title only in todo_console/tests/test_todo.py
- [X] T039 [P] [US4] Test updating task description only in todo_console/tests/test_todo.py

### Implementation for User Story 4

- [X] T040 [P] [US4] Implement update_task() function in todo_console/todo.py
- [X] T041 [US4] Add CLI menu option for updating tasks in todo_console/main.py
- [X] T042 [US4] Implement user input handling for task updates in todo_console/main.py
- [X] T043 [US4] Add validation for updated fields in todo_console/todo.py
- [X] T044 [US4] Add friendly confirmation message for updates in todo_console/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---
## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Enable users to delete tasks to remove items they no longer need to track

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the task list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T045 [P] [US5] Unit test for delete_task() function in todo_console/tests/test_todo.py
- [X] T046 [P] [US5] Test deleting existing task in todo_console/tests/test_todo.py
- [X] T047 [P] [US5] Test error handling for invalid task ID in todo_console/tests/test_todo.py

### Implementation for User Story 5

- [X] T048 [P] [US5] Implement delete_task() function in todo_console/todo.py
- [X] T049 [US5] Add CLI menu option for deleting tasks in todo_console/main.py
- [X] T050 [US5] Implement user input handling for task deletion in todo_console/main.py
- [X] T051 [US5] Add confirmation prompt for task deletion in todo_console/main.py
- [X] T052 [US5] Add friendly confirmation message for deletion in todo_console/main.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T053 [P] Complete CLI menu with all options in todo_console/main.py
- [X] T054 [P] Implement comprehensive error handling for all operations in todo_console/todo.py
- [X] T055 [P] Add user-friendly prompts and responses across all features in todo_console/main.py
- [X] T056 [P] Implement validation for all user inputs in todo_console/main.py
- [X] T057 [P] Add graceful exit functionality in todo_console/main.py
- [X] T058 [P] Complete unit tests for all functions in todo_console/tests/test_todo.py
- [X] T059 [P] Run integration test to verify all features work together in todo_console/
- [X] T060 [P] Documentation updates in todo_console/README.md

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for add_task() function in todo_console/tests/test_todo.py"
Task: "Test adding task with title only in todo_console/tests/test_todo.py"
Task: "Test adding task with title and description in todo_console/tests/test_todo.py"

# Launch all implementation for User Story 1 together:
Task: "Implement add_task() function in todo_console/todo.py"
Task: "Add CLI menu option for adding tasks in todo_console/main.py"
```

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence