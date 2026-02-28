# Program Code: STR-ST-01
# Title: Plan Before You Code — Build a Student Report Formatter!
# Cognitive Skill: Structured Thinking (Planning approach)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Diya's school asked her to build a text-based report formatter.
# It takes a student's name and marks, then prints a neat report.
# Before writing ANY code — PLAN IT OUT!
# ============================================================

# ============================================================
# ===          PLANNING SECTION (Always do this first!)     ===
# ============================================================
# WHAT do we need to do?
#   → Take student name and subject marks as input
#   → Format the name (strip + title)
#   → Calculate total and average
#   → Assign a grade based on average
#   → Print a neat, formatted report card
#
# HOW will we use strings?
#   → strip() and title() to format names
#   → Concatenation to build the report lines
#   → Repetition (*) for borders and separators
#   → ljust() / rjust() for column alignment
#
# WHAT is the expected output?
#   → A bordered report card with name, marks, total, avg, grade
# ============================================================

print("=" * 55)
print("    PROGRA REPORT CARD FORMATTER")
print("=" * 55)

# -------------------------------------------------------
# STEP 1: Collect student data
# -------------------------------------------------------
raw_name = input("\nEnter student name : ")
print("Enter marks out of 100:")

subjects = {
    "Mathematics" : int(input("  Mathematics : ")),
    "Science"     : int(input("  Science     : ")),
    "English"     : int(input("  English     : ")),
    "Tamil"       : int(input("  Tamil       : ")),
    "Computers"   : int(input("  Computers   : ")),
}

# -------------------------------------------------------
# STEP 2: Format name using strings
# -------------------------------------------------------
student_name = raw_name.strip().title()

# -------------------------------------------------------
# STEP 3: Calculate totals
# -------------------------------------------------------
total   = sum(subjects.values())
average = total / len(subjects)

# -------------------------------------------------------
# STEP 4: Assign grade using string
# -------------------------------------------------------
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

remark = "Outstanding!" if grade == "A+" else \
         "Excellent!"   if grade == "A"  else \
         "Good Work!"   if grade == "B"  else \
         "Keep Going!"  if grade == "C"  else \
         "Need Improvement"

# -------------------------------------------------------
# STEP 5: Print the formatted report card
# -------------------------------------------------------
print()
print("+" + "=" * 47 + "+")
print("|" + "     PROGRA KIDS CODING SCHOOL".center(47) + "|")
print("|" + "          STUDENT REPORT CARD".center(47) + "|")
print("|" + "-" * 47 + "|")
print("|" + ("  Student : " + student_name).ljust(47) + "|")
print("|" + "  Year    : 2025 - 2026".ljust(47) + "|")
print("|" + "-" * 47 + "|")
print("|" + ("  " + "SUBJECT".ljust(18) + "MARKS".rjust(8) + "OUT OF".rjust(8)).ljust(47) + "|")
print("|" + "  " + "-" * 30 + " " * 15 + "|")

for subject, marks in subjects.items():
    print("|" + ("  " + subject.ljust(18) + str(marks).rjust(8) + "/ 100".rjust(8)).ljust(47) + "|")

print("|" + "  " + "-" * 30 + " " * 15 + "|")
print("|" + ("  " + "TOTAL".ljust(18) + str(total).rjust(8) + "/ 500".rjust(8)).ljust(47) + "|")
print("|" + ("  " + "AVERAGE".ljust(18) + str(round(average, 1)).rjust(8) + "/ 100".rjust(8)).ljust(47) + "|")
print("|" + "-" * 47 + "|")
print("|" + ("  Grade   : " + grade).ljust(47) + "|")
print("|" + ("  Remark  : " + remark).ljust(47) + "|")
print("|" + " " * 47 + "|")
print("+" + "=" * 47 + "+")

# ============================================================
# REFLECTION:
# 1. Why did we plan before coding? What did it help us avoid?
# 2. What string operations made the output look neat?
# 3. How would you add a "Pass/Fail" status?
# 4. What would happen without strip() on the student's name?
# ============================================================
