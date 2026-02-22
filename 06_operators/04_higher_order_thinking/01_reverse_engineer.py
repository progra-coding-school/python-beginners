# Program Code: OP-HOT-01
# Title: Reverse Engineer — Find the Expression
# Cognitive Skill: Higher Order Thinking (Reverse Engineering)
# Topic: Operators in Python

# Given the INPUTS and OUTPUT — figure out the EXPRESSION used.
# Work backwards like a detective!

score = 0

print("=== Reverse Engineer ===")
print("Given the inputs and output — what expression produced it?")
print()

# --- Challenge 1 ---
print("Challenge 1:")
print("  a = 9,  b = 4")
print("  result = 1")
print("  Hint: result is less than both a and b")
answer = input("What expression? (use a, b, and an operator): ")
if answer.strip() in ["a % b", "9 % 4"]:
    print("Correct! 9 % 4 = 1 (remainder when 9 is divided by 4)")
    score += 1
else:
    print("Answer: a % b  →  9 % 4 = 1")
print()

# --- Challenge 2 ---
print("Challenge 2:")
print("  a = 3,  b = 4")
print("  result = 81")
print("  Hint: result is much bigger than a * b = 12")
answer = input("What expression? ")
if answer.strip() in ["a ** b", "3 ** 4"]:
    print("Correct! 3 ** 4 = 81 (3 to the power 4)")
    score += 1
else:
    print("Answer: a ** b  →  3 ** 4 = 3×3×3×3 = 81")
print()

# --- Challenge 3 ---
print("Challenge 3:")
print("  marks = 87")
print("  result = True")
print("  Hint: it's checking if marks qualify for distinction")
answer = input("What comparison expression? ")
correct_answers = ["marks >= 80", "marks > 79", "marks >= 75", "marks > 86"]
if any(a in answer.strip() for a in ["marks >= 80", "marks > 79", "marks >= 75", "marks > 86"]):
    print("Correct! e.g., marks >= 80 → 87 >= 80 → True")
    score += 1
else:
    print("Answer: marks >= 80  →  87 >= 80 → True")
print()

# --- Challenge 4 ---
print("Challenge 4:")
print("  total = 250,  subjects = 5")
print("  result = 50")
print("  Hint: result is equal for every subject")
answer = input("What expression? ")
if answer.strip() in ["total // subjects", "total / subjects"]:
    print("Correct! 250 // 5 = 50 (per subject average)")
    score += 1
else:
    print("Answer: total // subjects  →  250 // 5 = 50")
print()

# --- Challenge 5 ---
print("Challenge 5:")
print("  age = 16,  has_license = False")
print("  result = False")
print("  Hint: BOTH must be true to drive")
answer = input("What logical expression? ")
if "and" in answer.strip():
    print("Correct! age >= 18 and has_license → False and False → False")
    score += 1
else:
    print("Answer: age >= 18 and has_license  →  False and False → False")
print()

print(f"Score: {score} / 5")
