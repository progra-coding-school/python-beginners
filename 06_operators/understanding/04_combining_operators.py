# Program Code: OP-UN-04
# Title: Combining All Operators Together
# Cognitive Skill: Understanding
# Topic: Operators in Python

# Real programs combine arithmetic, comparison, and logical operators.
# Let's see how they work together.

print("=== Combining Operators ===")

# Step 1: Arithmetic gives a number
total_marks = 85 + 90 + 78       # 253 — arithmetic
average = total_marks / 3        # 84.33 — arithmetic

# Step 2: Comparison uses that number → gives bool
is_distinction = average >= 80   # True — comparison

# Step 3: Logical combines booleans
attendance = 92
eligible = is_distinction and attendance >= 75  # True and True → True

print("Total:", total_marks)
print("Average:", round(average, 2))
print("Distinction?", is_distinction)
print("Eligible for award?", eligible)

print()

# --- Example 2: Movie ticket eligibility ---
name = "Diya"
age = 14
is_accompanied = True

# Arithmetic: calculate years to 18
years_to_adult = 18 - age  # 4

# Comparison: check conditions
is_adult = age >= 18       # False
is_child = age < 12        # False

# Logical: combine for final decision
can_watch_pg13 = age >= 13 or is_accompanied  # False or True → True

print(f"{name}'s age: {age}")
print(f"Is adult: {is_adult}")
print(f"Years to adult: {years_to_adult}")
print(f"Can watch PG-13 movie: {can_watch_pg13}")

print()

# --- Example 3: ATM withdrawal ---
balance = 5000
withdrawal = int(input("Enter withdrawal amount: "))

# Arithmetic
remaining = balance - withdrawal

# Comparison + Logical
is_valid_amount = withdrawal > 0 and withdrawal <= balance
is_multiple_of_100 = withdrawal % 100 == 0
can_withdraw = is_valid_amount and is_multiple_of_100

if can_withdraw:
    print(f"Dispensing Rs.{withdrawal}. Remaining balance: Rs.{remaining}")
else:
    print("Invalid amount. Must be > 0, ≤ balance, and a multiple of 100.")

# Think:
# 1. What type does (85 + 90) >= 160 return? Trace it step by step.
# 2. Write a single expression to check: marks > 50 AND NOT absent.
