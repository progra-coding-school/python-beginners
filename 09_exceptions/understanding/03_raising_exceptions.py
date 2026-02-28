# Program Code: EX-UN-03
# Title: Raising Exceptions
# Cognitive Skill: Understanding
# Topic: Exceptions in Python

# You can RAISE exceptions yourself using the `raise` keyword.
# This lets you enforce your own rules and signal problems clearly.

# --- Basic raise ---
print("=== Basic raise ===")

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    print(f"  Age set to: {age}")

try:
    set_age(13)
    set_age(-5)
except ValueError as e:
    print(f"  ValueError: {e}")

print()

# --- raise inside validation ---
print("=== Raising from validation ===")

def set_score(score):
    if not isinstance(score, int):
        raise TypeError(f"Score must be an integer, got {type(score).__name__}")
    if not (0 <= score <= 100):
        raise ValueError(f"Score must be 0–100, got {score}")
    return score

tests = [85, -10, 110, "A+", 0]
for val in tests:
    try:
        result = set_score(val)
        print(f"  Valid score: {result}")
    except (ValueError, TypeError) as e:
        print(f"  Rejected: {e}")

print()

# --- Re-raising an exception ---
print("=== Re-raising (passing the error up) ===")

def parse_number(text):
    try:
        return int(text)
    except ValueError:
        print(f"  parse_number: caught ValueError for '{text}', re-raising...")
        raise       # re-raise the SAME exception

try:
    parse_number("oops")
except ValueError as e:
    print(f"  Outer caught re-raised ValueError: {e}")

print()

# --- Custom exception classes ---
print("=== Custom exception ===")

class InsufficientBalanceError(Exception):
    """Raised when a withdrawal exceeds available balance."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            f"Cannot withdraw Rs.{amount}. Balance is only Rs.{balance}."
        )
    return balance - amount

try:
    new_balance = withdraw(500, 200)
    print(f"  Withdrawn. Remaining: Rs.{new_balance}")
    new_balance = withdraw(new_balance, 1000)   # this fails
except InsufficientBalanceError as e:
    print(f"  {e}")

# Think:
# 1. When would you raise a ValueError vs a TypeError?
# 2. Why is it useful to create your own custom exception class?
