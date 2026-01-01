# Research: Phase I - In-Memory Todo App

## Decision: Python CLI with Procedural/Functional Split
The application will be a single Python script that separates the CLI loop (UI) from the task management logic (Data).

## Rationale
Given the strictly scoped "Phase I" constraints (in-memory, no persistence, console-only), a lightweight Python script is the most efficient approach. Separation of concerns between UI and Data ensures that the core logic is testable and maintainable for future phases.

## Alternatives Considered
- **Object-Oriented Approach**: A `TaskManager` class could be used. While robust, for a single-user in-memory app, a simplified module with functions and a global list is sufficient and avoids over-engineering in Phase I.
- **Third-Party Libraries (e.g., Click or Typer)**: Rejected because the constitution/spec mandates "no external libraries" for core logic and Phase I should be minimal. Standard library `input()` and `print()` are sufficient.

## Task Identification Strategy
- **Decision**: Global auto-incrementing integer.
- **Rationale**: Simplest unique identifier for an in-memory session. Fits the `FR-003` requirement.

## Data Structure
- **Decision**: List of Dictionaries. mẫu: `[{'id': 1, 'title': '...', 'is_completed': False}]`.
- **Rationale**: Provides O(n) lookup which is acceptable for a console app with a small task list, and maps easily to JSON in future phases.

## Error Handling
- **Decision**: `try-except` blocks for numeric input and explicit checks for ID existence.
- **Rationale**: Prevents crashes on invalid user input (`SC-003`) and provides user-friendly error messages as required by the spec.
