# Task Manager

A command-line Task Manager application in Python, allowing users to manage their tasks by adding, viewing, marking as complete, and deleting tasks. Task data is saved in a JSON file (`tasks.json`) for persistence.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Future Enhancements](#future-enhancements)

## Features
- **Add Task**: Add a new task by providing a title.
- **View Tasks**: View all tasks with their IDs, titles, and statuses (Completed or Pending).
- **Mark Task as Complete**: Mark a task as completed by providing its ID.
- **Delete Task**: Delete a task by its ID.
- **Persistent Storage**: Tasks are saved to a JSON file (`tasks.json`) so data is retained across sessions.

## How It Works
- Tasks are represented by the `Task` class, with attributes for task ID, title, and completion status.
- The application loads tasks from `tasks.json` at startup and saves any changes to this file.
- Each task can be manipulated via a simple command-line interface.

## Requirements
- Python 3.6 or higher
- `json` module (built-in)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/Task_Manager.git
    cd Task_Manager
    ```

2. **Run the application**:

    ```bash
    python task_manager.py
    ```

## Usage

Once you run the program, a command-line interface will be displayed with the following options:

1. **Add Task**: Prompts you to enter a title, creates a new task with an ID, and saves it to `tasks.json`.
2. **View Tasks**: Displays all tasks in the system with their IDs, titles, and completion status (Pending or Completed).
3. **Delete Task**: Prompts you to enter the ID of the task you want to delete, removes it from the list, and updates `tasks.json`.
4. **Mark Task as Complete**: Prompts you to enter the ID of a task to mark it as completed, updates the task status, and saves it.
5. **Exit**: Exits the program.

### Example Commands
After running the application, you will see a menu like this:

```plaintext
Task Manager CLI
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Exit
