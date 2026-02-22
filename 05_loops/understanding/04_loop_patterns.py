# Program Code: LP-UN-04
# Title: Common Loop Patterns
# Cognitive Skill: Understanding
# Topic: Loops in Python

# These are the 5 most useful loop patterns you'll use in real programs.

print("=== Pattern 1: ACCUMULATOR (build a total) ===")
marks = [85, 72, 90, 65, 88, 76]
total = 0              # accumulator starts at 0
for mark in marks:
    total += mark      # add each item to the total
average = total / len(marks)
print(f"Total: {total}, Average: {average:.1f}")

print()

print("=== Pattern 2: COUNTER (count matching items) ===")
scores = [45, 82, 91, 33, 67, 88, 25, 79]
pass_count = 0         # counter starts at 0
for score in scores:
    if score >= 35:
        pass_count += 1
print(f"Passed: {pass_count} out of {len(scores)}")

print()

print("=== Pattern 3: SEARCH (find an item) ===")
students = ["Aarav", "Diya", "Karthik", "Riya", "Aman"]
target = input("Enter a name to search: ")
found = False
for student in students:
    if student.lower() == target.lower():
        found = True
        break
if found:
    print(f"'{target}' is in the class!")
else:
    print(f"'{target}' is not found.")

print()

print("=== Pattern 4: FILTER (collect matching items) ===")
all_marks = [82, 45, 91, 33, 78, 88, 55, 65]
high_scores = []
for mark in all_marks:
    if mark >= 80:
        high_scores.append(mark)
print("High scorers (>=80):", high_scores)

print()

print("=== Pattern 5: BUILD (create output step by step) ===")
name = input("Enter a name: ")
initials = ""
for word in name.split():
    initials += word[0].upper() + "."
print("Initials:", initials)

# Think:
# 1. Which pattern would you use to find the highest mark in a list?
# 2. Which pattern would you use to count how many students scored below 35?
