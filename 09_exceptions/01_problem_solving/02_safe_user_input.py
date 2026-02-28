# Program Code: EX-PS-02
# Title: Safe User Input Validator
# Cognitive Skill: Problem Solving
# Topic: Exceptions in Python

# Problem:
# Build input validators that keep asking until valid data is entered.
# Use exceptions to detect bad input cleanly.

# NOTE: These functions use input() — run this file to interact!
# The demo at the bottom simulates inputs without blocking.

# --- Validator 1: Get a valid integer ---
def get_integer(prompt, min_val=None, max_val=None):
    """Keep asking until a valid integer in range is entered."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  Too small! Must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Too large! Must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("  Not a valid integer. Please try again.")

# --- Validator 2: Get a positive float ---
def get_positive_float(prompt):
    """Keep asking until a positive number is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  Must be a positive number.")
                continue
            return value
        except ValueError:
            print("  Not a valid number. Please try again.")

# --- Validator 3: Get one of allowed choices ---
def get_choice(prompt, choices):
    """Keep asking until a valid choice is entered."""
    choices_lower = [c.lower() for c in choices]
    while True:
        answer = input(prompt).strip().lower()
        if answer in choices_lower:
            return answer
        print(f"  Invalid choice. Choose from: {choices}")

# --- Simulation (no live input needed to run this file) ---
print("=== Input Validator Demonstration ===")
print()

print("--- Simulating: integer between 1 and 10 ---")
test_inputs = ["abc", "-5", "15", "7"]
for val in test_inputs:
    try:
        n = int(val)
        if n < 1 or n > 10:
            raise ValueError("Out of range")
        print(f"  '{val}' → accepted: {n}")
        break
    except ValueError as e:
        print(f"  '{val}' → rejected: {e}")

print()

print("--- Simulating: positive float ---")
for val in ["hello", "-3.5", "0", "4.75"]:
    try:
        n = float(val)
        if n <= 0:
            raise ValueError("Must be positive")
        print(f"  '{val}' → accepted: {n}")
        break
    except ValueError as e:
        print(f"  '{val}' → rejected: {e}")

print()

print("--- Simulating: yes/no choice ---")
for val in ["maybe", "YES", "no"]:
    if val.lower() in ["yes", "no"]:
        print(f"  '{val}' → accepted: {val.lower()}")
        break
    else:
        print(f"  '{val}' → rejected: not yes or no")

print()
print("=== To use live validators, call: ===")
print("  age = get_integer('Enter age: ', min_val=5, max_val=18)")
print("  price = get_positive_float('Enter price: Rs.')")
print("  choice = get_choice('Yes or No? ', ['yes', 'no'])")

# Think:
# 1. Why use a while True loop inside the validator?
# 2. What would happen without the try/except if the user types letters into get_integer()?
