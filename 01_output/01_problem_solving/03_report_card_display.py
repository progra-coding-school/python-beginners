# Program Code: OUT-PS-03
# Title: Report Card Display
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Output in Python

# Big question: How do we display a beautiful, formatted school report card?
# Break it into output decisions — header, table, summary, footer.

# Step 1: Inputs
name       = input("Student name: ")
roll_no    = input("Roll number: ")
class_name = input("Class: ")

print("Enter marks (out of 100):")
maths   = int(input("  Maths: "))
science = int(input("  Science: "))
english = int(input("  English: "))
hindi   = int(input("  Hindi: "))
computer = int(input("  Computer: "))

# Step 2: Calculations
subjects = {
    "Maths":    maths,
    "Science":  science,
    "English":  english,
    "Hindi":    hindi,
    "Computer": computer,
}
total   = sum(subjects.values())
average = total / len(subjects)
highest = max(subjects, key=subjects.get)

def get_grade(mark):
    if mark >= 90: return "A+"
    elif mark >= 80: return "A"
    elif mark >= 70: return "B+"
    elif mark >= 60: return "B"
    elif mark >= 35: return "C"
    else: return "F"

overall_grade = get_grade(average)
result = "PASS" if all(m >= 35 for m in subjects.values()) else "FAIL"

# Step 3: Print — Header
w = 44
print()
print("*" * w)
print(f"{'PROGRA KIDS CODING SCHOOL':^{w}}")
print(f"{'Annual Progress Report Card':^{w}}")
print("*" * w)
print(f"  Name     : {name:<20} Roll No : {roll_no}")
print(f"  Class    : {class_name}")
print("-" * w)

# Step 4: Print — Subject table
print(f"  {'Subject':<12} {'Marks':>6} {'Out of':>7} {'Grade':>7}")
print("-" * w)
for subject, mark in subjects.items():
    grade = get_grade(mark)
    print(f"  {subject:<12} {mark:>6} {'100':>7} {grade:>7}")

print("-" * w)

# Step 5: Print — Summary
print(f"  {'Total':<12} {total:>6} {'500':>7}")
print(f"  {'Average':<12} {average:>6.1f} {'100':>7}")
print("-" * w)
print(f"  Overall Grade : {overall_grade}")
print(f"  Result        : {result}")
print(f"  Best subject  : {highest} ({subjects[highest]}/100)")
print("*" * w)
print(f"{'Keep learning and keep growing!':^{w}}")
print("*" * w)

# Think:
# 1. How would you add a rank if you had marks for 30 students?
# 2. What would you change to make this card work for a different school?
