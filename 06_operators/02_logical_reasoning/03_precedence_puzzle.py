# Program Code: OP-LR-03
# Title: Precedence Puzzle
# Cognitive Skill: Logical Reasoning (Sequential Reasoning)
# Topic: Operators in Python

# Solve each expression step by step using BODMAS.
# Bracket → Exponent → Division/Multiplication → Addition/Subtraction

score = 0

print("=== Precedence Puzzle ===")
print("Solve step by step. BODMAS applies!")
print()

# --- Puzzle 1 ---
print("Puzzle 1: 3 + 4 * 2")
print("  Step 1: ___")
print("  Step 2: ___")
answer = input("Final answer: ")
if answer.strip() == "11":
    print("Correct! Step 1: 4*2=8. Step 2: 3+8=11")
    score += 1
else:
    print("Answer: 11. Step 1: 4*2=8. Step 2: 3+8=11")
print()

# --- Puzzle 2 ---
print("Puzzle 2: (3 + 4) * 2")
answer = input("Final answer: ")
if answer.strip() == "14":
    print("Correct! Brackets first: (3+4)=7, then 7*2=14")
    score += 1
else:
    print("Answer: 14. Brackets first: (3+4)=7, then 7*2=14")
print()

# --- Puzzle 3 ---
print("Puzzle 3: 2 ** 3 * 2")
answer = input("Final answer: ")
if answer.strip() == "16":
    print("Correct! Exponent first: 2**3=8, then 8*2=16")
    score += 1
else:
    print("Answer: 16. Exponent first: 2**3=8, then 8*2=16")
print()

# --- Puzzle 4 ---
print("Puzzle 4: 20 - 10 / 2 + 3")
answer = input("Final answer: ")
if answer.strip() in ["18", "18.0"]:
    print("Correct! Division first: 10/2=5.0. Then left-right: 20-5.0+3=18.0")
    score += 1
else:
    print("Answer: 18.0. Division first: 10/2=5.0. Then: 20-5.0+3=18.0")
print()

# --- Puzzle 5 ---
print("Puzzle 5: (5 + 3) ** 2 // 4")
answer = input("Final answer: ")
if answer.strip() == "16":
    print("Correct! (5+3)=8, then 8**2=64, then 64//4=16")
    score += 1
else:
    print("Answer: 16. (5+3)=8, then 8**2=64, then 64//4=16")
print()

# Verify all answers with Python
print("--- Python Verification ---")
print("3 + 4 * 2 =", 3 + 4 * 2)
print("(3 + 4) * 2 =", (3 + 4) * 2)
print("2 ** 3 * 2 =", 2 ** 3 * 2)
print("20 - 10 / 2 + 3 =", 20 - 10 / 2 + 3)
print("(5 + 3) ** 2 // 4 =", (5 + 3) ** 2 // 4)

print(f"\nScore: {score} / 5")
