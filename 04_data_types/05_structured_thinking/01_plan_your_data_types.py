# Program Code: DT-ST-01
# Title: Aarav's Report Card Generator
# Cognitive Skill: Structured Thinking (Plan first, then code)
# Topic: Data Types in Python

# PLAN BEFORE CODING:
# Category 1 — Identity (str): student_name, class_name, school
# Category 2 — Marks (int): tamil, english, maths, science, social
# Category 3 — Results (float): total_marks, average, percentage
# Category 4 — Status (bool): is_passed, is_distinction
# Category 5 — Display (str): result_text, grade

# --- Category 1: Identity ---
student_name = input("Student name: ")
class_name = input("Class: ")
school = input("School name: ")

# --- Category 2: Marks ---
tamil = int(input("Tamil marks (out of 100): "))
english = int(input("English marks (out of 100): "))
maths = int(input("Maths marks (out of 100): "))
science = int(input("Science marks (out of 100): "))
social = int(input("Social marks (out of 100): "))

# --- Category 3: Results ---
total_marks = tamil + english + maths + science + social
average = total_marks / 5
percentage = (total_marks / 500) * 100

# --- Category 4: Status ---
is_passed = all([tamil >= 35, english >= 35, maths >= 35, science >= 35, social >= 35])
is_distinction = percentage >= 75

# --- Category 5: Display ---
result_text = "PASS" if is_passed else "FAIL"
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "D"

print(f"\n--- Report Card ---")
print(f"Name: {student_name}  |  Class: {class_name}  |  School: {school}")
print(f"Tamil: {tamil}  English: {english}  Maths: {maths}  Science: {science}  Social: {social}")
print(f"Total: {total_marks}/500  |  Average: {average:.1f}  |  Percentage: {percentage:.1f}%")
print(f"Grade: {grade}  |  Result: {result_text}")

# Think:
# 1. Did planning the categories first make coding easier?
# 2. Why are marks stored as int but percentage stored as float?
