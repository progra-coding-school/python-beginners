# Program Code: EX-KN-02
# Title: try and except
# Cognitive Skill: Knowledge
# Topic: Exceptions in Python

# SYNTAX:
#   try:
#       <code that might fail>
#   except <ExceptionType>:
#       <what to do if it fails>

# --- Basic try/except ---
print("=== Basic try/except ===")

try:
    score = int("ninety")   # this will fail
    print("Score:", score)  # this line is SKIPPED if above fails
except ValueError:
    print("That is not a valid number!")

print("Program continues after the except block.")

print()

# --- Catching the error message with 'as' ---
print("=== Catching the error message ===")
try:
    result = 100 / 0
except ZeroDivisionError as e:
    print("Error caught:", e)
    print("Type:", type(e).__name__)

print()

# --- try/except keeps the program alive ---
print("=== Keeping program alive ===")
numbers = [10, 0, 5, 0, 2]

for divisor in numbers:
    try:
        result = 100 / divisor
        print(f"  100 / {divisor} = {result:.1f}")
    except ZeroDivisionError:
        print(f"  100 / {divisor} = Cannot divide by zero!")

print()

# --- Bare except (catches ALL exceptions — use carefully) ---
print("=== Bare except — catches everything ===")
try:
    data = {"name": "Aarav"}
    print(data["age"])      # KeyError
except:
    print("Something went wrong! (bare except — we don't know what)")

print()
print("Better: name the specific exception type so you know exactly what went wrong.")

# Think:
# 1. What happens to lines AFTER the error inside the try block?
# 2. Why is a bare except (without naming the exception) generally a bad practice?
