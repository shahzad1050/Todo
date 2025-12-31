<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- Added sections: Core Principles (6), Additional Constraints (3 phases), Development Workflow
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ⚠ pending
- Follow-up TODOs: None
-->
# Todo – Spec-Driven Cloud Native AI Application Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
Features must be generated strictly from specifications; No manual coding allowed; Follow Agentic Dev Stack: Write spec → Generate plan → Break into tasks → Implement via Claude Code; All changes must follow the spec-driven workflow across all phases.

### II. Clean Code & Modularity
Follow clean Python coding practices; Modularize code with classes/functions for tasks and utilities; Maintain separation of concerns; Ensure code is readable, testable, and maintainable across all phases of development.

### III. Test-First Development (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced; Include basic CLI tests, API tests, and integration tests; Validate feature correctness at every phase.

### IV. Error Handling & Input Validation
Validate all API inputs; Handle missing task IDs gracefully; Return meaningful error messages; Ensure database consistency at all times; Provide friendly messages to users; Follow consistent error taxonomy across all phases.

### V. Security & Authentication
Use Better Auth for user verification; Implement proper AuthN/AuthZ; Secure all API endpoints; Ensure chat sessions are private per user; Follow security best practices for data handling and secrets management.

### VI. Performance & Observability
Maintain responsive UI; Ensure p95 latency requirements; Implement structured logging; Provide metrics and traces; Monitor API performance; Follow observability best practices across all phases.

## Additional Constraints

### Phase I – In-Memory Python CLI Todo App
- Implement all 5 basic features: Add, Delete, Update, View, Mark Complete
- Tasks are stored in memory
- Task IDs must be unique integers; completion toggles must work reliably
- Handle missing task IDs gracefully; validate input and provide friendly messages
- Include basic CLI tests to validate feature correctness

### Phase II – Full-Stack Web Application
- Technology Stack: Frontend: Next.js 16+ (App Router), Backend: Python FastAPI, ORM/Database: SQLModel + Neon Serverless PostgreSQL, Authentication: Better Auth
- Implement all 5 basic features as web APIs + frontend with RESTful endpoints: GET /api/{user_id}/tasks, POST /api/{user_id}/tasks, GET /api/{user_id}/tasks/{id}, PUT /api/{user_id}/tasks/{id}, DELETE /api/{user_id}/tasks/{id}, PATCH /api/{user_id}/tasks/{id}/complete
- Build responsive UI; use Better Auth for login/signup; display task status and allow updates/deletions
- Include API and integration tests for backend and frontend

### Phase III – AI-Powered Todo Chatbot
- Use OpenAI Agents SDK + MCP server; maintain stateless tools with state persisted in DB
- Database Models: Task, Conversation, Message tables must follow spec with consistent IDs, timestamps, and relationships
- AI Tools: add_task, list_tasks, update_task, delete_task, complete_task; Agents must select correct tool based on natural language intent; Always confirm actions with friendly responses; Handle missing tasks or errors gracefully
- Chat API endpoint: POST /api/{user_id}/chat accepting message and optional conversation_id, returning AI response + tool_calls array

## Development Workflow

- Follow Agentic Dev Stack: Write spec → Generate plan → Break into tasks → Implement via Claude Code
- Maintain documentation for features, APIs, and AI behavior
- Apply iterative reviews and version tracking in every phase
- Use clean code, spec-driven development, and error handling as mandatory requirements
- Ensure all outputs strictly follow user intent with small, testable changes

## Governance

Constitution supersedes all other practices; All development must strictly follow this constitution across all phases; Amendments require documentation, approval, and migration plan; All PRs/reviews must verify compliance; Complexity must be justified; Use CLAUDE.md for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29
