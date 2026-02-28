# Program Code: EX-UN-02
# Title: How Exceptions Work Internally
# Cognitive Skill: Understanding
# Topic: Exceptions in Python

# --- What happens when an exception is raised ---
print("=== Execution stops at the error line ===")

def step_a():
    print("  step_a: start")
    result = 10 / 0          # exception raised HERE
    print("  step_a: this line is NEVER reached")
    return result

try:
    print("Before call")
    step_a()
    print("After call — also NEVER reached")
except ZeroDivisionError as e:
    print(f"Caught in caller: {e}")

print()

# --- Exceptions bubble up the call stack ---
print("=== Exception bubbles up if not caught ===")

def inner():
    return int("bad")       # ValueError raised here

def middle():
    return inner()          # not caught here — bubbles up

def outer():
    try:
        return middle()     # caught HERE, two levels up
    except ValueError as e:
        print(f"  outer() caught it: {e}")

outer()

print()

# --- The exception hierarchy ---
print("=== Exception hierarchy (simplified) ===")
print("  BaseException")
print("  └── Exception          ← most exceptions inherit from here")
print("      ├── ValueError     ← bad value (e.g. int('abc'))")
print("      ├── TypeError      ← wrong type (e.g. 1 + 'a')")
print("      ├── ZeroDivisionError ← divide by zero")
print("      ├── IndexError     ← list index out of range")
print("      ├── KeyError       ← dict key not found")
print("      ├── NameError      ← variable not defined")
print("      ├── AttributeError ← object has no such attribute")
print("      └── RuntimeError   ← general runtime error")

print()

# --- Catching a parent catches all children ---
print("=== Catching a parent exception type ===")
errors = [
    lambda: 1 / 0,
    lambda: int("abc"),
    lambda: [1, 2][99],
]

for fn in errors:
    try:
        fn()
    except Exception as e:       # catches all of the above
        print(f"  {type(e).__name__}: {e}")

print()
print("Exception is the parent of most errors —")
print("catching it catches almost everything (use sparingly).")

# Think:
# 1. If inner() raises ValueError and middle() doesn't catch it, where does it go?
# 2. Why is it risky to always catch Exception instead of a specific type?
