# Program Code: LP-LR-03
# Title: Loop Pattern Detective
# Cognitive Skill: Logical Reasoning (Sequential Reasoning)
# Topic: Loops in Python

# Given the OUTPUT — figure out what LOOP produced it.
# Work backwards like a detective!

score = 0

print("=== Loop Pattern Detective ===")
print("Given the output — identify the loop that produced it.")
print()

# --- Clue 1 ---
print("Clue 1 — Output:")
print("  1")
print("  4")
print("  9")
print("  16")
print("  25")
answer = input("What loop produced this? ")
print("Answer: for i in range(1, 6): print(i * i)  → squares of 1 to 5")
if "i * i" in answer or "i**2" in answer or "square" in answer.lower():
    score += 1
print()

# --- Clue 2 ---
print("Clue 2 — Output:")
print("  10  8  6  4  2")
answer = input("What loop produced this (one line)? ")
print("Answer: for i in range(10, 0, -2): print(i, end='  ')")
if "range" in answer and ("-2" in answer or "step" in answer.lower()):
    score += 1
print()

# --- Clue 3 ---
print("Clue 3 — Output (stars):")
print("  *")
print("  **")
print("  ***")
print("  ****")
answer = input("What loop produced this? ")
print("Answer:")
print("  for i in range(1, 5):")
print("      print('*' * i)")
if "'*' * i" in answer or "star" in answer.lower() or "* i" in answer:
    score += 1
print()

# --- Clue 4 ---
print("Clue 4 — Output:")
print("  1 is odd")
print("  3 is odd")
print("  5 is odd")
print("  7 is odd")
print("  9 is odd")
answer = input("What loop produced this? ")
print("Answer: for i in range(1, 10, 2): print(i, 'is odd')")
if "range" in answer and ("2" in answer):
    score += 1
print()

# --- Clue 5 ---
print("Clue 5 — Output:")
print("  5")
print("  10")
print("  15")
print("  20")
print("  ...until 100")
answer = input("What loop produced this (multiples of 5)? ")
print("Answer: for i in range(5, 101, 5): print(i)")
print("  OR:   for i in range(1, 21): print(i * 5)")
if "5" in answer and "range" in answer:
    score += 1
print()

# Verify all answers by running them
print("--- Verification ---")
print("Clue 1:", [i*i for i in range(1, 6)])
print("Clue 2:", list(range(10, 0, -2)))
print("Clue 4:", list(range(1, 10, 2)))
print("Clue 5:", list(range(5, 101, 5)))
print()

print(f"Detective Score: {score} / 5")
