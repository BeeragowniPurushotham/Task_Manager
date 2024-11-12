# Import necessary libraries
import json

# Define the Task class
class Task:
    """
    Class to represent a task with attributes:
    - id (int): Task ID
    - title (str): Task title
    - completed (bool): Status indicating if the task is completed
    """
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        """Convert task object to dictionary for JSON serialization."""
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        """Create a Task object from a dictionary."""
        return Task(data["id"], data["title"], data["completed"])


# Initialize the task list with empty because whatever data you enter That is storing in this tasks
tasks = []

# Load tasks from a file
def load_tasks():
    """Load tasks from tasks.json file if it exists."""
    global tasks
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            tasks = [Task.from_dict(task_data) for task_data in data]
    except FileNotFoundError:
        # No file found, start with an empty task list
        tasks = []
    except json.JSONDecodeError:
        print("Error: Failed to decode tasks from tasks.json.")


# Save tasks to a file
def save_tasks():
    """Save current tasks list to tasks.json file."""
    with open("tasks.json", "w") as file:
        json.dump([task.to_dict() for task in tasks], file)


# Add a new task
def add_task(title):
    """
    Add a new task to the task list.
    
    Parameters:
    - title (str): Title of the new task
    """
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)
    save_tasks()
    print(f"Task '{title}' added with ID {task_id}.")


# View all tasks
def view_tasks():
    """Display all tasks with their IDs, titles, and completion status."""
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"ID: {task.id}, Title: '{task.title}', Status: {status}")


# Delete a task by ID
def delete_task(task_id):
    """
    Delete a task by its ID.
    
    Parameters:
    - task_id (int): The ID of the task to delete
    """
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    save_tasks()
    print(f"Task with ID {task_id} deleted.")


# Mark a task as complete by ID
def mark_task_as_complete(task_id):
    """
    Mark a task as completed by its ID.
    Parameters:
    - task_id (int): The ID of the task to mark as complete
    """
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            save_tasks()
            print(f"Task with ID {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")


# Main command-line interface loop
def main():
    """Main function to handle the CLI interface for task management."""
    load_tasks()
    while True:
        # Display menu options
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                mark_task_as_complete(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main loop
if __name__ == "__main__":
    main()
