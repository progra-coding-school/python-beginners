# Program Code: LP-HOT-03
# Title: Loop Mini App — Attendance Tracker
# Cognitive Skill: Higher Order Thinking (Creative Synthesis)
# Topic: Loops in Python

# Build a complete attendance tracker using loops.
# Every feature depends on looping through the class list.

print("╔══════════════════════════════════╗")
print("║   Progra Attendance Tracker     ║")
print("╚══════════════════════════════════╝")

# --- Setup: class list ---
students = ["Aarav", "Diya", "Karthik", "Riya", "Aman", "Priya", "Rohan", "Meena"]
attendance = {}   # name → list of daily status ("P" or "A")
days_completed = 0

def take_attendance():
    global days_completed
    days_completed += 1
    print(f"\n--- Day {days_completed} Attendance ---")
    for student in students:
        while True:
            status = input(f"  {student} (P/A): ").upper()
            if status in ["P", "A"]:
                break
            print("  Please enter P (Present) or A (Absent)")
        if student not in attendance:
            attendance[student] = []
        attendance[student].append(status)
    print("Attendance saved!")

def show_today():
    if days_completed == 0:
        print("No attendance taken yet.")
        return
    print(f"\n--- Attendance for Day {days_completed} ---")
    for student in students:
        status = attendance[student][-1]
        label = "Present" if status == "P" else "Absent"
        print(f"  {student:10} : {label}")

def show_summary():
    if days_completed == 0:
        print("No attendance taken yet.")
        return
    print(f"\n--- Attendance Summary ({days_completed} days) ---")
    print(f"  {'Name':12} {'Present':8} {'Absent':8} {'%':6}")
    print("  " + "-" * 38)
    for student in students:
        records = attendance.get(student, [])
        present = records.count("P")
        absent  = records.count("A")
        total   = len(records)
        percent = (present / total * 100) if total > 0 else 0
        flag    = " ⚠ LOW" if percent < 75 else ""
        print(f"  {student:12} {present:8} {absent:8} {percent:5.1f}%{flag}")

def find_absentees():
    if days_completed == 0:
        print("No attendance taken yet.")
        return
    print(f"\n--- Absentees on Day {days_completed} ---")
    found = False
    for student in students:
        if attendance[student][-1] == "A":
            print(f"  {student} was absent.")
            found = True
    if not found:
        print("  Full attendance today!")

def show_menu():
    print("\n=== Menu ===")
    print("1. Take today's attendance")
    print("2. Show today's attendance")
    print("3. Summary report")
    print("4. Today's absentees")
    print("5. Exit")

# --- Main app loop ---
while True:
    show_menu()
    choice = input("Choose (1-5): ")

    if choice == "1":
        take_attendance()
    elif choice == "2":
        show_today()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        find_absentees()
    elif choice == "5":
        print("Goodbye! Attendance saved.")
        break
    else:
        print("Invalid choice. Try again.")

# Think:
# 1. How would you add a feature to search for a specific student's record?
# 2. How would you generate a monthly report (30 days of attendance)?
