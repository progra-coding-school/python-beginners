# Program Code: LP-UN-02
# Title: How the for Loop Works Internally
# Cognitive Skill: Understanding
# Topic: Loops in Python

# A for loop picks each item from a sequence one by one.
# Python does this automatically — let's trace it step by step.

print("=== Tracing a for loop ===")
colours = ["red", "green", "blue"]

# What Python does internally:
# Iteration 1: colour = "red"  → run body
# Iteration 2: colour = "green" → run body
# Iteration 3: colour = "blue" → run body
# No more items → stop

for colour in colours:
    print(f"  colour = '{colour}'  → running body...")

print()

# --- How range() works ---
print("=== range() breakdown ===")
print("range(5)       →", list(range(5)))       # [0,1,2,3,4]
print("range(1, 6)    →", list(range(1, 6)))     # [1,2,3,4,5]
print("range(0,10,2)  →", list(range(0, 10, 2))) # [0,2,4,6,8]
print("range(10,0,-1) →", list(range(10, 0, -1)))# [10,9,...,1]

print()

# --- Loop variable is overwritten each iteration ---
print("=== Loop variable changes each iteration ===")
total = 0
for num in [10, 20, 30, 40]:
    print(f"  Before: total={total}, num={num}")
    total += num
    print(f"  After:  total={total}")
print("Final total:", total)

print()

# --- Nested loops: inner completes fully before outer moves ---
print("=== Nested loop order ===")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"  row={row}, col={col}")

print()

# --- Loop over string: character by character ---
print("=== Loop over a string ===")
word = "PYTHON"
for i, ch in enumerate(word):
    print(f"  Index {i} → '{ch}'")

# Think:
# 1. What does range(5, 0, -1) produce? Trace it without running.
# 2. If the outer loop runs 3 times and the inner loop runs 4 times,
#    how many total iterations happen?
