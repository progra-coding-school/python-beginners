# Program Code: VAR-LR-02
# Title: Pattern Detective
# Cognitive Skill: Logical Reasoning (Finding patterns)
# Topic: Variables in Python

score = 0

# Pattern 1
print("--- Pattern 1 ---")
print("a=2, b=4, c=6, d=8, e=?")
guess = int(input("What is e? "))
e = 10
print("Answer:", e)
if guess == e:
    print("Correct! Pattern: +2 each time")
    score = score + 1
else:
    print("Pattern is +2 each time. 2, 4, 6, 8,", e)

# Pattern 2
print("--- Pattern 2 ---")
print("a=3, b=9, c=27, d=?")
guess = int(input("What is d? "))
d = 81
print("Answer:", d)
if guess == d:
    print("Correct! Pattern: x3 each time")
    score = score + 1
else:
    print("Pattern is x3 each time. 3, 9, 27,", d)

# Pattern 3
print("--- Pattern 3 ---")
print("a=100, b=90, c=80, d=70, e=?")
guess = int(input("What is e? "))
e = 60
print("Answer:", e)
if guess == e:
    print("Correct! Pattern: -10 each time")
    score = score + 1
else:
    print("Pattern is -10 each time. 100, 90, 80, 70,", e)

# Pattern 4
print("--- Pattern 4 ---")
print("a=1, b=2, c=4, d=8, e=?")
guess = int(input("What is e? "))
e = 16
print("Answer:", e)
if guess == e:
    print("Correct! Pattern: x2 each time")
    score = score + 1
else:
    print("Pattern is x2. 1, 2, 4, 8,", e)

# Pattern 5 — challenge
print("--- Pattern 5 (Challenge) ---")
print("a=1, b=4, c=9, d=16, e=?")
print("Hint: 1x1, 2x2, 3x3...")
guess = int(input("What is e? "))
e = 25
print("Answer:", e)
if guess == e:
    print("Correct! Square numbers: 1, 4, 9, 16, 25")
    score = score + 1
else:
    print("Square numbers: 1x1=1, 2x2=4, 3x3=9, 4x4=16, 5x5=", e)

print("Score:", score, "/ 5")
