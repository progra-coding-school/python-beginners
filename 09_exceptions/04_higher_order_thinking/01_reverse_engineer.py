# Program Code: EX-HOT-01
# Title: Reverse Engineer the Exception Handler
# Cognitive Skill: Higher Order Thinking
# Topic: Exceptions in Python

# Study the OUTPUT. Write the code that produced it.
# Then compare with the reference.

# --- Challenge 1 ---
# Output:
#   10 / 2 = 5.0
#   Cannot divide by zero
#   10 / 5 = 2.0

print("=== Challenge 1 ===")
print("Target output above ↑")
for b in [2, 0, 5]:
    try:
        print(f"  10 / {b} = {10/b:.1f}")
    except ZeroDivisionError:
        print("  Cannot divide by zero")

print()

# --- Challenge 2 ---
# Output:
#   '85' → 85
#   'abc' → invalid
#   '0' → 0
#   '3.5' → invalid

print("=== Challenge 2 ===")
print("Target: parse ints, label others 'invalid'")
inputs = ["85", "abc", "0", "3.5"]
for s in inputs:
    try:
        print(f"  '{s}' → {int(s)}")
    except ValueError:
        print(f"  '{s}' → invalid")

print()

# --- Challenge 3 ---
# Output:
#   Sum of valid numbers: 18
#   Skipped 2 invalid entries

print("=== Challenge 3 ===")
print("Target: sum valid numbers, count skipped")
data = ["5", "abc", "8", "?", "5"]
total   = 0
skipped = 0
for item in data:
    try:
        total += int(item)
    except ValueError:
        skipped += 1
print(f"  Sum of valid numbers: {total}")
print(f"  Skipped {skipped} invalid entries")

print()

# --- Challenge 4 ---
# Output:
#   Aarav's marks: 85
#   Riya's marks: Not found
#   try/except done

print("=== Challenge 4 ===")
print("Target: safe dict lookup with finally")
marks = {"Aarav": 85, "Diya": 92}
for name in ["Aarav", "Riya"]:
    try:
        print(f"  {name}'s marks: {marks[name]}")
    except KeyError:
        print(f"  {name}'s marks: Not found")
    finally:
        print("  try/except done")
    print()

# Think:
# 1. In Challenge 3, could you solve it with a list comprehension + if? Which is cleaner?
# 2. In Challenge 4, `finally` prints for every name. Is that a good design? Why or why not?
