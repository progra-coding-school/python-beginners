# Program Code: FN-CT-03
# Title: Assumption Breaker — Functions
# Cognitive Skill: Critical Thinking (Assumption Breaking)
# Topic: Functions in Python

# We often make wrong assumptions about how functions behave.
# Let's test and break those assumptions!

print("=== Assumption Breaker — Functions ===")
print()

# --- Assumption 1 ---
print("Assumption 1: 'Calling a function always prints something'")
def silent_add(a, b):
    return a + b    # returns but does NOT print

result = silent_add(5, 3)
# Nothing is printed from the function call!
print(f"  silent_add(5, 3) ran, but nothing printed from inside it.")
print(f"  The returned value is: {result}")
print("  WRONG! A function with only 'return' prints NOTHING.")
print()

# --- Assumption 2 ---
print("Assumption 2: 'return and print do the same thing'")
def with_print(n):
    print("From print:", n * 2)    # displays but returns nothing

def with_return(n):
    return n * 2                   # returns but displays nothing

val_p = with_print(5)     # displays 10 on screen
val_r = with_return(5)    # doesn't display, but gives 10 back
print(f"  with_print stored: {val_p}")     # None
print(f"  with_return stored: {val_r}")    # 10
print("  WRONG! Only 'return' lets you USE the result later.")
print()

# --- Assumption 3 ---
print("Assumption 3: 'Variables inside a function are accessible outside'")
def set_score():
    secret_score = 100    # local variable

set_score()
try:
    print(secret_score)   # will cause NameError!
except NameError:
    print("  NameError! 'secret_score' doesn't exist outside the function.")
print("  WRONG! Variables inside a function are LOCAL — they disappear after the call.")
print()

# --- Assumption 4 ---
print("Assumption 4: 'A function can only return one value'")
def get_stats(numbers):
    total   = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum    # returns 4 values!

t, a, lo, hi = get_stats([80, 45, 92, 67, 55])
print(f"  Total={t}, Average={a:.1f}, Min={lo}, Max={hi}")
print("  WRONG! A function can return multiple values (as a tuple).")
print()

# --- Assumption 5 ---
print("Assumption 5: 'You must store a return value in a variable'")
def greet(name):
    return f"Hello, {name}!"

# You can use the return value directly — no storage needed!
print(greet("Aarav"))          # directly print
print(greet("Diya").upper())   # use it immediately with .upper()
print("  Correct! You can use a return value directly without storing it.")

# Think:
# 1. What happens if you return inside an if but there's no else — and the if is skipped?
# 2. Can two functions have a parameter with the same name (e.g., both use 'n')? Why?
