# Program Code: LP-LR-01
# Title: Trace the Loop
# Cognitive Skill: Logical Reasoning (Tracing)
# Topic: Loops in Python

# Read each loop carefully. Predict the output BEFORE running.
# Trace iteration by iteration — follow each variable.

score = 0

# --- Round 1 ---
print("Round 1: What is printed?")
print("""
  for i in range(1, 5):
      print(i * 2)
""")
answer = input("Write the output (one per line, separate with commas): ")
actual = [str(i * 2) for i in range(1, 5)]
print("Answer:", ", ".join(actual))
if answer.strip().replace(" ", "") == ",".join(actual):
    score += 1
    print("Correct!")
print()

# --- Round 2 ---
print("Round 2: What is the final value of total?")
print("""
  total = 0
  for n in [3, 7, 2, 8]:
      total += n
  print(total)
""")
answer = input("Your answer: ")
actual = 0
for n in [3, 7, 2, 8]: actual += n
print(f"Answer: {actual}  (3+7=10, +2=12, +8=20)")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

# --- Round 3 ---
print("Round 3: How many times does 'Hi' print?")
print("""
  for i in range(2):
      for j in range(3):
          print("Hi")
""")
answer = input("Your answer: ")
print("Answer: 6  (outer runs 2 times × inner runs 3 times = 6)")
if answer.strip() == "6":
    score += 1
    print("Correct!")
print()

# --- Round 4 ---
print("Round 4: What is printed?")
print("""
  count = 10
  while count > 0:
      print(count)
      count -= 3
""")
answer = input("Write the output (separate with commas): ")
result = []
count = 10
while count > 0:
    result.append(str(count))
    count -= 3
print("Answer:", ", ".join(result))
if answer.strip().replace(" ", "") == ",".join(result):
    score += 1
    print("Correct!")
print()

# --- Round 5 ---
print("Round 5: What is printed?")
print("""
  for i in range(1, 8):
      if i % 3 == 0:
          print(i)
""")
answer = input("Write the output: ")
result = [str(i) for i in range(1, 8) if i % 3 == 0]
print("Answer:", ", ".join(result), " (multiples of 3 between 1 and 7)")
if answer.strip().replace(" ", "") == ",".join(result):
    score += 1
    print("Correct!")
print()

print(f"Tracing Score: {score} / 5")
