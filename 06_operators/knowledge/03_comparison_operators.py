# Program Code: OP-KN-03
# Title: Comparison Operators
# Cognitive Skill: Knowledge
# Topic: Operators in Python

# Comparison operators compare two values.
# They always return True or False.

marks = 72
pass_mark = 35

print("marks =", marks, "  pass_mark =", pass_mark)
print()

# == Equal to
print("marks == 72 →", marks == 72)       # True
print("marks == 80 →", marks == 80)       # False

# != Not equal to
print("marks != 80 →", marks != 80)       # True
print("marks != 72 →", marks != 72)       # False

# > Greater than
print("marks > pass_mark →", marks > pass_mark)    # True

# < Less than
print("marks < pass_mark →", marks < pass_mark)    # False

# >= Greater than or equal to
print("marks >= 72 →", marks >= 72)       # True
print("marks >= 75 →", marks >= 75)       # False

# <= Less than or equal to
print("marks <= 80 →", marks <= 80)       # True
print("marks <= 70 →", marks <= 70)       # False

print()
# Real-life uses — comparison operators drive decisions
age = 15
if age >= 18:
    print("Can vote.")
else:
    print("Too young to vote.")

temperature = 38.2
if temperature > 37.5:
    print("Fever detected. Stay home.")

score = 91
if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
else:
    print("Grade: B")

# Think:
# 1. What is the difference between = and ==?
# 2. Write a comparison to check if your age is between 10 and 18.
