# Program Code: OP-LR-01
# Title: Trace the Expression
# Cognitive Skill: Logical Reasoning (Tracing)
# Topic: Operators in Python

# Read each expression. Predict the output BEFORE running.
# Then check your answer!

score = 0

# --- Round 1 ---
print("Round 1: What is the output?")
print("  a = 15")
print("  b = 4")
print("  print(a + b * 2)")
answer = input("Your answer: ")
a = 15
b = 4
actual = a + b * 2
print(f"Actual output: {actual}")
print("Step: b*2 = 8 first (multiplication before addition), then 15+8 = 23")
if str(actual) == answer.strip():
    score += 1
    print("Correct!")
print()

# --- Round 2 ---
print("Round 2: What is the output?")
print("  x = 17")
print("  print(x % 5)")
answer = input("Your answer: ")
x = 17
actual = x % 5
print(f"Actual output: {actual}")
print("Step: 17 ÷ 5 = 3 remainder 2. So 17 % 5 = 2")
if str(actual) == answer.strip():
    score += 1
    print("Correct!")
print()

# --- Round 3 ---
print("Round 3: What is the output?")
print("  marks = 72")
print("  print(marks >= 70 and marks < 80)")
answer = input("Your answer (True/False): ")
marks = 72
actual = marks >= 70 and marks < 80
print(f"Actual output: {actual}")
print("Step: 72 >= 70 → True. 72 < 80 → True. True and True → True")
if answer.strip().lower() == str(actual).lower():
    score += 1
    print("Correct!")
print()

# --- Round 4 ---
print("Round 4: What is the output?")
print("  n = 20")
print("  print(n // 3 + n % 3)")
answer = input("Your answer: ")
n = 20
actual = n // 3 + n % 3
print(f"Actual output: {actual}")
print("Step: 20//3 = 6, 20%3 = 2, 6+2 = 8")
if str(actual) == answer.strip():
    score += 1
    print("Correct!")
print()

# --- Round 5 ---
print("Round 5: What is the output?")
print("  a = 5")
print("  print(not (a > 3 and a < 10))")
answer = input("Your answer (True/False): ")
a = 5
actual = not (a > 3 and a < 10)
print(f"Actual output: {actual}")
print("Step: 5>3 → True. 5<10 → True. True and True → True. not True → False")
if answer.strip().lower() == str(actual).lower():
    score += 1
    print("Correct!")
print()

print(f"Score: {score} / 5")
