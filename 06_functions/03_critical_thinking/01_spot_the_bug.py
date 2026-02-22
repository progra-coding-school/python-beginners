# Program Code: FN-CT-01
# Title: Spot the Bug — Functions
# Cognitive Skill: Critical Thinking (Bug Spotting)
# Topic: Functions in Python

# Each snippet below has a bug related to functions.
# Find it, explain why it's wrong, and fix it.

print("=== Bug 1 ===")
print("""
  def greet(name):
      print("Hello,", name)

  greet()
""")
answer = input("What is the bug? ")
print("Bug: greet() is called WITHOUT an argument, but the function needs 'name'.")
print("Fix: greet('Aarav')  ← provide the argument")
print()

print("=== Bug 2 ===")
print("""
  def add(a, b):
      result = a + b
      print(result)

  total = add(5, 10)
  doubled = total * 2
  print(doubled)
""")
answer = input("What is the bug? ")
print("Bug: add() uses print() instead of return.")
print("     So 'total' = None, and None * 2 causes a TypeError!")
print("Fix: Replace print(result) with return result")
print()

print("=== Bug 3 ===")
print("""
  def calculate_area(length, width):
      area = length * width

  result = calculate_area(5, 3)
  print("Area:", result)
""")
answer = input("What is the bug? ")
print("Bug: The function calculates area but DOESN'T return it.")
print("     result = None, so prints 'Area: None'")
print("Fix: Add 'return area' at the end of the function")
print()

print("=== Bug 4 ===")
print("""
  result = multiply(4, 5)
  print(result)

  def multiply(a, b):
      return a * b
""")
answer = input("What is the bug? ")
print("Bug: multiply() is CALLED before it's DEFINED.")
print("     Python reads top-to-bottom, so it doesn't know multiply yet!")
print("Fix: Always DEFINE functions BEFORE calling them.")
print()

print("=== Bug 5 ===")
print("""
  def get_grade(marks):
      if marks >= 80:
          return "A"
      elif marks >= 60:
          return "B"

  grade = get_grade(45)
  print(grade.upper())
""")
answer = input("What is the bug? ")
print("Bug: If marks < 60 (like 45), no return is hit → function returns None.")
print("     None.upper() causes AttributeError!")
print("Fix: Add 'else: return \"C\"' (or 'return \"F\"') to cover all cases.")
print()

print("Function bugs are often: missing return, wrong number of args, or calling before defining!")
