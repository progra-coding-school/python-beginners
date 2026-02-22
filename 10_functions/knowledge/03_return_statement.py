# Program Code: FN-KN-03
# Title: The Return Statement
# Cognitive Skill: Knowledge
# Topic: Functions in Python

# 'return' sends a value BACK from the function to where it was called.
# Without return, the function does its job but gives nothing back.

# --- Without return ---
def add_no_return(a, b):
    result = a + b
    print("Inside function:", result)   # prints, but gives nothing back

value = add_no_return(5, 3)
print("Outside function:", value)       # None — nothing was returned!

print()

# --- With return ---
def add(a, b):
    result = a + b
    return result    # sends result back to the caller

value = add(5, 3)
print("Outside function:", value)       # 8 — received the returned value!

print()

# --- Using the returned value directly ---
print("Sum:", add(10, 20))
print("Sum:", add(7, 3))

total = add(15, 25) + add(5, 5)    # use returned values in expressions
print("Combined total:", total)

print()

# --- Return stops the function immediately ---
def check_pass(marks):
    if marks >= 35:
        return "PASS"    # function stops here if marks >= 35
    return "FAIL"        # only reaches here if marks < 35

print(check_pass(72))
print(check_pass(28))

print()

# --- Returning multiple values ---
def get_min_max(a, b, c):
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    return minimum, maximum    # returns two values as a tuple

low, high = get_min_max(45, 89, 23)
print("Lowest:", low, "  Highest:", high)

# Think:
# 1. What is printed if you call a function that has no return statement?
# 2. Can a function have more than one return statement? When would that be useful?
