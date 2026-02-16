# Program Code: CS-PS-03
# Title: Priya's School Report Card
# Cognitive Skill: Problem Solving (Plan First, Then Code)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Priya got her exam results. She wants to create a
# report card that shows all her marks, total, and percentage.
# But before writing code, she needs to PLAN what
# variables she will need. Planning first = fewer mistakes!
# ============================================================

# ------------------------------------------------------------
# PLANNING SECTION (Fill this BEFORE writing code!):
#
# What variables do I need?
#
# Subject marks:
#   - maths_mark      (stores Maths marks)
#   - science_mark    (stores Science marks)
#   - english_mark    (stores English marks)
#   - tamil_mark      (stores Tamil marks)
#   - social_mark     (stores Social Science marks)
#
# Calculations:
#   - total_marks     (sum of all 5 subjects)
#   - max_marks       (maximum possible marks = 5 x 100)
#   - percentage      (total / max * 100)
#
# Student info:
#   - student_name    (Priya's name)
#   - grade           (which class she is in)
#
# Total variables needed: 10
# ------------------------------------------------------------

print("=== School Report Card Builder ===")
print()

# STEP 1: Collect student information
student_name = input("Enter student name: ")
grade = input("Enter class/grade: ")

# STEP 2: Collect marks for each subject (5 sub-problems)
print()
print("Enter marks out of 100 for each subject:")
maths_mark = int(input("  Maths:          "))
science_mark = int(input("  Science:        "))
english_mark = int(input("  English:        "))
tamil_mark = int(input("  Tamil:          "))
social_mark = int(input("  Social Science: "))

# STEP 3: Calculate total and percentage
total_marks = maths_mark + science_mark + english_mark + tamil_mark + social_mark
max_marks = 500
percentage = (total_marks / max_marks) * 100

# STEP 4: Display the report card
print()
print("=" * 45)
print("         SCHOOL REPORT CARD")
print("=" * 45)
print(f"  Student Name : {student_name}")
print(f"  Class        : {grade}")
print("-" * 45)
print("  SUBJECT          MARKS")
print("-" * 45)
print(f"  Maths            {maths_mark}/100")
print(f"  Science          {science_mark}/100")
print(f"  English          {english_mark}/100")
print(f"  Tamil            {tamil_mark}/100")
print(f"  Social Science   {social_mark}/100")
print("-" * 45)
print(f"  TOTAL:           {total_marks}/{max_marks}")
print(f"  PERCENTAGE:      {percentage}%")
print("=" * 45)

# ============================================================
# REFLECTION PROMPTS:
# 1. We planned 10 variables before writing code.
#    Did the plan help? What if we had started coding without it?
# 2. If your school also gives marks for Computer Science
#    and Art, what new variables would you add to the plan?
# 3. The PLANNING SECTION at the top is like a blueprint
#    for a building. Why do architects draw blueprints
#    before building a house?
# ============================================================
