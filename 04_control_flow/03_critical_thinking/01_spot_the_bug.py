# Program Code: CF-CT-01
# Title: Spot the Bug — Control Flow Errors
# Cognitive Skill: Critical Thinking (Finding logic errors)
# Topic: Control Flow in Python

score = 0

# Bug 1
print("--- Bug 1 ---")
print("  marks = 85")
print("  if marks = 85:      # supposed to check if marks equals 85")
print("      print('Good')")
answer = input("What is the bug? ")
print("Bug: = is assignment, not comparison. Use == for comparison.")
print("Fix: if marks == 85:")
score += 1
input("Press Enter for Bug 2...")

# Bug 2
print("--- Bug 2 ---")
print("  count = 0")
print("  while count < 5:")
print("      print(count)")
print("  # Expected: prints 0 1 2 3 4")
answer = input("What is the bug? ")
print("Bug: count is never incremented → INFINITE LOOP!")
print("Fix: add    count += 1    inside the while block.")
score += 1
input("Press Enter for Bug 3...")

# Bug 3
print("--- Bug 3 ---")
print("  score = 72")
print("  if score >= 35:")
print("      print('Pass')")
print("  if score >= 60:")
print("      print('Merit')")
print("  if score >= 75:")
print("      print('Distinction')")
answer = input("What prints for score = 72? How many lines? ")
print("Prints: 'Pass' AND 'Merit' — both! Each is a separate if.")
print("Bug: should use if-elif-else so only one branch executes.")
score += 1
input("Press Enter for Bug 4...")

# Bug 4
print("--- Bug 4 ---")
print("  for i in range(1, 5):")
print("      print(i)")
print("  print('Total:', total)   # expects sum of 1+2+3+4")
answer = input("What is the bug? ")
print("Bug: 'total' was never created or accumulated inside the loop.")
print("Fix: total = 0 before loop, then    total += i    inside the loop.")
score += 1
input("Press Enter for Bug 5...")

# Bug 5
print("--- Bug 5 ---")
print("  for i in range(10):")
print("      if i == 5:")
print("          print('Found 5!')")
print("      break")
answer = input("What is the bug? ")
print("Bug: break is NOT indented under the if — it always breaks on i=0!")
print("Fix: indent 'break' to be inside the 'if i == 5:' block.")
score += 1

print(f"\nBugs found: {score} / 5")

# Think:
# 1. Why is an infinite loop dangerous?
# 2. Bug 3 used separate 'if' instead of 'elif'. When would separate 'if' be the correct choice?
