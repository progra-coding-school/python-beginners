# Program Code: LP-UN-01
# Title: Why Loops Exist
# Cognitive Skill: Understanding
# Topic: Loops in Python

# Without loops: code is repeated line by line — slow, error-prone, unscalable.
# With loops: one block handles any number of items.

print("=== WITHOUT a loop — 5 students ===")
print("Aarav's attendance: Present")
print("Diya's attendance: Present")
print("Karthik's attendance: Present")
print("Riya's attendance: Absent")
print("Aman's attendance: Present")
print("(What if there are 500 students?!)")

print()

print("=== WITH a loop — any number of students ===")
students = [
    ("Aarav",   "Present"),
    ("Diya",    "Present"),
    ("Karthik", "Present"),
    ("Riya",    "Absent"),
    ("Aman",    "Present"),
]
for name, status in students:
    print(f"{name}'s attendance: {status}")
print("(Add 500 more names — same 3 lines of loop code!)")

print()

# --- Without loop: can't process unknown count ---
print("=== Loop handles UNKNOWN count ===")
total = 0
count = 0
print("Enter marks one by one (type -1 to stop):")
while True:
    mark = int(input("Mark: "))
    if mark == -1:
        break
    total += mark
    count += 1

if count > 0:
    print(f"Total: {total}, Average: {total/count:.1f}")
else:
    print("No marks entered.")

print()

# --- 3 reasons loops exist ---
print("=== Why Loops? ===")
print("1. SCALE: Handle 5 or 5000 items with the same code")
print("2. UNKNOWN count: Keep going until a condition is met")
print("3. PATTERN: Repeat a calculation for every item automatically")

# Think:
# 1. A teacher checks 30 answer sheets. Without a loop, how many if-statements?
# 2. Name a task in daily life that naturally repeats until a condition is met.
