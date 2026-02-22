# Program Code: LP-LR-02
# Title: Count the Iterations
# Cognitive Skill: Logical Reasoning (Pattern Finding)
# Topic: Loops in Python

# How many times does each loop run?
# Count carefully — off-by-one errors are the most common loop mistake!

score = 0

print("=== Count the Iterations ===")
print("How many times does the loop body run?")
print()

# --- Q1 ---
print("Q1: for i in range(5):")
answer = input("Iterations: ")
print("Answer: 5  (0, 1, 2, 3, 4 → 5 values)")
if answer.strip() == "5": score += 1
print()

# --- Q2 ---
print("Q2: for i in range(1, 6):")
answer = input("Iterations: ")
print("Answer: 5  (1, 2, 3, 4, 5 → 5 values, stop is excluded)")
if answer.strip() == "5": score += 1
print()

# --- Q3 ---
print("Q3: for i in range(0, 10, 2):")
answer = input("Iterations: ")
print("Answer: 5  (0, 2, 4, 6, 8 → 5 values)")
if answer.strip() == "5": score += 1
print()

# --- Q4 ---
print("Q4: for i in range(10, 0, -1):")
answer = input("Iterations: ")
print("Answer: 10  (10, 9, 8, ... 1 → 10 values)")
if answer.strip() == "10": score += 1
print()

# --- Q5 ---
print("Q5:")
print("  n = 1")
print("  while n < 20:")
print("      n *= 2")
answer = input("Iterations (trace n: 1→2→4→8→16→32 stops when n>=20): ")
print("Answer: 5  (1→2→4→8→16→32 — loop runs 5 times, stops at 32>=20)")
if answer.strip() == "5": score += 1
print()

# --- Q6 ---
print("Q6: Nested loop — how many total iterations of the INNER loop?")
print("  for i in range(3):")
print("      for j in range(4):")
print("          print(i, j)    ← count this line")
answer = input("Total inner iterations: ")
print("Answer: 12  (outer runs 3 times × inner runs 4 times = 12)")
if answer.strip() == "12": score += 1
print()

# --- Q7 ---
print("Q7: Loop with break — how many times does print run?")
print("  for i in range(10):")
print("      if i == 4:")
print("          break")
print("      print(i)")
answer = input("Iterations before break: ")
print("Answer: 4  (i=0,1,2,3 → prints 4 times, then i=4 breaks)")
if answer.strip() == "4": score += 1
print()

print(f"Score: {score} / 7")
print()
print("Quick formula: range(start, stop, step) → (stop - start) / step iterations")
