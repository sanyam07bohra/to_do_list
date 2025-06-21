import os
import json

FILENAME = "tasks.json"

# Load existing tasks if file exists
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def show_tasks():
    if not tasks:
        print("\n✅ No tasks for now. Enjoy your free time!\n")
        return
    print("\n📝 Your To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")
    print()

def add_task():
    task = input("Enter task description: ")
    tasks.append({"task": task, "done": False})
    save_tasks()
    print("Task added ✅")

def mark_done():
    show_tasks()
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks()
            print("Task marked as done ✅")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks()
            print(f"Deleted task: {removed['task']} 🗑️")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("you are a sexy boiiii 👋")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
