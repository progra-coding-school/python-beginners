# Program Code: EX-KN-03
# Title: Handling Multiple Exceptions
# Cognitive Skill: Knowledge
# Topic: Exceptions in Python

# You can catch different exception types with separate except blocks.
# Python checks them TOP to BOTTOM and runs the FIRST match.

# --- Multiple except blocks ---
print("=== Multiple except blocks ===")

def safe_divide(a, b):
    try:
        result = a / b
        print(f"  {a} / {b} = {result:.2f}")
    except ZeroDivisionError:
        print(f"  Cannot divide {a} by zero!")
    except TypeError:
        print(f"  Both values must be numbers, not strings!")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "x")

print()

# --- Catching multiple exceptions in ONE line with a tuple ---
print("=== Catching multiple types at once ===")

def parse_and_divide(a_str, b_str):
    try:
        result = int(a_str) / int(b_str)
        print(f"  Result: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"  Error: {e}")

parse_and_divide("10", "2")     # OK
parse_and_divide("10", "0")     # ZeroDivisionError
parse_and_divide("10", "abc")   # ValueError

print()

# --- Order matters: specific before general ---
print("=== Order matters — specific FIRST ===")

try:
    x = int("hello")
except ValueError:
    print("Caught ValueError specifically — 'hello' is not an int")
except Exception:
    print("Caught general Exception (never reached here)")

print()

# --- General Exception as fallback ---
print("=== Specific + general fallback ===")

data = [10, "twenty", 0, 5]
for item in data:
    try:
        print(f"  100 / {item} = {100 / item:.1f}")
    except ZeroDivisionError:
        print(f"  Skipping {item} — division by zero")
    except TypeError:
        print(f"  Skipping '{item}' — not a number")
    except Exception as e:
        print(f"  Unexpected error with {item}: {e}")

# Think:
# 1. What happens if you put the general `except Exception` BEFORE the specific ones?
# 2. When would you use (ValueError, TypeError) in a single except vs two separate blocks?
