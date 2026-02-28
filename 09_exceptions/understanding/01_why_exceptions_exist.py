# Program Code: EX-UN-01
# Title: Why Exceptions Exist
# Cognitive Skill: Understanding
# Topic: Exceptions in Python

# WITHOUT exceptions: you have to manually check EVERY possible failure.
# WITH exceptions: you write the happy path, catch errors separately.

# --- Problem: Safe division without exceptions ---
print("=== WITHOUT exceptions — checking everything manually ===")

def divide_manual(a, b):
    if not isinstance(a, (int, float)):
        return "Error: a is not a number"
    if not isinstance(b, (int, float)):
        return "Error: b is not a number"
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

print(divide_manual(10, 2))     # 5.0
print(divide_manual(10, 0))     # Error
print(divide_manual(10, "x"))   # Error
print()
print("Problem: you must anticipate EVERY possible failure BEFORE it happens.")
print("For complex programs this becomes impossible to do completely.")

print()

# --- Same logic WITH exceptions ---
print("=== WITH exceptions — clean and complete ===")

def divide_exceptions(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: both must be numbers"

print(divide_exceptions(10, 2))      # 5.0
print(divide_exceptions(10, 0))      # Error
print(divide_exceptions(10, "x"))    # Error
print()
print("Better: write the happy path clearly, catch errors separately.")
print("Python tells you WHAT went wrong, not just 'something failed'.")

print()

# --- Exceptions separate normal flow from error flow ---
print("=== Separation of concerns ===")
print("Normal logic  → inside try")
print("Error handling → inside except")
print("Cleanup        → inside finally")
print("Success only   → inside else")
print()
print("This makes code READABLE — you see the main purpose first,")
print("and error handling as a clearly labelled afterthought.")

print()

# --- Real-world: ATM machine ---
print("=== Real-world: ATM withdrawal ===")
balance = 500

def withdraw(amount):
    try:
        amount = int(amount)
        if amount > balance:
            raise ValueError("Insufficient balance")
        print(f"  Dispensing Rs.{amount}. Remaining: Rs.{balance - amount}")
    except ValueError as e:
        print(f"  Transaction failed: {e}")
    except TypeError:
        print("  Please enter a valid number.")

withdraw(200)
withdraw(1000)
withdraw("two hundred")

# Think:
# 1. Without exceptions, how would you handle a file that doesn't exist?
# 2. Why is it better to "ask forgiveness" (try/except) than "ask permission" (if checks)?
