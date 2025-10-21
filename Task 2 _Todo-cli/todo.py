TASKS_FILE = "Task 2/tasks.txt"

def load_tasks():
    """Load tasks from the file into a list."""
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # File will be created automatically when saving the first task
        pass
    return tasks

def save_tasks(tasks):
    """Save all tasks from the list into the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Task added: '{task}'")
    else:
        print("⚠️ Task cannot be empty!")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed task: '{removed}'")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    """Main menu loop."""
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid option, please try again.")

if __name__ == "__main__":
    main()
