# Program Code: CF-ST-03
# Title: Loop with Accumulator Pattern
# Cognitive Skill: Structured Thinking (Recognizing patterns)
# Topic: Control Flow in Python

# The ACCUMULATOR PATTERN:
# 1. Create a variable BEFORE the loop (starts at 0 or [])
# 2. Update it INSIDE the loop
# 3. Use it AFTER the loop

print("=== Accumulator Pattern ===\n")

# Pattern 1: Sum accumulator
print("--- Sum of marks ---")
marks = [88, 74, 92, 65, 81]
total = 0                    # Step 1: initialize
for mark in marks:
    total += mark            # Step 2: update
print("Total:", total)       # Step 3: use

# Pattern 2: Count accumulator
print("\n--- Count students above 80 ---")
count_above_80 = 0
for mark in marks:
    if mark > 80:
        count_above_80 += 1
print("Above 80:", count_above_80)

# Pattern 3: List accumulator (collect results)
print("\n--- Collect students who passed ---")
student_names = ["Aarav", "Diya", "Priya", "Karthik", "Meera"]
passed = []
for i in range(len(marks)):
    if marks[i] >= 35:
        passed.append(student_names[i])
print("Passed:", passed)

# Pattern 4: Max/Min accumulator
print("\n--- Find highest mark ---")
highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark
print("Highest:", highest)

# Think:
# 1. What would happen if you set total = 1 instead of total = 0? Why does it matter?
# 2. Can you write an accumulator that counts how many marks are below 70?
