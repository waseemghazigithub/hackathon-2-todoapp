# Tasks: Phase I - In-Memory Todo App

**Input**: Design documents from `/specs/001-phase-i-todo/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/ logic.md

**Organization**: Tasks are grouped by foundational setup and user stories to enable incremental delivery and testing.

## Format: `[ID] [P?] [Story] Description`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create source directory `src/` at repository root (Ref: plan.md:46)
- [x] T002 Create initial `src/todo.py` with encoding and basic Python structure (Ref: plan.md:49)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T003 Initialize in-memory storage: global `tasks` list and `next_id` counter in `src/todo.py` (Ref: plan.md:57)
- [x] T004 Implement CLI menu display function `show_menu()` in `src/todo.py` (Ref: plan.md:67, spec.md:62)
- [x] T005 Implement the main application loop and exit flow (Option 6) in `src/todo.py` (Ref: plan.md:68, spec.md:67)

**Checkpoint**: Foundation ready - CLI loop is functional, can proceed to user story implementation.

---

## Phase 3: User Story 1 - Create and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add tasks to the in-memory list and display them.

**Independent Test**: Use Option 1 to add "Task A", then Option 2 to view and verify "Task A" appears with ID 1.

### Implementation for User Story 1

- [x] T006 [US1] Implement `add_task(title)` logic per contract in `src/todo.py` (Ref: contracts/logic.md:10)
- [x] T007 [US1] Implement "Add Task" CLI flow (Option 1) including input capture in `src/todo.py` (Ref: plan.md:69)
- [x] T008 [US1] Implement `get_all_tasks()` logic per contract in `src/todo.py` (Ref: contracts/logic.md:15)
- [x] T009 [US1] Implement "View Tasks" CLI flow (Option 2) with empty list handling in `src/todo.py` (Ref: spec.md:54)

**Checkpoint**: User Story 1 complete. Basic CRUD (Create/Read) is functional.

---

## Phase 4: User Story 2 - Complete and Update Tasks (Priority: P2)

**Goal**: Allow users to modify task descriptions and toggle completion status.

**Independent Test**: Add a task, then use Option 3 to update title and Option 4 to toggle status. Verify changes via Option 2.

### Implementation for User Story 2

- [x] T010 [US2] Implement `update_task(task_id, new_title)` logic in `src/todo.py` (Ref: contracts/logic.md:19)
- [x] T011 [US2] Implement "Update Task" CLI flow (Option 3) with ID validation in `src/todo.py` (Ref: plan.md:71)
- [x] T012 [US2] Implement `toggle_task_status(task_id)` logic in `src/todo.py` (Ref: contracts/logic.md:24)
- [x] T013 [US2] Implement "Mark Complete/Incomplete" CLI flow (Option 4) in `src/todo.py` (Ref: plan.md:61-64)

---

## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: Allow users to remove tasks from the list.

**Independent Test**: Add a task, use Option 5 to delete it, then verify it is gone via Option 2.

### Implementation for User Story 3

- [x] T014 [US3] Implement `delete_task(task_id)` logic in `src/todo.py` (Ref: contracts/logic.md:29)
- [x] T015 [US3] Implement "Delete Task" CLI flow (Option 5) with ID validation in `src/todo.py` (Ref: plan.md:73)

---

## Phase 6: Polish & Robustness

**Purpose**: Input validation and final verification.

- [x] T016 Implement global input validation for non-numeric menu choices and task IDs (`ValueError` handling) (Ref: spec.md:82)
- [x] T017 Final verification of all success criteria (SC-001 to SC-005) (Ref: spec.md:78)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup & Foundational (Phases 1-2)**: MUST be completed first.
- **User Story 1 (Phase 3)**: Depends on Foundational.
- **User Story 2 & 3 (Phases 4-5)**: Depend on User Story 1 (requires list/ID infrastructure).
- **Polish (Phase 6)**: Final step.

### Within Each User Story
- Logic functions MUST be implemented before their corresponding CLI menu flows.
