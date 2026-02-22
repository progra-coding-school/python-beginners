# Program Code: OP-CT-01
# Title: Spot the Bug — Operators
# Cognitive Skill: Critical Thinking (Bug Spotting)
# Topic: Operators in Python

# Each program below has a bug related to operators.
# Find the bug, explain why it's wrong, and fix it.

score = 0

# --- Bug 1 ---
print("=== Bug 1 ===")
print("""
  # Check if a student passed (marks >= 35)
  marks = 72
  if marks = 35:
      print("Passed")
""")
answer = input("What is the bug? ")
print("Bug: Used = (assignment) instead of == (comparison) inside if!")
print("Fix: if marks == 35:  ← but this checks exact 35, should be >= 35")
print("Correct: if marks >= 35:")
print()

# --- Bug 2 ---
print("=== Bug 2 ===")
print("""
  # Split Rs.100 equally among 3 friends
  money = 100
  friends = 3
  each_gets = money / friends
  print("Each gets Rs.", each_gets)
  # Output: Each gets Rs. 33.333...
  # (They can't split Rs.0.33!)
""")
answer = input("What operator should be used instead? ")
print("Bug: / gives 33.333... — you can't split a decimal rupee!")
print("Fix: Use // (floor division): 100 // 3 = 33")
print("Bonus: 100 % 3 = 1 (Rs.1 is leftover — who keeps it?)")
print()

# --- Bug 3 ---
print("=== Bug 3 ===")
print("""
  # Check if number is even
  number = 8
  if number % 2 = 0:
      print("Even")
""")
answer = input("What are the TWO bugs here? ")
print("Bug 1: = should be == in the condition (assignment vs comparison)")
print("Bug 2: (actually this only has 1 bug — good eye if you spotted just one!)")
print("Fix: if number % 2 == 0:")
print()

# --- Bug 4 ---
print("=== Bug 4 ===")
print("""
  # Calculate total cost with 10% discount
  price = 200
  discount = price * 10 / 100     # 10% of 200
  final = price - discount
  print("Final price:", final)
  # This works, but there's a better way. What's a common MISTAKE here?
""")
answer = input("What could go wrong with this approach? ")
print("Common mistake: Writing price * 10/100 without brackets.")
print("  price * 10 / 100 = (price * 10) / 100 = 2000 / 100 = 20.0 ✓")
print("  But some write: price * (10/100) — same result here, but risky with integers.")
print("Best practice: discount = price * 0.1  OR  (price * 10) // 100")
print()

print(f"Critical Thinking complete!")
print("Remember: = assigns, == compares. / gives float, // gives int.")
