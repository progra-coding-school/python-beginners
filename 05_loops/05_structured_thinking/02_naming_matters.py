# Program Code: LP-ST-02
# Title: Naming Matters — Loop Variables
# Cognitive Skill: Structured Thinking (Naming Conventions)
# Topic: Loops in Python

# Good loop variable names make code self-explanatory.
# Bad names make it impossible to understand.

# --- Example 1: Iterating over a list ---

# BAD — 'x' tells you nothing
fruits = ["mango", "banana", "apple"]
for x in fruits:
    print(x)

# GOOD — 'fruit' makes it clear you're handling ONE fruit per iteration
for fruit in fruits:
    print(fruit)

print()

# --- Example 2: Range-based counting ---

# BAD — what does 'i' represent here?
for i in range(1, 6):
    print(i * 120)

# GOOD — 'month_number' is clear
for month_number in range(1, 6):
    monthly_saving = month_number * 120
    print(f"Month {month_number}: Rs.{monthly_saving} saved")

print()

# --- Example 3: Nested loops ---

# BAD — i and j give no context
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

print()

# GOOD — row and column describe what's happening
for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row},{column})", end=" ")
    print()

print()

# --- Example 4: Accumulator variable ---

marks = [85, 72, 90, 65, 88]

# BAD
t = 0
for m in marks:
    t += m
print("t:", t)

# GOOD
total_marks = 0
for mark in marks:
    total_marks += mark
average_marks = total_marks / len(marks)
print(f"Total: {total_marks}, Average: {average_marks:.1f}")

print()

# --- Golden Rules ---
print("=== Loop Naming Rules ===")
print("1. Loop variable = singular of the list name")
print("   for student in students:")
print("   for mark in marks:")
print("   for product in products:")
print()
print("2. Range loops: name describes what the number REPRESENTS")
print("   for day_number in range(1, 31):")
print("   for attempt in range(1, 4):")
print()
print("3. Nested loops: row/column, outer/inner, i/j ONLY if truly generic")
print()
print("4. Accumulators: total_, count_, sum_, max_, min_ prefix")
print("   total_marks, pass_count, max_score")

# Think:
# 1. Rename: for a in b: c += a (b is a list of prices)
# 2. What would you name the loop variable when looping through a list of cities?
