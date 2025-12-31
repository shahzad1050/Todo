---
id: 1
title: Update Project Constitution
stage: constitution
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, spec-driven-development, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - none
---

## Prompt

```
prompt /sp.constitution
Project Name: Todo – Spec-Driven Cloud Native AI Application

Global Rules for Claude Code & Spec-Kit Plus:

=====================================================
PHASE I – In-Memory Python CLI Todo App
=====================================================
1. **Spec-Driven Development**
   - Features must be generated strictly from specifications.
   - No manual coding allowed; follow Agentic Dev Stack: Write spec → Generate plan → Break into tasks → Implement via Claude Code.

2. **Feature Rules**
   - Implement all 5 basic features: Add, Delete, Update, View, Mark Complete.
   - Tasks are stored in memory.
   - Task IDs must be unique integers; completion toggles must work reliably.

3. **Code Quality**
   - Follow clean Python coding practices.
   - Modularize code with classes/functions for tasks and utilities.

4. **Error Handling**
   - Handle missing task IDs gracefully.
   - Validate input and provide friendly messages.

5. **Testing**
   - Include basic CLI tests to validate feature correctness.

=====================================================
PHASE II – Full-Stack Web Application
=====================================================
1. **Spec-Driven Development**
   - Transform CLI app to multi-user web app with persistence.
   - Continue following Agentic Dev Stack workflow.

2. **Technology Stack**
   - Frontend: Next.js 16+ (App Router)
   - Backend: Python FastAPI
   - ORM/Database: SQLModel + Neon Serverless PostgreSQL
   - Authentication: Better Auth

3. **Feature Rules**
   - Implement all 5 basic features as web APIs + frontend.
   - RESTful endpoints must follow spec:
     GET /api/{user_id}/tasks
     POST /api/{user_id}/tasks
     GET /api/{user_id}/tasks/{id}
     PUT /api/{user_id}/tasks/{id}
     DELETE /api/{user_id}/tasks/{id}
     PATCH /api/{user_id}/tasks/{id}/complete

4. **Error Handling & Validation**
   - Validate all API inputs.
   - Return meaningful JSON error messages.
   - Ensure database consistency at all times.

5. **Frontend**
   - Build responsive UI.
   - Use Better Auth for login/signup.
   - Display task status and allow updates/deletions.

6. **Testing**
   - Include API and integration tests for backend and frontend.

=====================================================
PHASE III – AI-Powered Todo Chatbot
=====================================================
1. **Spec-Driven Development**
   - Add AI conversational interface to manage todos.
   - Use OpenAI Agents SDK + MCP server.
   - Stateless tools with state persisted in DB.

2. **Database Models**
   - Task, Conversation, Message tables must follow spec.
   - Maintain consistent IDs, timestamps, and relationships.

3. **AI Tools & Behavior**
   - Tools: add_task, list_tasks, update_task, delete_task, complete_task.
   - Agents must select the correct tool based on natural language intent.
   - Always confirm actions with friendly responses.
   - Handle missing tasks or errors gracefully.

4. **Chat API**
   - Endpoint: POST /api/{user_id}/chat
   - Accepts message and optional conversation_id.
   - Returns AI response + tool_calls array.

5. **Security & Auth**
   - Use Better Auth for user verification.
   - Chat sessions must be private per user.

6. **Testing**
   - Validate AI tool calls and conversation state persistence.
   - Include automated tests for chat flows.

=====================================================
ENFORCEMENT (ALL PHASES)
=====================================================
- Claude Code + Spec-Kit Plus **must always follow this constitution**.
- Clean code, spec-driven development, and error handling are mandatory.
- Documentation must be maintained for features, APIs, and AI behavior.
- Iterative reviews and version tracking must be applied in every phase.
```

## Response snapshot

Updated the project constitution file (.specify/memory/constitution.md) to reflect the specific requirements for the Todo – Spec-Driven Cloud Native AI Application. The constitution now includes:

- Core Principles section with 6 principles: Spec-Driven Development, Clean Code & Modularity, Test-First Development, Error Handling & Input Validation, Security & Authentication, and Performance & Observability
- Additional Constraints section with requirements for all 3 phases (CLI app, web application, AI chatbot)
- Development Workflow section outlining the Agentic Dev Stack process
- Governance section with amendment procedures

Also updated template files to align with the new constitution:
- Updated plan-template.md to include constitution check gates
- Updated spec-template.md with constitution-aligned functional requirements
- Updated tasks-template.md with constitution-aligned foundational tasks

The constitution version is now 1.0.0, with ratification and amendment dates set to 2025-12-29.

## Outcome

- ✅ Impact: Project constitution updated with comprehensive requirements for all 3 phases
- 🧪 Tests: No tests required for this configuration change
- 📁 Files: 4 files updated to align with new constitution
- 🔁 Next prompts: Ready to proceed with feature specification and implementation
- 🧠 Reflection: Constitution now provides clear guidance for all development phases

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification following the new constitution