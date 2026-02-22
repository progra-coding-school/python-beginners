# Program Code: OP-KN-02
# Title: Arithmetic Operators
# Cognitive Skill: Knowledge
# Topic: Operators in Python

# Arithmetic operators perform mathematical calculations.

a = 17
b = 5

print("a =", a, "  b =", b)
print()

# + Addition
result = a + b
print("a + b =", result)       # 22

# - Subtraction
result = a - b
print("a - b =", result)       # 12

# * Multiplication
result = a * b
print("a * b =", result)       # 85

# / Division (always gives a float)
result = a / b
print("a / b =", result)       # 3.4

# // Floor Division (removes decimal part)
result = a // b
print("a // b =", result)      # 3

# % Modulo (gives the remainder)
result = a % b
print("a % b =", result)       # 2

# ** Exponentiation (power)
result = a ** b
print("a ** b =", result)      # 1419857 (17 to the power 5)

print()
# Real-life examples
price_per_pen = 12
quantity = 7
total = price_per_pen * quantity
print("7 pens at Rs.12 each → Total: Rs.", total)

total_marks = 450
subjects = 5
average = total_marks / subjects
print("450 marks in 5 subjects → Average:", average)

students = 47
groups = 5
per_group = students // groups
leftover = students % groups
print("47 students in 5 groups → Per group:", per_group, "Remaining:", leftover)

# Think:
# 1. What is the difference between / and //? Try 9/2 and 9//2.
# 2. What does 15 % 4 give? How do you check if a number is divisible by another?
