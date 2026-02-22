# Program Code: FN-ST-02
# Title: Naming Matters — Function Names
# Cognitive Skill: Structured Thinking (Naming Conventions)
# Topic: Functions in Python

# A good function name tells you EXACTLY what it does.
# Bad names make code unreadable and hard to fix.

# --- Example 1: Calculation functions ---

# BAD names
def f(a, b):
    return a + b

def g(x):
    return x * 0.10

def h(p, d):
    return p - d

# GOOD names
def calculate_total(price, quantity):
    return price * quantity

def calculate_discount(price):
    return price * 0.10

def apply_discount(price, discount):
    return price - discount

# Which is easier to read?
bad_result = h(f(120, 3), g(f(120, 3)))
good_result = apply_discount(
    calculate_total(120, 3),
    calculate_discount(calculate_total(120, 3))
)

print("Bad code result:", bad_result)
print("Good code result:", good_result)
print("Both are 324.0 — but only the good version EXPLAINS ITSELF!")
print()

# --- Example 2: Boolean functions ---

# BAD
def check(age):
    return age >= 18

# GOOD — start with is_, has_, can_
def is_adult(age):
    return age >= 18

def can_vote(age, is_citizen):
    return is_adult(age) and is_citizen

def has_passed(marks):
    return marks >= 35

print("is_adult(17):", is_adult(17))
print("can_vote(20, True):", can_vote(20, True))
print("has_passed(42):", has_passed(42))
print()

# --- Example 3: Display vs Calculate ---
# Functions that DISPLAY should start with: show_, print_, display_
# Functions that CALCULATE should start with: get_, calculate_, find_

def get_grade(marks):          # calculates and returns a grade
    if marks >= 80: return "A"
    elif marks >= 60: return "B"
    else: return "C"

def show_grade(name, marks):   # displays the result
    grade = get_grade(marks)
    print(f"{name}: {marks} marks → Grade {grade}")

show_grade("Aarav", 88)
show_grade("Diya", 65)

print()

# --- Golden Rules for Function Names ---
print("=== Function Naming Rules ===")
print("1. Use verbs: calculate_, get_, find_, show_, check_, apply_")
print("2. Be specific: 'get_average_marks' not 'get_stuff'")
print("3. Boolean functions: start with is_, has_, can_")
print("4. Display functions: start with show_, print_, display_")
print("5. Use snake_case: calculate_total not CalculateTotal or calctotal")

# Think:
# 1. Rename these: def a(n): def b(x, y): def c(p, r, t):
# 2. What would you name a function that checks if a library book is overdue?
