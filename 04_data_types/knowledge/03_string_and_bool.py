# Program Code: DT-KN-03
# Title: Strings and Booleans
# Cognitive Skill: Knowledge
# Topic: Data Types in Python

# STRINGS — any text wrapped in quotes
student_name = "Priya"
school = 'Chennai Public School'
subject = "Maths"

print(student_name)
print(school)
print(subject)

# Strings can be joined (concatenated) with +
greeting = "Hello, " + student_name + "!"
print(greeting)

# Strings have a length
print(len(student_name))   # 5 letters in "Priya"
print(len(school))

# Even numbers can be strings
roll_number = "42"          # "42" is a string, not a number!
print(type(roll_number))    # <class 'str'>

# BOOLEANS — only two values: True or False
has_submitted = True
is_absent = False

print(has_submitted)
print(is_absent)
print(type(has_submitted))  # <class 'bool'>

# Booleans from comparisons
marks = 75
passed = marks >= 35
print("Passed:", passed)    # True
above_90 = marks > 90
print("Above 90:", above_90)  # False

# Think:
# 1. Why must roll numbers like "007" be stored as strings, not integers?
# 2. What real-world situations give you a True/False answer?
