# Implementation Plan: Phase I - In-Memory Todo App

**Branch**: `001-phase-i-todo` | **Date**: 2026-01-01 | **Spec**: [specs/001-phase-i-todo/spec.md](spec.md)
**Input**: Feature specification for a Phase I in-memory Python console application.

## Summary
Implement a standalone Python script to manage a simple todo list in-memory. The application follows a procedural design with clear separation between task management arithmetic and the console-based user interface loop.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: None (Standard Library only)
**Storage**: In-memory (Python List of Dictionaries)
**Testing**: Manual CLI verification & Logic-level validation
**Target Platform**: CLI/Terminal
**Project Type**: Single project (DEFAULT)
**Performance Goals**: Sub-10ms logic execution
**Constraints**: No persistence, no databases, single-user session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] SDD Flow: Spec -> Plan -> Tasks -> Implement
- [x] Agent Rules: Architect role followed; no feature invention
- [x] Phase Governance: No Leakage (No persistence, no web)
- [x] Technology Constraints: Python only (No FastAPI/SQLModel used in Phase I)
- [x] Quality Principles: Clean separation between CLI loop and list logic

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-i-todo/
├── plan.md              # This file
├── research.md          # Data structures and ID strategy
├── data-model.md        # Task entity and transitions
├── quickstart.md        # Execution guide
├── contracts/
│   └── logic.md         # Internal module signatures
└── tasks.md             # (Next step: sp.tasks)
```

### Source Code (repository root)

```text
src/
└── todo.py              # Single executable program
```

**Structure Decision**: Option 1: Single project (DEFAULT). A single file `src/todo.py` meets Phase I requirements.

## Detailed Plan

### 1. Application Initialization
- Create `tasks` list and `next_id` counter at module scope.

### 2. Logic Layer Implementation
- `add_task(title)`: Create dict, assign ID, increment `next_id`, append to list.
- `update_task(task_id, new_title)`: Iterate/find task by ID, update title.
- `toggle_task(task_id)`: Find by ID, flip `is_completed` boolean.
- `delete_task(task_id)`: Filter list or remove item by ID.
- `get_tasks()`: Return the current list.

### 3. CLI Loop Implementation
- Display ASCII header.
- Continuous loop showing options 1-6.
- Capture input with `input().strip()`.
- Numeric validation for ID gathering (`try...except`).
- Clear feedback messages (Success/Error) after every operation.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None      | N/A        | N/A                                 |
