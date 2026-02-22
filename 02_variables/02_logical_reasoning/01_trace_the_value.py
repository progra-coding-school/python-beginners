# Program Code: VAR-LR-01
# Title: Trace the Value
# Cognitive Skill: Logical Reasoning (Tracing variable state)
# Topic: Variables in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("marbles = 10")
print("marbles = marbles + 5")
marbles = 10
marbles = marbles + 5
guess = int(input("What is marbles? "))
print("Answer:", marbles)
if guess == marbles:
    print("Correct!")
    score = score + 1
else:
    print("Trace: 10 + 5 =", marbles)

# Round 2
print("--- Round 2 ---")
print("aarav = 8")
print("diya  = 5")
print("aarav = aarav + diya")
aarav_marbles = 8
diya_marbles = 5
aarav_marbles = aarav_marbles + diya_marbles
guess = int(input("What is aarav_marbles? "))
print("Answer:", aarav_marbles)
if guess == aarav_marbles:
    print("Correct!")
    score = score + 1
else:
    print("Trace: 8 + 5 =", aarav_marbles)

# Round 3
print("--- Round 3 ---")
print("sweets = 20")
print("sweets = sweets - 7")
print("sweets = sweets + 3")
sweets = 20
sweets = sweets - 7
sweets = sweets + 3
guess = int(input("What is sweets? "))
print("Answer:", sweets)
if guess == sweets:
    print("Correct!")
    score = score + 1
else:
    print("Trace: 20 - 7 = 13, then 13 + 3 =", sweets)

# Round 4
print("--- Round 4 ---")
print("a = 10, b = 3")
print("a = a - b")
print("b = b + b")
a = 10
b = 3
a = a - b
b = b + b
guess_a = int(input("What is a? "))
guess_b = int(input("What is b? "))
print("Answer: a =", a, "  b =", b)
if guess_a == a and guess_b == b:
    score = score + 2
    print("Both correct!")
elif guess_a == a or guess_b == b:
    score = score + 1
    print("One correct!")

# Round 5 — tricky!
print("--- Round 5 ---")
print("x = 5")
print("y = x")
print("x = 20")
x = 5
y = x
x = 20
guess = int(input("What is y? "))
print("Answer:", y)
if guess == y:
    print("Correct! y got the VALUE 5, not a link to x.")
    score = score + 1
else:
    print("y got 5 from x. Changing x later does NOT change y.")

print("Score:", score, "/ 6")
