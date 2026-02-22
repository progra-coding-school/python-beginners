# Program Code: OP-LR-02
# Title: Operator Detective
# Cognitive Skill: Logical Reasoning (Pattern Finding)
# Topic: Operators in Python

# Given the inputs and the output — figure out WHICH operator was used!

score = 0

print("=== Operator Detective ===")
print("Find the missing operator: +, -, *, /, //, %, **")
print()

# --- Clue 1 ---
print("Clue 1:")
print("  a = 10, b = 3")
print("  result = a ??? b")
print("  result = 1")
answer = input("Which operator? ")
if answer.strip() == "%":
    print("Correct! 10 % 3 = 1 (remainder of 10 ÷ 3)")
    score += 1
else:
    print("Answer: % (modulo). 10 % 3 = 1")
print()

# --- Clue 2 ---
print("Clue 2:")
print("  a = 10, b = 3")
print("  result = a ??? b")
print("  result = 3")
answer = input("Which operator? ")
if answer.strip() == "//":
    print("Correct! 10 // 3 = 3 (floor division removes decimal)")
    score += 1
else:
    print("Answer: // (floor division). 10 // 3 = 3")
print()

# --- Clue 3 ---
print("Clue 3:")
print("  a = 2, b = 8")
print("  result = a ??? b")
print("  result = 256")
answer = input("Which operator? ")
if answer.strip() == "**":
    print("Correct! 2 ** 8 = 256 (exponentiation)")
    score += 1
else:
    print("Answer: ** (exponent). 2 ** 8 = 256")
print()

# --- Clue 4 ---
print("Clue 4:")
print("  a = 15, b = 3")
print("  result = a ??? b")
print("  result = 5.0")
answer = input("Which operator? ")
if answer.strip() == "/":
    print("Correct! 15 / 3 = 5.0 (division always returns float)")
    score += 1
else:
    print("Answer: / (division). 15 / 3 = 5.0")
print()

# --- Clue 5 ---
print("Clue 5:")
print("  a = 100, b = 37")
print("  result = a ??? b")
print("  result = 63")
answer = input("Which operator? ")
if answer.strip() == "-":
    print("Correct! 100 - 37 = 63 (subtraction)")
    score += 1
else:
    print("Answer: - (subtraction). 100 - 37 = 63")
print()

print(f"Detective Score: {score} / 5")
