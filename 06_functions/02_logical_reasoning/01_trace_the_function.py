# Program Code: FN-LR-01
# Title: Trace the Function
# Cognitive Skill: Logical Reasoning (Tracing)
# Topic: Functions in Python

# Read each function call. Predict the output BEFORE running.
# Trace step by step — follow the value through each line.

score = 0

# --- Round 1 ---
def double(n):
    return n * 2

print("Round 1: double(7)")
answer = input("What does it return? ")
actual = double(7)
print(f"Answer: {actual}")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

# --- Round 2 ---
def mystery(a, b):
    x = a + b
    y = x * 2
    return y

print("Round 2: mystery(3, 4)")
print("  x = 3 + 4 = ?")
print("  y = x * 2 = ?")
print("  returns y")
answer = input("What does mystery(3, 4) return? ")
actual = mystery(3, 4)
print(f"Answer: {actual}  (x=7, y=14)")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

# --- Round 3 ---
def greet(name):
    message = "Hello, " + name + "!"
    return message

print("Round 3: greet('Aarav')")
answer = input("What does it return? ")
actual = greet("Aarav")
print(f"Answer: {actual}")
if answer.strip() == actual:
    score += 1
    print("Correct!")
print()

# --- Round 4 ---
def is_teen(age):
    return age >= 13 and age <= 19

print("Round 4: is_teen(15)")
answer = input("What does it return? (True/False) ")
actual = is_teen(15)
print(f"Answer: {actual}  (15>=13 and 15<=19 → True and True → True)")
if answer.strip().lower() == str(actual).lower():
    score += 1
    print("Correct!")
print()

# --- Round 5 ---
def process(n):
    if n % 2 == 0:
        return "even"
    return "odd"

print("Round 5: process(9)")
answer = input("What does it return? ")
actual = process(9)
print(f"Answer: {actual}  (9 % 2 = 1, not 0, so → 'odd')")
if answer.strip() == actual:
    score += 1
    print("Correct!")
print()

# --- Round 6 ---
def add_tax(price):
    tax = price * 0.10
    return price + tax

def final_price(items):
    total = 0
    for item in items:
        total += item
    return add_tax(total)

prices = [100, 200, 50]
print("Round 6: final_price([100, 200, 50])")
print("  Step 1: total = 100 + 200 + 50 = ?")
print("  Step 2: add_tax(total) = total + total*0.10 = ?")
answer = input("What does final_price([100, 200, 50]) return? ")
actual = final_price(prices)
print(f"Answer: {actual}")
if answer.strip() in [str(actual), str(int(actual))]:
    score += 1
    print("Correct!")
print()

print(f"Tracing Score: {score} / 6")
