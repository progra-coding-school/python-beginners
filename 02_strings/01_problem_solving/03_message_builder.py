# Program Code: STR-PS-03
# Title: Personalised Message Builder — Greet Every Student!
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Progra wants to send personalised welcome messages to students.
# Each message should include:
#   - Student's name (formatted properly)
#   - Their batch (Morning/Evening)
#   - A motivational quote
# Instead of typing each message manually, let's BUILD them!
# ============================================================

print("=" * 55)
print("    PROGRA MESSAGE BUILDER — WELCOME ALL STUDENTS!")
print("=" * 55)

# -------------------------------------------------------
# TEMPLATE: Define the message pattern once
# We'll plug in each student's details
# -------------------------------------------------------
def build_message(raw_name, batch, course):
    name   = raw_name.strip().title()         # Format name
    batch  = batch.strip().title()
    course = course.strip().title()

    # Build the personalised message using concatenation
    line1 = "Dear " + name + ","
    line2 = "Welcome to the " + batch + " Batch — " + course + "!"
    line3 = "At Progra, we train minds to think, structure, apply, and lead."
    line4 = "Happy coding, " + name.split()[0] + "! 🚀"   # First name only

    # Join all lines into one message
    message = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    return message

# -------------------------------------------------------
# STUDENT DATA
# -------------------------------------------------------
students = [
    ("  aarav sharma  ", "morning", "python beginners"),
    ("DIYA NAIR",        "evening", "python beginners"),
    ("mani kumar",       "Morning", "python advanced"),
]

for raw_name, batch, course in students:
    print("\n" + "-" * 50)
    msg = build_message(raw_name, batch, course)
    print(msg)

print("\n" + "-" * 50)

# -------------------------------------------------------
# INTERACTIVE: Build a custom message for any student
# -------------------------------------------------------
print("\n--- Build a Custom Message ---")
name_input   = input("Enter student name : ")
batch_input  = input("Enter batch (Morning/Evening) : ")
course_input = input("Enter course : ")

print("\n" + "=" * 50)
custom_msg = build_message(name_input, batch_input, course_input)
print(custom_msg)
print("=" * 50)

# ============================================================
# REFLECTION:
# 1. What does .split()[0] do on "Aarav Sharma"?
# 2. Can you add the student's ID number to the message?
# 4. What would happen if someone entered only one name (no last name)?
# ============================================================
