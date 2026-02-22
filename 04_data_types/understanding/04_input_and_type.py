# Program Code: DT-UN-04
# Title: Input Always Gives a String
# Cognitive Skill: Understanding
# Topic: Data Types in Python

# KEY FACT: input() ALWAYS returns a string — even when the user types a number.

# This causes problems when you try to do math:
# age = input("Enter your age: ")   # → "13" (string, not 13)
# next_year = age + 1               # → ERROR: can't add str and int

# THE FIX: wrap input() with int() or float()
age = int(input("Enter your age: "))
print("Next year you'll be:", age + 1)

# Use float() when decimals are expected
height = float(input("Enter your height in cm: "))
print("Height in metres:", round(height / 100, 2))

# What if user types text for an int? Python gives an error.
# That's okay — we'll handle that later with try/except.

# GOOD HABIT: always convert input for calculations
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Total: Rs.{total:.2f}")

# But for things like names, keep them as strings
name = input("Enter your name: ")
print("Hello,", name)

# Think:
# 1. What happens if you run int(input()) and type "hello"?
#    Try it and read the error message.
# 2. Write two lines of code that ask for a student's marks (0-100)
#    and print whether they passed (>=35) or failed.
