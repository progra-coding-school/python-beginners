# Program Code: OP-KN-04
# Title: Logical Operators
# Cognitive Skill: Knowledge
# Topic: Operators in Python

# Logical operators combine multiple conditions.
# They return True or False.

# --- and ---
# Both conditions must be True → result is True
# If any one is False → result is False
print("=== and operator ===")
print(True and True)    # True  → both True
print(True and False)   # False → one is False
print(False and True)   # False → one is False
print(False and False)  # False → both False

# --- or ---
# At least one condition must be True → result is True
# Both must be False → result is False
print("\n=== or operator ===")
print(True or True)     # True  → both True
print(True or False)    # True  → one is True
print(False or True)    # True  → one is True
print(False or False)   # False → both False

# --- not ---
# Flips the result: True becomes False, False becomes True
print("\n=== not operator ===")
print(not True)    # False
print(not False)   # True

print()
# Real-life examples

# and: Both conditions needed
age = 17
has_id = True
if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry not allowed.")  # age < 18, so denied

# or: At least one condition needed
is_holiday = False
is_weekend = True
if is_holiday or is_weekend:
    print("School is off!")    # is_weekend is True, so allowed

# not: Flip a condition
is_raining = False
if not is_raining:
    print("Good weather for a walk!")

# Think:
# 1. Aarav can join the cricket team if: age >= 12 AND height >= 140 cm.
#    Write the condition.
# 2. The canteen is open if: it's lunch time OR it's snack time.
#    Write the condition.
