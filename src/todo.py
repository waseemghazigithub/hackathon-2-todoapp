#!/usr/bin/env python3
"""
Phase I - In-Memory Todo App
A simple console-based todo application using only in-memory storage.
"""

import sys

# In-memory storage
tasks = []
next_id = 1

def add_task(title, code):
    """Add a new task to the in-memory list."""
    global next_id
    if not title:
        print("Error: Task title cannot be empty.")
        return None

    task = {
        'id': next_id,
        'title': title,
        'code': code,
        'is_completed': False
    }
    tasks.append(task)
    next_id += 1
    return task

def get_all_tasks():
    """Return the list of all tasks."""
    return tasks

def update_task(task_id, new_title, new_code):
    """Update title and code of an existing task."""
    for t in tasks:
        if t['id'] == task_id:
            t['title'] = new_title
            t['code'] = new_code
            return True
    return False

def toggle_task_status(task_id):
    """Toggle completion status of a task."""
    for t in tasks:
        if t['id'] == task_id:
            t['is_completed'] = not t['is_completed']
            return True
    return False

def delete_task(task_id):
    """Delete a task from the list."""
    global tasks
    for i, t in enumerate(tasks):
        if t['id'] == task_id:
            tasks.pop(i)
            return True
    return False

def show_menu():
    """Display the application menu."""
    print("\n--- TODO APP (Phase I) ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Complete/Incomplete")
    print("5. Delete Task")
    print("6. Exit")
    print("--------------------------")

def main():
    """Main application loop."""
    print("Welcome to the Evolution of Todo App!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            code = input("Enter task code: ").strip()
            task = add_task(title, code)
            if task:
                print(f"Task added successfully! ID: {task['id']}")
        elif choice == '2':
            current_tasks = get_all_tasks()
            if not current_tasks:
                print("Your todo list is currently empty.")
            else:
                print("\n--- Current Tasks ---")
                for t in current_tasks:
                    status = "[Done]" if t['is_completed'] else "[ ]"
                    print(f"{t['id']}. {status} {t['title']} ({t['code']})")
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new title: ").strip()
                new_code = input("Enter new code: ").strip()
                if update_task(task_id, new_title, new_code):
                    print("Task updated successfully!")
                else:
                    print(f"Error: Task ID {task_id} not found.")
            except ValueError:
                print("Error: Please enter a numeric ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to toggle: "))
                if toggle_task_status(task_id):
                    print("Task status toggled successfully!")
                else:
                    print(f"Error: Task ID {task_id} not found.")
            except ValueError:
                print("Error: Please enter a numeric ID.")
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to delete: "))
                if delete_task(task_id):
                    print("Task deleted successfully!")
                else:
                    print(f"Error: Task ID {task_id} not found.")
            except ValueError:
                print("Error: Please enter a numeric ID.")
        elif choice == '6':
            print("Exiting application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
