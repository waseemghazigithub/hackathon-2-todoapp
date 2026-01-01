# Data Model: Phase I - In-Memory Todo App

## Entities

### Task
Represents a single item in the todo list.

| Field | Type | Description | Validation/Constraints |
|-------|------|-------------|-------------------------|
| `id` | Integer | Unique identifier | Auto-incrementing, Read-only (system set) |
| `title` | String | Description of task | MUST not be empty |
| `code` | String | Unique reference code | Internal identifier (system set or user input) |
| `is_completed` | Boolean | Completion status | Defaults to `False` |

## State Transitions
1. `Add`: Create new task with `is_completed=False` and a `code`.
2. `Update`: Change the `title` or `code` of an existing task.
3. `Complete/Incomplete`: Toggle the `is_completed` boolean.
4. `Delete`: Remove the task object from the in-memory list.
