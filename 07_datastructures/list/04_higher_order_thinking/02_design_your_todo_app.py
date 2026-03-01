# Todo App – Powered by a List
# One list (tasks = []) drives the whole app:
#   Add:    tasks.append(text)
#   View:   enumerate(tasks, start=1)
#   Done:   tasks[index] = "DONE: " + task
#   Remove: tasks.pop(index)
#   Menu:   while True + if-elif + break

tasks = []

def show_menu():
    print()
    print("--- MENU ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Remove a task")
    print("5. Exit")
    print()

def add_task():
    text = input("New task: ").strip()
    if text:
        tasks.append(text)
        print("Added. Total tasks:", len(tasks))
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print()
    for i, task in enumerate(tasks, start=1):
        print("  " + str(i) + ". " + task)
    print("Total:", len(tasks))

def get_task_index(action):
    view_tasks()
    raw = input("Enter task number to " + action + ": ").strip()
    if not raw.isdigit():
        print("Please enter a number.")
        return -1
    num = int(raw)
    if num < 1 or num > len(tasks):
        print("Invalid number. Must be 1 to", len(tasks))
        return -1
    return num - 1

def mark_done():
    if not tasks:
        print("No tasks to mark.")
        return
    idx = get_task_index("mark as done")
    if idx == -1:
        return
    if tasks[idx].startswith("DONE: "):
        print("Already marked as done.")
    else:
        tasks[idx] = "DONE: " + tasks[idx]
        print("Marked as done.")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    idx = get_task_index("remove")
    if idx == -1:
        return
    removed = tasks.pop(idx)
    print("Removed:", removed)

print("Todo App")

while True:
    show_menu()
    choice = input("Your choice (1-5): ").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye! Tasks remaining:", len(tasks))
        break
    else:
        print("Invalid choice. Enter 1-5.")
