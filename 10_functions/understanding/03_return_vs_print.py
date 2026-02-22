# Program Code: FN-UN-03
# Title: return vs print — What's the Difference?
# Cognitive Skill: Understanding
# Topic: Functions in Python

# This is one of the most common confusions for beginners.
# return and print look similar but are VERY different!

print("=== print inside a function ===")

def greet_print(name):
    print("Hello,", name)    # shows on screen BUT gives nothing back

result = greet_print("Aarav")
print("greet_print returned:", result)    # None — nothing came back!

print()
print("=== return from a function ===")

def greet_return(name):
    return "Hello, " + name   # gives the value BACK, but doesn't display it

result = greet_return("Aarav")
print("greet_return returned:", result)    # Hello, Aarav — got it back!

print()

# --- Why does this matter? ---
print("=== Why return matters ===")

# With print-only: you CANNOT use the result in calculations
def add_print(a, b):
    print(a + b)     # shows 15, but nothing comes back

total = add_print(10, 5)
# total = None — you can't do: total * 2

# With return: you CAN use the result
def add_return(a, b):
    return a + b     # sends 15 back

total = add_return(10, 5)
double = total * 2
print("Total:", total, "  Double:", double)    # works!

print()

# --- Real scenario ---
def calculate_average(m, s, e):
    return (m + s + e) / 3

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    else:
        return "C"

# Chaining works BECAUSE we use return!
maths, science, english = 82, 75, 90
avg = calculate_average(maths, science, english)
grade = get_grade(avg)
print(f"Average: {avg:.1f}  Grade: {grade}")

# This chain is IMPOSSIBLE if functions only used print and not return.

# Think:
# 1. When would you use print inside a function instead of return?
# 2. Can a function have BOTH print and return? What would happen?
