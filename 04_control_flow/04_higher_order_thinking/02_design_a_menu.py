# Program Code: CF-HOT-02
# Title: Design a Menu-Driven Program
# Cognitive Skill: Higher Order Thinking (Creating with control flow)
# Topic: Control Flow in Python

# TASK: Build a simple student record menu using loops and conditions.
# The menu should keep running until the user chooses to exit.

print("=== Student Record System ===")
students = []

while True:
    print("\n--- Menu ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})
        print(f"{name} added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No students yet.")
        else:
            print("\n--- Student List ---")
            for i, s in enumerate(students, start=1):
                print(f"{i}. {s['name']} — Marks: {s['marks']}")

    elif choice == "3":
        search = input("Enter name to search: ").lower()
        found = False
        for s in students:
            if s["name"].lower() == search:
                print(f"Found: {s['name']} — Marks: {s['marks']}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Think:
# 1. Which loop keeps the menu running? Why while True?
# 2. What does 'break' do in this context?
# 3. Can you add option 5: 'Show highest scorer'?
