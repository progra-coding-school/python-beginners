# Program Code: LP-HOT-01
# Title: Reverse Engineer — Write the Loop
# Cognitive Skill: Higher Order Thinking (Reverse Engineering)
# Topic: Loops in Python

# Given the OUTPUT — write the loop that produces it.
# Work backwards!

score = 0

print("=== Reverse Engineer the Loop ===")
print()

# --- Challenge 1 ---
print("Challenge 1 — Output:")
print("  2  4  6  8  10")
answer = input("Write the loop: ")
print("Answer: for i in range(2, 11, 2): print(i, end='  ')")
if "range" in answer and "2" in answer:
    score += 1
# Verify:
print("Verified:", end=" ")
for i in range(2, 11, 2): print(i, end="  ")
print()
print()

# --- Challenge 2 ---
print("Challenge 2 — Output:")
print("  5")
print("  4")
print("  3")
print("  2")
print("  1")
print("  Blastoff!")
answer = input("Write the loop: ")
print("Answer:")
print("  for i in range(5, 0, -1):")
print("      print(i)")
print("  print('Blastoff!')")
if "range" in answer and "-1" in answer:
    score += 1
print()

# --- Challenge 3 ---
print("Challenge 3 — Output (pattern):")
print("  1")
print("  2  2")
print("  3  3  3")
print("  4  4  4  4")
answer = input("Write the nested loop: ")
print("Answer:")
print("  for i in range(1, 5):")
print("      print((str(i) + '  ') * i)")
if "for" in answer and "range" in answer:
    score += 1
# Verify:
for i in range(1, 5):
    print("  " + (str(i) + "  ") * i)
print()

# --- Challenge 4 ---
print("Challenge 4 — Output:")
print("  Total marks: 370")
print("  (from marks = [85, 72, 90, 65, 58])")
answer = input("Write the accumulator loop: ")
print("Answer:")
print("  total = 0")
print("  for mark in marks:")
print("      total += mark")
print("  print('Total marks:', total)")
if "total" in answer and "+=" in answer:
    score += 1
marks = [85, 72, 90, 65, 58]
total = 0
for mark in marks: total += mark
print("Verified total:", total)
print()

# --- Challenge 5 ---
print("Challenge 5 — Output:")
print("  Aarav: PASS")
print("  Diya: FAIL")
print("  Karthik: PASS")
print("  (marks = [72, 28, 85], names = ['Aarav', 'Diya', 'Karthik'])")
answer = input("Write the loop: ")
print("Answer:")
print("  for i in range(len(marks)):")
print("      result = 'PASS' if marks[i] >= 35 else 'FAIL'")
print("      print(names[i] + ': ' + result)")
if "for" in answer and ("pass" in answer.lower() or "35" in answer):
    score += 1
print()

print(f"Score: {score} / 5")
