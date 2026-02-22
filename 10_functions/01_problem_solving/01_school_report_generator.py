# Program Code: FN-PS-01
# Title: School Report Card Generator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Functions in Python

# Big question: How do we generate a complete report card?
# Break it into small jobs — one function per job.

# --- PLAN ---
# Function 1: calculate_total(m, s, e, h, c) → total marks
# Function 2: calculate_average(total) → average
# Function 3: get_grade(average) → grade letter
# Function 4: get_result(maths, science, english) → PASS/FAIL
# Function 5: print_report(name, ...) → display everything

def calculate_total(maths, science, english, hindi, computer):
    return maths + science + english + hindi + computer

def calculate_average(total, subjects=5):
    return total / subjects

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 35:
        return "C"
    else:
        return "FAIL"

def get_result(maths, science, english, hindi, computer):
    # Must pass EACH subject with at least 35 marks
    subjects = [maths, science, english, hindi, computer]
    for mark in subjects:
        if mark < 35:
            return "FAIL"
    return "PASS"

def get_remarks(grade):
    remarks = {
        "A+": "Outstanding! Keep it up!",
        "A":  "Excellent performance!",
        "B+": "Very good! Push harder!",
        "B":  "Good effort. Can do better.",
        "C":  "Average. Needs improvement.",
        "FAIL": "Work harder. You can do it!"
    }
    return remarks.get(grade, "")

def print_report(name, maths, science, english, hindi, computer):
    total    = calculate_total(maths, science, english, hindi, computer)
    average  = calculate_average(total)
    grade    = get_grade(average)
    result   = get_result(maths, science, english, hindi, computer)
    remarks  = get_remarks(grade)

    print("=" * 45)
    print(f"     PROGRA SCHOOL — REPORT CARD")
    print("=" * 45)
    print(f"  Student   : {name}")
    print(f"  Maths     : {maths}/100")
    print(f"  Science   : {science}/100")
    print(f"  English   : {english}/100")
    print(f"  Hindi     : {hindi}/100")
    print(f"  Computer  : {computer}/100")
    print(f"  Total     : {total}/500")
    print(f"  Average   : {average:.1f}")
    print(f"  Grade     : {grade}")
    print(f"  Result    : {result}")
    print(f"  Remarks   : {remarks}")
    print("=" * 45)

# --- Generate reports ---
student_name = input("Enter student name: ")
m = int(input("Maths marks (out of 100): "))
s = int(input("Science marks (out of 100): "))
e = int(input("English marks (out of 100): "))
h = int(input("Hindi marks (out of 100): "))
c = int(input("Computer marks (out of 100): "))

print_report(student_name, m, s, e, h, c)

# Think:
# 1. What new function would you add to calculate rank among 30 students?
# 2. Which function would you change to add a new subject?
