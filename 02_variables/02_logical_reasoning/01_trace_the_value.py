# Program Code: CS-LR-01
# Title: Trace the Value - Guess the Output Game
# Cognitive Skill: Logical Reasoning (Tracing variable state)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav and Diya are playing with marbles.
# They keep giving marbles to each other!
# Can you trace (follow) the values step by step
# and PREDICT what each variable holds at the end?
# ============================================================

# ------------------------------------------------------------
# HOW TO PLAY:
# 1. Read the variable assignments carefully
# 2. Track the value in your head step by step
# 3. PREDICT the answer before the program reveals it
# 4. Check if you were right!
# ------------------------------------------------------------

score = 0

print("=== Trace the Value Game ===")
print("Follow the variables step by step.")
print("Predict the value BEFORE the answer is revealed!")
print()

# ----- ROUND 1 (Easy) -----
print("--- Round 1 ---")
print("  marbles = 10")
print("  marbles = marbles + 5")
print()
# The actual code:
marbles = 10
marbles = marbles + 5
guess = int(input("What is the value of marbles? : "))
print(f"Answer: marbles = {marbles}")
if guess == marbles:
    print("Correct!")
    score = score + 1
else:
    print(f"Not quite! Let's trace: 10 + 5 = {marbles}")
print()

# ----- ROUND 2 (Medium) -----
print("--- Round 2 ---")
print("  aarav_marbles = 8")
print("  diya_marbles = 5")
print("  aarav_marbles = aarav_marbles + diya_marbles")
print()
aarav_marbles = 8
diya_marbles = 5
aarav_marbles = aarav_marbles + diya_marbles
guess = int(input("What is the value of aarav_marbles? : "))
print(f"Answer: aarav_marbles = {aarav_marbles}")
if guess == aarav_marbles:
    print("Correct!")
    score = score + 1
else:
    print(f"Not quite! Trace: 8 + 5 = {aarav_marbles}")
print()

# ----- ROUND 3 (Tricky - value changes twice!) -----
print("--- Round 3 ---")
print("  sweets = 20")
print("  sweets = sweets - 7")
print("  sweets = sweets + 3")
print()
sweets = 20
sweets = sweets - 7
sweets = sweets + 3
guess = int(input("What is the value of sweets? : "))
print(f"Answer: sweets = {sweets}")
if guess == sweets:
    print("Correct!")
    score = score + 1
else:
    print(f"Not quite! Trace: 20 - 7 = 13, then 13 + 3 = {sweets}")
print()

# ----- ROUND 4 (Two variables changing) -----
print("--- Round 4 ---")
print("  a = 10")
print("  b = 3")
print("  a = a - b")
print("  b = b + b")
print()
a = 10
b = 3
a = a - b
b = b + b
guess_a = int(input("What is the value of a? : "))
guess_b = int(input("What is the value of b? : "))
print(f"Answer: a = {a}, b = {b}")
if guess_a == a and guess_b == b:
    print("Both correct! Amazing!")
    score = score + 2
elif guess_a == a or guess_b == b:
    print("One correct! Trace carefully:")
    print(f"  a = 10 - 3 = {a}")
    print(f"  b = 3 + 3 = {b}")
    score = score + 1
else:
    print(f"Let's trace together:")
    print(f"  a = 10 - 3 = {a}")
    print(f"  b = 3 + 3 = {b}")
print()

# ----- ROUND 5 (Hard - reassignment!) -----
print("--- Round 5 ---")
print("  x = 5")
print("  y = x")
print("  x = 20")
print()
x = 5
y = x
x = 20
guess = int(input("What is the value of y? : "))
print(f"Answer: y = {y}")
if guess == y:
    print("Excellent! You understood that y got the VALUE of x (5),")
    print("not a permanent link to x!")
    score = score + 1
else:
    print("Tricky! When we wrote y = x, y got the VALUE 5.")
    print("Later changing x to 20 does NOT change y!")
    print(f"So y is still {y}")
print()

# Final Score
print("=" * 35)
print(f"YOUR SCORE: {score} / 6")
print("=" * 35)

# ============================================================
# REFLECTION PROMPTS:
# 1. In Round 5, why did y stay as 5 even after x changed to 20?
# 2. When you trace a variable, what do you do in your head?
#    (Hint: You follow the steps one by one, like following
#    a recipe step by step)
# 3. Why is tracing important for programmers?
#    What happens if you skip a step?
# ============================================================
