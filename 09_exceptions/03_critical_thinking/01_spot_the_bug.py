# Program Code: EX-CT-01
# Title: Spot the Bug
# Cognitive Skill: Critical Thinking
# Topic: Exceptions in Python

# Each block has ONE bug. Find it, explain WHY it is wrong, then fix it.

# --- Bug 1: Catching the wrong exception type ---
print("=== Bug 1 ===")
# Intended: catch a ValueError when parsing fails
try:
    value = int("hello")
except TypeError:          # Bug! int("hello") raises ValueError, not TypeError
    print("Caught it!")

# Fix:
try:
    value = int("hello")
except ValueError:
    print("Fixed: caught ValueError correctly")

print()

# --- Bug 2: Bare except hides the real problem ---
print("=== Bug 2 ===")
data = {"name": "Aarav"}
try:
    print(data["age"])
except:                    # Bug! Too broad — hides what actually went wrong
    print("Something failed")   # which exception? we don't know

# Fix:
try:
    print(data["age"])
except KeyError as e:
    print(f"Fixed: KeyError — key {e} not found")

print()

# --- Bug 3: except before the error it handles ---
print("=== Bug 3 ===")
# Intended: specific then general
try:
    result = 1 / 0
except Exception:          # Bug! This catches everything — ValueError below never triggers
    print("general exception")
except ZeroDivisionError:
    print("zero division")  # unreachable!

# Fix: specific BEFORE general
try:
    result = 1 / 0
except ZeroDivisionError:
    print("Fixed: zero division caught first")
except Exception:
    print("general fallback")

print()

# --- Bug 4: Using variable defined only inside try ---
print("=== Bug 4 ===")
try:
    score = int("85")
except ValueError:
    print("Bad input")

# Bug! score might not be defined if exception was raised
# print(f"Score: {score}")   # NameError if "85" was "abc"

# Fix: initialise before try
score = None
try:
    score = int("85")
except ValueError:
    print("Bad input")
if score is not None:
    print(f"Fixed — score: {score}")

print()

# --- Bug 5: Swallowing exceptions silently ---
print("=== Bug 5 ===")
def load_data(raw):
    try:
        return int(raw)
    except:
        pass                # Bug! Silently ignores errors — caller has no idea what happened

result = load_data("oops")
print("Result:", result)    # None — but WHY? No indication of failure!

# Fix: at minimum log it; better — let it propagate or return a sentinel
def load_data_fixed(raw):
    try:
        return int(raw)
    except ValueError as e:
        print(f"  Warning: could not parse '{raw}': {e}")
        return None

result = load_data_fixed("oops")
print("Fixed result:", result)

# Think:
# 1. In Bug 2, what is the danger of using a bare `except` in a real application?
# 2. In Bug 4, what would happen at the print statement if the input was invalid?
