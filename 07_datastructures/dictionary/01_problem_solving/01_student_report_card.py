# Program Code: DC-PS-01
# Title: Student Report Card Builder
# Cognitive Skill: Problem Solving
# Topic: Dictionaries in Python

# Problem:
# Aarav's school needs a digital report card.
# Store a student's marks in 5 subjects and then:
# 1. Display all subject marks
# 2. Calculate total and average
# 3. Find the highest and lowest scoring subject
# 4. Print a grade (A+ / A / B / C) for each subject

# --- Step 1: Store the report card ---
report = {
    "Maths":   88,
    "Science": 92,
    "English": 74,
    "History": 80,
    "Tamil":   95,
}

student_name = "Aarav"

print(f"=== {student_name}'s Report Card ===")
print()

# --- Step 2: Display all subjects ---
print("Subject-wise Marks:")
for subject, marks in report.items():
    print(f"  {subject:10} : {marks}")

print()

# --- Step 3: Total and average ---
total   = sum(report.values())
average = total / len(report)
print(f"Total   : {total}")
print(f"Average : {average:.1f}")

print()

# --- Step 4: Highest and lowest subject ---
best_subject  = max(report, key=report.get)
worst_subject = min(report, key=report.get)

print(f"Best subject  : {best_subject} ({report[best_subject]})")
print(f"Needs work on : {worst_subject} ({report[worst_subject]})")

print()

# --- Step 5: Grade for each subject ---
def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

print("Grades:")
for subject, marks in report.items():
    grade = get_grade(marks)
    print(f"  {subject:10} : {grade}")

# Think:
# 1. How would you add a new subject to the report card?
# 2. What would change if a student had 8 subjects instead of 5?
