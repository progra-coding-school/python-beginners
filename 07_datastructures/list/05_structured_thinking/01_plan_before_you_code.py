# Program Code: LIST-ST-01
# Title: Plan Before You Code
# Cognitive Skill: Structured Thinking (Planning)
# Topic: Lists in Python

# PLANNING BLOCK (write this BEFORE coding):
#   WHAT to store?   → student_names, student_marks (parallel lists)
#   WHAT to do?      → find topper, sort by rank, print table
#   WHAT output?     → ranked table: Rank | Name | Marks
#   HOW to break it? → Step 1: data  Step 2: topper  Step 3: sort  Step 4: table

print("=== Plan Before You Code ===")
print()

# Step 1: Set up the data
student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
student_marks = [88, 95, 76, 91, 83]

print("Step 1 — Data:")
print("  student_names =", student_names)
print("  student_marks =", student_marks)
print()

# Step 2: Find the topper
highest_marks = max(student_marks)
topper_index  = student_marks.index(highest_marks)
topper_name   = student_names[topper_index]

print("Step 2 — Topper:")
print("  Highest marks:", highest_marks)
print("  Topper:", topper_name)
print("  Trick: index() finds the position of max — same position in names gives the topper.")
print()

# Step 3: Sort both lists together by marks (highest first)
# zip() pairs names+marks so they stay linked during sort
paired = list(zip(student_marks, student_names))
paired.sort(reverse=True)
sorted_marks = [m for m, n in paired]
sorted_names = [n for m, n in paired]

print("Step 3 — Sorted (highest first):", sorted_names)
print()

# Step 4: Print ranked table
print("Step 4 — Ranked Table:")
print("  Rank  Name        Marks")
print("  " + "-" * 28)
for rank in range(len(sorted_names)):
    label = " <-- Topper!" if rank == 0 else ""
    print("  " + str(rank + 1).ljust(6) + sorted_names[rank].ljust(12) + str(sorted_marks[rank]) + label)
print()

# WITHOUT A PLAN — Mani's messy version
print("=== Without a Plan — Mani's Version ===")
x = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
y = [88, 95, 76, 91, 83]

y_sorted = sorted(y, reverse=True)   # sorted marks only
# Problem: which name goes with which mark? Nobody knows!
print("  y_sorted =", y_sorted)
print("  Problem: the names are not sorted. Mani lost track and had to start over!")
print()

print("Lesson: 5 minutes planning saves 20 minutes of confusion.")
print()
print("Planning checklist:")
print("  [ ] WHAT to store?   → pick your lists")
print("  [ ] WHAT to do?      → list the operations")
print("  [ ] WHAT output?     → picture the result")
print("  [ ] HOW to break it? → number the steps")
