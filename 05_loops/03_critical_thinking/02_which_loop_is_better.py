# Program Code: LP-CT-02
# Title: Which Loop Is Better?
# Cognitive Skill: Critical Thinking (Approach Evaluation)
# Topic: Loops in Python

# Same problem — two loop approaches. Analyze which is better and WHY.

# --- Scenario 1: Print 1 to 10 ---
print("=== Scenario 1: Print numbers 1 to 10 ===")

print("Approach A (for):")
for i in range(1, 11):
    print(i, end=" ")
print()

print("Approach B (while):")
i = 1
while i <= 11:     # BUG! should be <= 10 — easy to get wrong
    print(i, end=" ")
    i += 1
print()

print("Better: A — for loop is cleaner, no risk of off-by-one in condition.")
print()

# --- Scenario 2: Keep asking until valid input ---
print("=== Scenario 2: Keep asking until valid age entered ===")

# Approach A (for — awkward, requires break)
print("Approach A (for — not ideal):")
for _ in range(100):     # fake "big" range
    age = int(input("  Enter age (1-120): "))
    if 1 <= age <= 120:
        print(f"  Valid age: {age}")
        break

# Approach B (while — natural fit)
print("Approach B (while — natural fit):")
while True:
    age = int(input("  Enter age (1-120): "))
    if 1 <= age <= 120:
        print(f"  Valid age: {age}")
        break
    print("  Invalid! Try again.")

print("Better: B — while True + break is the natural pattern for input validation.")
print()

# --- Scenario 3: Sum of a list ---
print("=== Scenario 3: Sum a list of numbers ===")

numbers = [10, 20, 30, 40, 50]

# Approach A: for loop with accumulator
total_a = 0
for n in numbers:
    total_a += n
print("Approach A (for + accumulator):", total_a)

# Approach B: while loop with index
total_b = 0
i = 0
while i < len(numbers):
    total_b += numbers[i]
    i += 1
print("Approach B (while + index):", total_b)

print("Better: A — for loop is cleaner when iterating over a known list.")
print()

# --- Decision Guide ---
print("=== Which to choose? ===")
print("for   → known count, known sequence, iterating a list")
print("while → unknown count, wait for condition, user input loops")
print("for + break → search and stop early")
print("while True + break → keep going until user/condition says stop")
