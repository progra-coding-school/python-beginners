# Todo App – Powered by a List
# One list (tasks = []) drives the whole app:
#   Add:    tasks.append(text)       → new task goes to the end
#   View:   enumerate(tasks, start=1) → show items numbered from 1
#   Done:   tasks[index] = "DONE: " + task  → update item in place
#   Remove: tasks.pop(index)         → delete by position
#   Menu:   while True + if-elif + break   → keeps the app running until user exits
# Each feature is its own function — one function, one job.

tasks = []   # the single list that stores everything

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
        tasks.append(text)           # append adds to the end of the list
        print("Added. Total tasks:", len(tasks))
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:                    # empty list is "falsy" — same as len(tasks) == 0
        print("No tasks yet.")
        return
    print()
    for i, task in enumerate(tasks, start=1):   # enumerate gives (index, item); start=1 shows 1,2,3 to user
        print("  " + str(i) + ". " + task)
    print("Total:", len(tasks))

def get_task_index(action):
    # Helper: show the list, ask for a task number, validate input, return 0-based index
    # Users see 1-based numbers (1, 2, 3...) but lists use 0-based indices (0, 1, 2...)
    # So we subtract 1: user types 2 → we use index 1
    view_tasks()
    raw = input("Enter task number to " + action + ": ").strip()
    if not raw.isdigit():
        print("Please enter a number.")
        return -1
    num = int(raw)
    if num < 1 or num > len(tasks):
        print("Invalid number. Must be 1 to", len(tasks))
        return -1
    return num - 1   # convert 1-based user input to 0-based list index

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
        tasks[idx] = "DONE: " + tasks[idx]   # update the item in place — lists are mutable!
        print("Marked as done.")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    idx = get_task_index("remove")
    if idx == -1:
        return
    removed = tasks.pop(idx)    # pop(index) removes and returns the item
    print("Removed:", removed)

print("Todo App")

# Main loop — keeps running until the user picks Exit (choice 5 → break)
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
