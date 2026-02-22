# Program Code: LP-CT-01
# Title: Spot the Bug — Loops
# Cognitive Skill: Critical Thinking (Bug Spotting)
# Topic: Loops in Python

# Each snippet has a loop bug. Find it, explain why it's wrong, and fix it.

print("=== Bug 1: Infinite Loop ===")
print("""
  count = 1
  while count <= 5:
      print(count)
""")
answer = input("What is the bug? ")
print("Bug: count is never updated — it stays 1 forever → INFINITE LOOP!")
print("Fix: Add  count += 1  inside the loop body.")
print()

print("=== Bug 2: Off-by-One Error ===")
print("""
  # Print numbers 1 to 10
  for i in range(10):
      print(i)
""")
answer = input("What is the bug? ")
print("Bug: range(10) gives 0–9, not 1–10. Prints 0 too, misses 10.")
print("Fix: range(1, 11)  → 1 to 10 inclusive")
print()

print("=== Bug 3: Wrong Accumulator Start ===")
print("""
  marks = [80, 90, 70]
  total = marks[0]     # starts at 80, not 0!
  for mark in marks:
      total += mark
  print("Total:", total)
""")
answer = input("What is the bug? ")
print("Bug: total starts at marks[0]=80, then adds ALL marks including the first one.")
print(f"     Result: 80 + 80 + 90 + 70 = 320 — WRONG!")
print("Fix: total = 0  (accumulator always starts at 0)")
print()

print("=== Bug 4: Loop Not Reaching Target ===")
print("""
  # Print all multiples of 3 up to 30
  for i in range(3, 30, 3):
      print(i)
""")
answer = input("What is the bug? ")
print("Bug: range(3, 30, 3) stops before 30 — 30 is not included!")
print("     Last value printed: 27.")
print("Fix: range(3, 31, 3)  → includes 30")
print()

print("=== Bug 5: break in wrong place ===")
print("""
  # Find and print ALL items containing 'a'
  items = ["apple", "banana", "cherry", "mango"]
  for item in items:
      if 'a' in item:
          print(item)
          break
""")
answer = input("What is the bug? ")
print("Bug: break exits after the FIRST match — prints only 'apple', not banana/mango.")
print("Fix: Remove break. Let the loop continue to check all items.")
print()

print("Loop bugs: infinite loops, off-by-one errors, wrong start values, misplaced break.")
