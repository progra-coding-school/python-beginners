# Program Code: DT-FC-01
# Title: Spot the Type Difference
# Cognitive Skill: Focus and Concentration (Attention to detail)
# Topic: Data Types in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("  Code A: x = 10")
print("  Code B: x = 10.0")
answer = input("What is different? ")
print("Answer: A is int, B is float. Same value but different types!")
score += 1

# Round 2
print("--- Round 2 ---")
print("  Code A: result = 10 / 2")
print("  Code B: result = 10 // 2")
answer = input("What is different? ")
print("Answer: A gives 5.0 (float), B gives 5 (int). Different operators!")
score += 1

# Round 3
print("--- Round 3 ---")
print("  Code A: age = '15'")
print("  Code B: age = 15")
answer = input("What is different? ")
print("Answer: A is str (text), B is int (number). Quotes make it a string!")
score += 1

# Round 4
print("--- Round 4 ---")
print("  Code A: print(bool(0))")
print("  Code B: print(bool('0'))")
answer = input("What is different? (Look very carefully!) ")
print("Answer: A gives False (int 0), B gives True (non-empty string '0')!")
print("'0' as a string is NOT zero — it's a character, so it's True.")
score += 1

# Round 5
print("--- Round 5 ---")
print("  Code A: val = int(3.9)")
print("  Code B: val = round(3.9)")
answer = input("What is different? ")
print("Answer: A gives 3 (truncate), B gives 4 (round). Big difference!")
score += 1

# Round 6
print("--- Round 6 ---")
print("  Code A: name = 'Aarav '")
print('  Code B: name = "Aarav"')
answer = input("What is different? (Count characters!) ")
print("Answer: Code A has a trailing space inside the string. Invisible bug!")
score += 1

# Round 7 — Challenge
print("--- Round 7 (Challenge) ---")
print("  Code A: is_valid = True")
print("  Code B: is_valid = 'True'")
answer = input("What is different? ")
print("Answer: A is bool, B is str.")
print("bool(True) = True but 'True' is just text — a non-empty string.")
print("They behave differently in strict comparisons: True == 'True' is False!")
score += 1

print(f"\nScore: {score} / 7")
