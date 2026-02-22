# Program Code: LP-PS-02
# Title: Student Marks Processor
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Loops in Python

# Big question: Process an entire class's marks — total, average, highest, lowest, pass/fail.
# Break it into smaller loop tasks — one job per loop.

print("=== Student Marks Processor ===")

# Step 1: Collect marks
num_students = int(input("How many students? "))
names = []
marks = []

for i in range(num_students):
    name = input(f"  Student {i+1} name: ")
    mark = int(input(f"  {name}'s marks (out of 100): "))
    names.append(name)
    marks.append(mark)

print()

# Step 2: Calculate total and average (accumulator pattern)
total = 0
for mark in marks:
    total += mark
average = total / num_students

# Step 3: Find highest and lowest (search pattern)
highest = marks[0]
lowest  = marks[0]
topper  = names[0]
weakest = names[0]

for i in range(len(marks)):
    if marks[i] > highest:
        highest = marks[i]
        topper  = names[i]
    if marks[i] < lowest:
        lowest  = marks[i]
        weakest = names[i]

# Step 4: Count pass and fail (counter pattern)
pass_count = 0
fail_count = 0
for mark in marks:
    if mark >= 35:
        pass_count += 1
    else:
        fail_count += 1

# Step 5: Display individual results with grade (filter + display)
def get_grade(m):
    if m >= 90: return "A+"
    elif m >= 80: return "A"
    elif m >= 70: return "B"
    elif m >= 35: return "C"
    else: return "FAIL"

print("=== Individual Results ===")
for i in range(num_students):
    grade = get_grade(marks[i])
    status = "PASS" if marks[i] >= 35 else "FAIL"
    print(f"  {names[i]:15} {marks[i]:3}/100  Grade: {grade}  {status}")

# Step 6: Class summary
print()
print("=== Class Summary ===")
print(f"  Total students : {num_students}")
print(f"  Class total    : {total}")
print(f"  Class average  : {average:.1f}")
print(f"  Highest mark   : {highest} ({topper})")
print(f"  Lowest mark    : {lowest} ({weakest})")
print(f"  Passed         : {pass_count}")
print(f"  Failed         : {fail_count}")

# Think:
# 1. How would you find the second highest mark?
# 2. How would you print only the students who scored above the class average?
