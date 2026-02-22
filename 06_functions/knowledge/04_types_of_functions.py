# Program Code: FN-KN-04
# Title: Types of Functions
# Cognitive Skill: Knowledge
# Topic: Functions in Python

# Functions come in 4 patterns based on parameters and return values.

print("=== Type 1: No parameters, No return ===")
# Just does a task — like an announcement
def show_welcome():
    print("Welcome to Progra Coding School!")
    print("Today we learn Functions!")

show_welcome()
print()

print("=== Type 2: With parameters, No return ===")
# Takes input, does something, but gives nothing back
def show_report(name, marks):
    print(f"Student: {name}")
    print(f"Marks:   {marks}/100")
    if marks >= 35:
        print("Result:  PASS")
    else:
        print("Result:  FAIL")

show_report("Aarav", 85)
print()

print("=== Type 3: No parameters, With return ===")
# Generates and returns something without needing input
def get_school_name():
    return "Progra Kids Coding School"

school = get_school_name()
print("School:", school)
print()

print("=== Type 4: With parameters, With return ===")
# The most useful pattern — takes input, gives back a calculated result
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 35:
        return "C"
    else:
        return "FAIL"

grade = calculate_grade(87)
print("Grade:", grade)

# Chain them together!
print("Aarav's grade:", calculate_grade(92))
print("Diya's grade:", calculate_grade(61))
print("Riya's grade:", calculate_grade(28))

# --- Summary ---
# Type 1: def f()         — no input, no output  → announcements, display
# Type 2: def f(x)        — input, no output     → display formatted data
# Type 3: def f() return  — no input, has output → fixed values, config
# Type 4: def f(x) return — input, has output    → calculations (most common!)

# Think:
# 1. Which type would you use to calculate total marks? Why?
# 2. Which type would you use to print a welcome banner?
