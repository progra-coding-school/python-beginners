# Program Code: EX-PS-01
# Title: Safe Calculator
# Cognitive Skill: Problem Solving
# Topic: Exceptions in Python

# Problem:
# Build a calculator that handles ALL possible errors gracefully.
# It should never crash, no matter what the user enters.
# Operations: +, -, *, /

# --- Step 1: Core calculation with exception handling ---
def calculate(a_str, operator, b_str):
    # Step 1a: parse inputs
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        return f"Error: '{a_str}' or '{b_str}' is not a valid number."

    # Step 1b: perform operation
    try:
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a / b
        else:
            return f"Error: Unknown operator '{operator}'. Use +, -, *, /"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Step 1c: clean output (remove .0 for whole numbers)
    if result == int(result):
        return f"Result: {int(result)}"
    return f"Result: {result:.4f}"

# --- Step 2: Demo with various inputs ---
print("=== Safe Calculator ===")
print()

test_cases = [
    ("10",    "+", "5"),
    ("20",    "-", "8"),
    ("6",     "*", "7"),
    ("15",    "/", "3"),
    ("10",    "/", "0"),       # ZeroDivisionError
    ("abc",   "+", "5"),       # ValueError
    ("10",    "%", "3"),       # Unknown operator
    ("3",     "*", "3.5"),     # float result
    ("-10",   "+", "-5"),      # negatives
    ("1000",  "*", "1000"),    # large numbers
]

for a, op, b in test_cases:
    output = calculate(a, op, b)
    print(f"  {a} {op} {b}  →  {output}")

# --- Step 3: What a CRASH would look like without handling ---
print()
print("=== What crashes look like (without try/except) ===")
print("  int('abc')   → ValueError: invalid literal for int()")
print("  10 / 0       → ZeroDivisionError: division by zero")
print("  'abc' + 10   → TypeError: can only concatenate str (not int) to str")

# Think:
# 1. Why did we use float() instead of int() to parse the inputs?
# 2. How would you extend this to support ** (power) and // (floor division)?
