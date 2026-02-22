# Program Code: VAR-FC-01
# Title: Spot the Difference
# Cognitive Skill: Focus and Concentration (Attention to detail)
# Topic: Variables in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("  Code A: marks = 95")
print("  Code B: marks = 85")
answer = input("What is different? ")
print("Answer: marks is 95 in A but 85 in B.")
score = score + 1

# Round 2
print("--- Round 2 ---")
print("  Code A: total = price * quantity")
print("  Code B: total = prize * quantity")
answer = input("What is different? ")
print("Answer: 'price' vs 'prize' — one wrong letter causes a crash!")
score = score + 1

# Round 3
print("--- Round 3 ---")
print("  Code A: result = a + b")
print("  Code B: result = a - b")
answer = input("What is different? ")
print("Answer: + vs - . Result changes from 13 to 7.")
score = score + 1

# Round 4
print("--- Round 4 ---")
print('  Code A: city = "Chennai"')
print('  Code B: city = "Chennai "')
answer = input("What is different? (Look very carefully!) ")
print('Answer: Code B has an extra space inside the quotes.')
print("That invisible space can cause bugs in comparisons.")
score = score + 1

# Round 5
print("--- Round 5 ---")
print("  Code A: area = length * width")
print("  Code B: area = length * length")
answer = input("What is different? ")
print("Answer: Code B uses 'length' twice instead of 'length * width'.")
print("It calculates a square instead of a rectangle.")
score = score + 1

# Round 6
print("--- Round 6 ---")
print('  Code A: greeting = "Vanakkam"')
print('  Code B: greeting = "Vanakam"')
answer = input("What is different? (Count the letters!) ")
print('Answer: "Vanakkam" (double k) vs "Vanakam" (single k).')
score = score + 1

# Round 7
print("--- Round 7 (Challenge) ---")
print("  Code A: score = score + bonus")
print("  Code B: score + bonus")
answer = input("What is different? ")
print("Answer: Code A stores the result (score = score + bonus).")
print("Code B only calculates but does NOT store. Score stays unchanged!")
score = score + 1

print("Score:", score, "/ 7")
