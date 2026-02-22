# Program Code: LIST-PS-02
# Title: Find the Class Topper — Analysing Student Marks!
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Lists in Python

# ======================================================
# WHAT PROBLEM ARE WE SOLVING?
# ======================================================
# Class teacher Meera Ma'am has just finished correcting
# the Math test papers for 5 students.
# She needs to:
#   - Find out WHO scored the highest (the class topper)
#   - Find out WHO scored the lowest
#   - Calculate the class average
#   - Identify students who scored ABOVE average
#
# WHY USE LISTS?
# Names and marks go together — parallel lists let us
# store them separately but link them using index numbers.
# The same index in both lists = the same student.
# e.g., names[0] and marks[0] both belong to student 1.
# ======================================================

# ======================================================
# DECOMPOSE THE PROBLEM
# ======================================================
# Break the big problem into small, clear steps:
#
# Step 1: Store student names and marks in two parallel lists
# Step 2: Find the highest marks and who got them using index()
# Step 3: Find the lowest marks and who got them using index()
# Step 4: Calculate the total marks and the class average
# Step 5: Display all results neatly in a report
# Step 6: List only the students who scored above average
#
# BONUS: Sort students from Rank 1 (highest) to Rank 5 (lowest)
#        and print a proper rank card for the class
# ======================================================


print("=" * 55)
print("   Find the Class Topper — Analysing Student Marks!")
print("=" * 55)


# --------------------------------------------------
# STEP 1: Store student names and marks
# --------------------------------------------------
# Two parallel lists — same index = same student
# names[0] = "Aarav"  and  marks[0] = 88 → same person

names = ["Aarav", "Diya",  "Rohan", "Priya", "Karthik"]
marks = [88,       95,      72,      85,       91]

print("\nStep 1: Class data entered by Meera Ma'am")
print("-" * 40)
print(f"{'Student':<12} {'Marks':>6}")
print("-" * 20)

for i in range(len(names)):
    print(f"{names[i]:<12} {marks[i]:>6}")

print("-" * 20)


# --------------------------------------------------
# STEP 2: Find the highest marks (topper)
# --------------------------------------------------
# max() finds the highest value in the list
# index() gives us the POSITION of that value
# Using that position on the names list gives the topper's name

highest_marks = max(marks)
topper_index  = marks.index(highest_marks)   # position of max score
topper_name   = names[topper_index]          # same position in names list

print("\nStep 2: Finding the class topper")
print("-" * 40)
print(f"Highest marks in the list : {highest_marks}")
print(f"Position (index) of topper: {topper_index}")
print(f"Topper name               : {topper_name}")


# --------------------------------------------------
# STEP 3: Find the lowest marks
# --------------------------------------------------
# Same idea as Step 2 but using min() this time

lowest_marks    = min(marks)
weakest_index   = marks.index(lowest_marks)
weakest_student = names[weakest_index]

print("\nStep 3: Finding the lowest scorer")
print("-" * 40)
print(f"Lowest marks in the list  : {lowest_marks}")
print(f"Position (index)          : {weakest_index}")
print(f"Student name              : {weakest_student}")


# --------------------------------------------------
# STEP 4: Calculate total and class average
# --------------------------------------------------
# sum() adds all values in the list
# Divide by the number of students for the average

total_marks   = sum(marks)
num_students  = len(marks)
class_average = total_marks / num_students

print("\nStep 4: Class average calculation")
print("-" * 40)
print(f"Sum of all marks    : {total_marks}")
print(f"Number of students  : {num_students}")
print(f"Class average       : {class_average:.2f}")   # .2f = 2 decimal places


# --------------------------------------------------
# STEP 5: Display the full results report
# --------------------------------------------------

print()
print("=" * 55)
print("        MEERA MA'AM'S CLASS REPORT — MATH TEST")
print("=" * 55)
print(f"  Class Topper    : {topper_name} with {highest_marks} marks")
print(f"  Lowest Scorer   : {weakest_student} with {lowest_marks} marks")
print(f"  Class Average   : {class_average:.2f} marks")
print(f"  Total Students  : {num_students}")
print("=" * 55)


# --------------------------------------------------
# STEP 6: Students who scored ABOVE average
# --------------------------------------------------
# Loop through the marks list
# For each mark, check if it is greater than the average
# If yes, the student at that same index scored above average

print("\nStep 6: Students who scored ABOVE class average")
print("-" * 40)
print(f"Class average is {class_average:.2f} — students above this:\n")

above_average_found = False

for i in range(len(marks)):
    if marks[i] > class_average:
        print(f"  {names[i]:<12} scored {marks[i]} — above average!")
        above_average_found = True

if not above_average_found:
    print("  No students scored above average in this test.")


# --------------------------------------------------
# BONUS: Rank card — sorted from highest to lowest
# --------------------------------------------------
# We create a combined list of [score, name] pairs
# so we can sort by score and still keep the name linked
# Then we reverse it so highest comes first (Rank 1)

print()
print("=" * 55)
print("   BONUS: Class Rank Card (Highest → Lowest)")
print("=" * 55)

# Pair each score with its name: [[88, "Aarav"], [95, "Diya"], ...]
score_name_pairs = []
for i in range(len(names)):
    score_name_pairs.append([marks[i], names[i]])

# Sort the pairs — Python sorts by the first element (score) by default
score_name_pairs.sort(reverse=True)   # reverse=True → highest first

print(f"\n{'Rank':<6} {'Student':<12} {'Marks':>6}")
print("-" * 28)

for rank, pair in enumerate(score_name_pairs, start=1):
    score = pair[0]
    name  = pair[1]
    # Mark the topper with a special label
    label = "  <-- TOPPER!" if rank == 1 else ""
    print(f"{rank:<6} {name:<12} {score:>6}{label}")

print("=" * 55)
print("\nGreat work, Meera Ma'am! Report is ready.")


# ======================================================
# REFLECTION — Think and Answer
# ======================================================
# 1. Why do we use two separate lists (names and marks)
#    instead of one? What is the advantage of parallel lists?
#
# 2. What does marks.index(highest_marks) actually return —
#    a name or a number? How do we use it to get the name?
#
# 3. If two students scored the same highest mark,
#    what would index() return? Would that be a problem?
#    How could you fix it?
#
# 4. In the BONUS section, why do we use reverse=True in sort()?
#    What would happen if we left it out?
# ======================================================
