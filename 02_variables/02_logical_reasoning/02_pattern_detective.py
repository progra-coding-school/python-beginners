# Program Code: CS-LR-02
# Title: Pattern Detective
# Cognitive Skill: Logical Reasoning (Induction - finding patterns)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Diya loves rangoli and kolam patterns!
# She noticed that numbers can have patterns too.
# Can you look at a sequence of numbers stored in variables
# and figure out the RULE (pattern) that connects them?
# Then predict the NEXT number!
# ============================================================

# ------------------------------------------------------------
# HOW TO PLAY:
# 1. Look at the values in the variables
# 2. Find the PATTERN (what rule connects them?)
# 3. Predict what the next variable should be
# 4. Check your answer!
# ------------------------------------------------------------

score = 0

print("=== Pattern Detective ===")
print("Find the hidden pattern and predict the next value!")
print()

# ----- PATTERN 1: Simple addition -----
print("--- Pattern 1 ---")
a = 2
b = 4
c = 6
d = 8
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = {c}")
print(f"  d = {d}")
print(f"  e = ?")
print()
guess = int(input("What should e be? : "))
e = 10  # Pattern: adding 2 each time
print(f"Answer: e = {e}")
if guess == e:
    print("Correct! Pattern: each number increases by 2")
    score = score + 1
else:
    print(f"The pattern: +2 each time. 2, 4, 6, 8, {e}")
print()

# ----- PATTERN 2: Multiplication -----
print("--- Pattern 2 ---")
a = 3
b = 9
c = 27
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = {c}")
print(f"  d = ?")
print()
guess = int(input("What should d be? : "))
d = 81  # Pattern: multiply by 3 each time
print(f"Answer: d = {d}")
if guess == d:
    print("Correct! Pattern: multiply by 3 each time")
    score = score + 1
else:
    print(f"The pattern: x3 each time. 3, 9, 27, {d}")
print()

# ----- PATTERN 3: Subtraction -----
print("--- Pattern 3 ---")
a = 100
b = 90
c = 80
d = 70
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = {c}")
print(f"  d = {d}")
print(f"  e = ?")
print()
guess = int(input("What should e be? : "))
e = 60  # Pattern: subtract 10 each time
print(f"Answer: e = {e}")
if guess == e:
    print("Correct! Pattern: subtract 10 each time")
    score = score + 1
else:
    print(f"The pattern: -10 each time. 100, 90, 80, 70, {e}")
print()

# ----- PATTERN 4: Doubling -----
print("--- Pattern 4 ---")
a = 1
b = 2
c = 4
d = 8
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = {c}")
print(f"  d = {d}")
print(f"  e = ?")
print()
guess = int(input("What should e be? : "))
e = 16  # Pattern: double each time
print(f"Answer: e = {e}")
if guess == e:
    print("Correct! Pattern: double (x2) each time")
    score = score + 1
else:
    print(f"The pattern: x2 each time. 1, 2, 4, 8, {e}")
print()

# ----- PATTERN 5: Squares! -----
print("--- Pattern 5 (Challenge!) ---")
a = 1
b = 4
c = 9
d = 16
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = {c}")
print(f"  d = {d}")
print(f"  e = ?")
print(f"  Hint: Think about 1x1, 2x2, 3x3...")
print()
guess = int(input("What should e be? : "))
e = 25  # Pattern: squares (1, 4, 9, 16, 25 = 1^2, 2^2, 3^2, 4^2, 5^2)
print(f"Answer: e = {e}")
if guess == e:
    print("Excellent! Pattern: square numbers! 1x1, 2x2, 3x3, 4x4, 5x5")
    score = score + 1
else:
    print(f"These are SQUARE numbers: 1x1=1, 2x2=4, 3x3=9, 4x4=16, 5x5={e}")
print()

# Final Score
print("=" * 35)
print(f"YOUR SCORE: {score} / 5")
print("=" * 35)

# ============================================================
# REFLECTION PROMPTS:
# 1. Which pattern was easiest to spot? Why?
# 2. When you find a pattern, how do you CHECK if it is correct?
#    (Hint: You test it on ALL the numbers, not just two)
# 3. Patterns are everywhere! Can you think of a pattern
#    in your daily life? (Hint: bus timings, class schedule,
#    rangoli designs)
# ============================================================
