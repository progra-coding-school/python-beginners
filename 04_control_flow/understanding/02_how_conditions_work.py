# Program Code: CF-UN-02
# Title: How Conditions Work
# Cognitive Skill: Understanding
# Topic: Control Flow in Python

# A CONDITION is any expression that evaluates to True or False.
# Python uses the result to decide which code to run.

age = 17
print(age >= 18)        # False
print(age < 18)         # True
print(age == 17)        # True
print(age != 17)        # False

# Conditions with variables
temperature = 36.5
is_fever = temperature > 37.5
print("Fever:", is_fever)    # False
if is_fever:
    print("See a doctor.")
else:
    print("You're fine!")

# Combining conditions
# and — both must be True
marks = 78
attendance = 85
if marks >= 35 and attendance >= 75:
    print("Eligible for exam.")
else:
    print("Not eligible.")

# or — at least one must be True
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Weekday.")

# not — flips True to False
is_raining = False
if not is_raining:
    print("Go for a walk!")

# Think:
# 1. Write a condition that checks: marks >= 50 AND age >= 10
# 2. What does 'not True' evaluate to? What about 'not False'?
