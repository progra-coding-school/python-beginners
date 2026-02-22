# Program Code: VAR-UN-01
# Title: Why Variables Exist
# Cognitive Skill: Understanding
# Topic: Variables in Python

# WITHOUT variables — name repeated in every line
print("Welcome, Aarav!")
print("Aarav, attendance marked.")
print("Aarav, fee receipt ready.")
print("Goodbye, Aarav!")

# Problem: if the name changes, you must fix 4 lines.

# WITH a variable — define once, use everywhere
student_name = "Aarav Sharma"

print("Welcome,", student_name)
print(student_name, "attendance marked.")
print(student_name, "fee receipt ready.")
print("Goodbye,", student_name)

# Change student_name to your name — all 4 lines update automatically.

# Real example: report card
student_name = "Priya Nair"
marks = 94
total_marks = 100

print("Name:", student_name)
print("Marks:", marks, "/", total_marks)
print("Percent:", marks / total_marks * 100)

# Change marks = 96 and the percentage updates automatically.

# Think:
# 1. A cricket scoreboard shows the player's score in 4 places.
#    How does a variable help every time the score changes?
# 2. Name 3 things in daily life that change and should be in a variable.
