# Program Code: OP-FC-01
# Title: Spot the Difference — Operators
# Cognitive Skill: Focus and Concentration (Attention to Detail)
# Topic: Operators in Python

# Look carefully at each pair of expressions.
# They look similar — but they produce DIFFERENT results!

score = 0

print("=== Spot the Difference ===")
print("Look carefully — what is different between Code A and Code B?")
print()

# --- Round 1 ---
print("Round 1:")
print("  Code A: 10 / 2")
print("  Code B: 10 // 2")
answer = input("What is different? ")
print("Answer: Code A gives 5.0 (float). Code B gives 5 (int).")
print("  / always returns a float. // returns an integer.")
score += 1
print()

# --- Round 2 ---
print("Round 2:")
print("  Code A: if marks = 90:")
print("  Code B: if marks == 90:")
answer = input("What is different? ")
print("Answer: Code A is a syntax ERROR — = is assignment, not comparison.")
print("  Code B is correct — == checks equality.")
score += 1
print()

# --- Round 3 ---
print("Round 3:")
print("  Code A: 2 ** 3 + 1")
print("  Code B: 2 ** (3 + 1)")
answer = input("What does each produce? ")
print(f"Answer: Code A = {2 ** 3 + 1} (exponent first: 8+1=9)")
print(f"         Code B = {2 ** (3 + 1)} (brackets first: 2^4=16)")
score += 1
print()

# --- Round 4 ---
print("Round 4:")
print("  Code A: age > 10 and age < 20")
print("  Code B: age > 10 or age < 20")
print("  (age = 25)")
answer = input("What does each return? ")
age = 25
print(f"Answer: Code A = {age > 10 and age < 20} (25 < 20 is False, so AND fails)")
print(f"         Code B = {age > 10 or age < 20} (25 > 10 is True, so OR passes)")
score += 1
print()

# --- Round 5 ---
print("Round 5:")
print("  Code A: 7 % 3")
print("  Code B: 7 // 3")
answer = input("What does each return? ")
print(f"Answer: Code A = {7 % 3} (remainder of 7÷3 = 1)")
print(f"         Code B = {7 // 3} (whole-number part of 7÷3 = 2)")
print("  % gives the LEFTOVER. // gives how many WHOLE TIMES it fits.")
score += 1
print()

# --- Round 6 ---
print("Round 6:")
print("  Code A: not True and False")
print("  Code B: not (True and False)")
answer = input("What does each return? ")
print(f"Answer: Code A = {not True and False} (not True = False, then False and False = False)")
print(f"         Code B = {not (True and False)} (True and False = False, then not False = True)")
print("  The brackets change EVERYTHING — precedence matters!")
score += 1
print()

print(f"Score: {score} / 6")
print("Great focus work! Operators differ by just one character — always read carefully.")
