---
id: 006
title: Add code field to task entity
stage: green
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-phase-i-todo
branch: main
user: current
command: none
labels: [feature, data-model, logic, ui]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-phase-i-todo/data-model.md
 - specs/001-phase-i-todo/spec.md
 - specs/001-phase-i-todo/contracts/logic.md
 - specs/001-phase-i-todo/tasks.md
 - src/todo.py
tests:
 - manual
---

## Prompt

add another field title code in app

## Response snapshot

Added a new `code` field to the task entity across the application, including:
- Updated documentation (data-model.md, spec.md, tasks.md, contracts/logic.md)
- Updated logic and CLI in `src/todo.py` to support task codes during creation, display, and update.

## Outcome

- ✅ Impact: Task entity now supports a 'code' field for better identification.
- 🧪 Tests: Manual verification of add, view, and update flows.
- 📁 Files: Updated 5 files.
- 🔁 Next prompts: none
- 🧠 Reflection: Followed SDD patterns consistently.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
