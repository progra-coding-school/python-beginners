# Program Code: FN-UN-02
# Title: How Functions Work Internally
# Cognitive Skill: Understanding
# Topic: Functions in Python

# When you call a function, Python does these steps:
# 1. Jumps to the function definition
# 2. Assigns the arguments to the parameters
# 3. Runs the function body
# 4. Returns the result (or None) back to the call point
# 5. Continues from where it left off

# --- Tracing a function call step by step ---
def add(a, b):
    print(f"  [Inside add] a={a}, b={b}")
    result = a + b
    print(f"  [Inside add] result={result}")
    return result

print("Before calling add()")
total = add(10, 5)
print("After calling add(), total =", total)
print()

# --- Variables inside a function are LOCAL ---
# They exist only while the function is running. They disappear after.
def calculate_discount(price):
    discount = price * 0.10      # 'discount' is LOCAL to this function
    final = price - discount
    return final

bill = calculate_discount(500)
print("Bill after discount: Rs.", bill)
# print(discount)  ← This would ERROR! 'discount' doesn't exist outside

print()

# --- Each function call is independent ---
def show_double(number):
    doubled = number * 2
    print(f"  Double of {number} = {doubled}")

show_double(3)    # doubled = 6 here
show_double(7)    # doubled = 14 here (separate, independent call)
show_double(10)   # doubled = 20 here

print()

# --- Functions can call other functions ---
def calculate_total(price, quantity):
    return price * quantity

def calculate_tax(amount):
    return amount * 0.05

def final_bill(price, quantity):
    total = calculate_total(price, quantity)   # calls another function!
    tax = calculate_tax(total)
    return total + tax

bill = final_bill(120, 3)
print(f"Final bill for 3 items at Rs.120: Rs.{bill}")

# Think:
# 1. If you define a variable 'x = 5' inside a function, can you use x outside it?
# 2. What happens if you call a function BEFORE defining it?
