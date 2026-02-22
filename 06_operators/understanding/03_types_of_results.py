# Program Code: OP-UN-03
# Title: Types of Results — int, float, bool
# Cognitive Skill: Understanding
# Topic: Operators in Python

# Different operators give different types of results.
# Understanding this prevents bugs!

# --- ARITHMETIC → gives int or float ---
print("=== Arithmetic Result Types ===")
a = 10
b = 3

print(a + b, type(a + b))    # 13 → int
print(a - b, type(a - b))    # 7  → int
print(a * b, type(a * b))    # 30 → int
print(a / b, type(a / b))    # 3.333 → float (always float!)
print(a // b, type(a // b))  # 3  → int
print(a % b, type(a % b))    # 1  → int
print(a ** b, type(a ** b))  # 1000 → int

print()

# Important: / ALWAYS gives float, even if result is whole
print(10 / 2, type(10 / 2))   # 5.0 → float, NOT 5!
print(10 // 2, type(10 // 2)) # 5   → int

print()

# --- COMPARISON → always gives bool (True/False) ---
print("=== Comparison Result Types ===")
x = 7
print(x == 7, type(x == 7))   # True → bool
print(x > 10, type(x > 10))   # False → bool
print(x != 5, type(x != 5))   # True → bool

print()

# --- LOGICAL → always gives bool ---
print("=== Logical Result Types ===")
print(True and False, type(True and False))  # False → bool
print(True or False, type(True or False))    # True → bool
print(not True, type(not True))              # False → bool

print()

# Why does this matter?
marks = 85
grade = marks / 5         # 17.0 — float
level = marks // 10       # 8    — int (useful for grade lookup)
is_passed = marks >= 35   # True — bool

print("marks / 5 =", grade, "→ use for decimal averages")
print("marks // 10 =", level, "→ use for category/level")
print("marks >= 35 =", is_passed, "→ use in if-conditions")

# Think:
# 1. Why does 9/3 give 3.0 and not 3? When would this cause a problem?
# 2. Booleans (True/False) are actually 1 and 0. Try: print(True + True)
