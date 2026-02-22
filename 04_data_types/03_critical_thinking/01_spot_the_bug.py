# Program Code: DT-CT-01
# Title: Spot the Bug — Type Errors
# Cognitive Skill: Critical Thinking (Finding type errors)
# Topic: Data Types in Python

score = 0

# Bug 1
print("--- Bug 1 ---")
print("  age = input('Enter your age: ')")
print("  next_year = age + 1")
answer = input("What is the bug? ")
print("Bug: input() gives a string. You cannot add str + int.")
print("Fix: age = int(input('Enter your age: '))")
score += 1
input("Press Enter for Bug 2...")

# Bug 2
print("--- Bug 2 ---")
print("  price = '49.99'")
print("  total = price * 3")
answer = input("What is the bug? ")
print("Bug: price is a string. str * int repeats the string, not multiply!")
print("'49.99' * 3 = '49.9949.9949.99'")
print("Fix: price = float('49.99')  or  price = 49.99")
score += 1
input("Press Enter for Bug 3...")

# Bug 3
print("--- Bug 3 ---")
print("  name = 'Priya'")
print("  marks = 95")
print("  message = 'Hello ' + name + ', your marks: ' + marks")
answer = input("What is the bug? ")
print("Bug: cannot join str + int with +.")
print("Fix: use str(marks) or an f-string: f'Hello {name}, your marks: {marks}'")
score += 1
input("Press Enter for Bug 4...")

# Bug 4
print("--- Bug 4 ---")
print("  height = 165")
print("  height_in_m = height / 100")
print("  # Expected type: int,  Got: float")
answer = input("What is wrong with their expectation? ")
print("Bug: Division / always returns float in Python 3.")
print("165 / 100 = 1.65 (float). Use // for integer division.")
score += 1
input("Press Enter for Bug 5...")

# Bug 5
print("--- Bug 5 ---")
print("  x = int(7.9)")
print("  print('Rounded:', x)")
answer = input("What is wrong here? ")
print("Bug: int() does NOT round — it truncates (drops the decimal).")
print("int(7.9) = 7, NOT 8.")
print("Fix: use round(7.9) = 8 if rounding is needed.")
score += 1

print(f"\nBugs found: {score} / 5")

# Think:
# 1. Which bug was hardest to spot? Why?
# 2. Type errors in Python crash the program. How can you prevent them?
