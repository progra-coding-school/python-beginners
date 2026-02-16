# Program Code: 07-application-01
# Title: My Todo List App

# A simple todo list where you can:
# 1. Add a task
# 2. View all tasks
# 3. Remove a completed task
# 4. Exit

todo_list = []

while True:
    print("\n--- My Todo List ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i in range(len(todo_list)):
                print(i + 1, ".", todo_list[i])

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove!")
        else:
            for i in range(len(todo_list)):
                print(i + 1, ".", todo_list[i])
            task_number = int(input("Enter task number to remove: "))
            if task_number >= 1 and task_number <= len(todo_list):
                removed = todo_list.pop(task_number - 1)
                print("Removed:", removed)
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
