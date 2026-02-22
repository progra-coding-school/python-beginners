# Program Code: VAR-CT-01
# Title: Spot the Bug
# Cognitive Skill: Critical Thinking (Finding errors)
# Topic: Variables in Python

score = 0

# Bug 1
print("--- Bug 1 ---")
print("  print(greeting)")
print("  greeting = 'Vanakkam!'")
answer = input("What is the bug? ")
print("Bug: used greeting BEFORE creating it.")
print("Fix: create the variable first, then print.")
score = score + 1
input("Press Enter for Bug 2...")

# Bug 2
print("--- Bug 2 ---")
print("  student_name = 'Diya'")
print("  print(studnet_name)")
answer = input("What is the bug? ")
print("Bug: 'studnet_name' is a spelling mistake — should be 'student_name'.")
print("Python treats them as two different variables.")
score = score + 1
input("Press Enter for Bug 3...")

# Bug 3
print("--- Bug 3 ---")
print("  marks = 85")
print("  marks = 92")
print("  print('Maths:', marks)")
print("  print('Science:', marks)")
answer = input("What is the bug? ")
print("Bug: both subjects show 92. The value 85 was overwritten.")
print("Fix: use different variable names — maths_marks and science_marks.")
score = score + 1
input("Press Enter for Bug 4...")

# Bug 4
print("--- Bug 4 ---")
print("  age = input('Enter your age: ')")
print("  birth_year = 2025 - age")
answer = input("What is the bug? ")
print("Bug: input() gives a string. You cannot subtract a string from 2025.")
print("Fix: age = int(input('Enter your age: '))")
score = score + 1
input("Press Enter for Bug 5...")

# Bug 5
print("--- Bug 5 ---")
print("  price_per_item = 50")
print("  quantity = 3")
print("  discount = 10")
print("  total = price_per_item * quantity")
print("  final_price = total - price_per_item   # should subtract discount")
answer = input("What is the bug? ")
print("Bug: subtracting price_per_item (50) instead of discount (10).")
print("Fix: final_price = total - discount")
score = score + 1

print("Bugs found:", score, "/ 5")

# Think:
# 1. Which bug was hardest to spot? Why?
# 2. Bug 5 gave a wrong answer with no error. Why are silent bugs dangerous?
