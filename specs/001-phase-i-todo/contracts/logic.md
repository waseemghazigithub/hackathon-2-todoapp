# Internal Logic Contracts: Phase I Todo

Since this is a single Python script with no external API, "contracts" here define the function signatures for the internal data handling layer.

## Task Operations

### `add_task(title: str, code: str) -> dict`
- **Purpose**: Creates and adds a task to the global list.
- **Input**: `title` (non-empty string), `code` (string).
- **Output**: The created task dictionary.

### `get_all_tasks() -> list[dict]`
- **Purpose**: Returns the current list of tasks.
- **Output**: List of all task dictionaries.

### `update_task(task_id: int, new_title: str, new_code: str) -> bool`
- **Purpose**: Updates the title and code of a specific task.
- **Output**: `True` if found and updated, `False` otherwise.

### `toggle_task_status(task_id: int) -> bool`
- **Purpose**: Toggles `is_completed` for a specific task.
- **Output**: `True` if found and toggled, `False` otherwise.

### `delete_task(task_id: int) -> bool`
- **Purpose**: Removes a task from the list.
- **Output**: `True` if found and deleted, `False` otherwise.
