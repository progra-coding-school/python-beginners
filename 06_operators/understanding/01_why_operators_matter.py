# Program Code: OP-UN-01
# Title: Why Operators Matter
# Cognitive Skill: Understanding
# Topic: Operators in Python

# Without operators, we can't do anything useful with data.
# Let's feel the difference.

# --- WITHOUT OPERATORS ---
# Imagine having marks but no way to calculate or compare them
maths = 85
science = 90
english = 78

# Without operators, we're stuck:
# We can't add, can't average, can't compare — just raw data.
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("(Without operators, this is all we can do — just display.)")

print()

# --- WITH ARITHMETIC OPERATORS ---
# Now we can calculate!
total = maths + science + english
average = total / 3
highest = max(maths, science, english)   # built-in function uses comparison internally

print("Total marks:", total)
print("Average:", average)
print("Highest:", highest)

print()

# --- WITH COMPARISON OPERATORS ---
# Now we can make decisions!
pass_mark = 35
if maths >= pass_mark and science >= pass_mark and english >= pass_mark:
    print("Result: PASS in all subjects")
else:
    print("Result: FAIL in at least one subject")

print()

# --- WITH LOGICAL OPERATORS ---
# Now we can combine conditions!
attendance = 88
eligible_for_exam = average >= 40 and attendance >= 75
print("Eligible for exam:", eligible_for_exam)

# Why % matters — check divisibility
students = 43
teams = 5
remainder = students % teams
print(f"\n{students} students in {teams} teams:")
print(f"  {students // teams} per team, {remainder} students left out")

# Think:
# 1. What would a shopping app be like without operators?
# 2. Name 3 decisions your phone makes that use comparison operators.
