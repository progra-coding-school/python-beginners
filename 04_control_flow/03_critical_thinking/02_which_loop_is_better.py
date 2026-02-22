# Program Code: CF-CT-02
# Title: Which Loop Is Better?
# Cognitive Skill: Critical Thinking (Evaluating choices)
# Topic: Control Flow in Python

print("=== Which Loop Is Better? ===\n")

# Scenario 1: Print marks for 5 students
print("--- Scenario 1: Print marks for 5 fixed students ---")
print("Option A: for loop")
print("  for mark in [88, 92, 74, 85, 79]:")
print("      print(mark)")
print("Option B: while loop")
print("  i = 0")
print("  marks = [88, 92, 74, 85, 79]")
print("  while i < 5:")
print("      print(marks[i])")
print("      i += 1")
print("Winner: for loop — simpler, no manual index tracking needed.")
input("Press Enter to continue...")

# Scenario 2: Keep asking until correct password
print("\n--- Scenario 2: Ask until correct password ---")
print("Option A: for loop (limited attempts)")
print("  for i in range(3):     # exactly 3 attempts")
print("      password = input('Password: ')")
print("      if password == 'python': break")
print("Option B: while loop (unlimited until correct)")
print("  while True:")
print("      password = input('Password: ')")
print("      if password == 'python': break")
print("Winner: while loop — you don't know how many tries the user needs.")
input("Press Enter to continue...")

# Scenario 3: Sum numbers 1 to 100 — live comparison
print("\n--- Scenario 3: Sum 1 to 100 ---")
total_for = 0
for i in range(1, 101):
    total_for += i

total_while = 0
i = 1
while i <= 100:
    total_while += i
    i += 1

print("For loop total:", total_for)
print("While loop total:", total_while)
print("Both give 5050. For is cleaner when bounds are known.")

# Think:
# 1. You're downloading a file — keep going until download is 100%. Which loop?
# 2. You're printing a 12-month report. Which loop and why?
