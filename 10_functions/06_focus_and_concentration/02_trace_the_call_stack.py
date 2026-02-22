# Program Code: FN-FC-02
# Title: Trace the Call Stack
# Cognitive Skill: Focus and Concentration (Mental Tracking)
# Topic: Functions in Python

# When functions call other functions, you must track values carefully.
# Follow each step — don't lose the thread!

score = 0

# --- Setup: functions to trace ---
def double(n):
    return n * 2

def add_ten(n):
    return n + 10

def square(n):
    return n * n

def process(x):
    a = double(x)        # Step 1
    b = add_ten(a)       # Step 2
    c = square(b)        # Step 3
    return c

# --- Trace challenges ---
print("=== Trace the Call Stack ===")
print("Track each variable's value through every function call.")
print()

print("Challenge 1: process(3)")
print("  Step 1: a = double(3) = ?")
print("  Step 2: b = add_ten(a) = ?")
print("  Step 3: c = square(b) = ?")
answer = input("Final result: ")
actual = process(3)
print(f"Answer: double(3)=6, add_ten(6)=16, square(16)={actual}")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

print("Challenge 2: process(5)")
answer = input("Final result (trace all 3 steps): ")
actual = process(5)
print(f"Answer: double(5)=10, add_ten(10)=20, square(20)={actual}")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

# Nested call chain
def get_bonus(salary):
    return salary * 0.10

def get_tax(salary):
    return salary * 0.05

def get_net(salary):
    bonus = get_bonus(salary)
    tax = get_tax(salary + bonus)
    return salary + bonus - tax

print("Challenge 3: get_net(10000)")
print("  Step 1: bonus = get_bonus(10000) = ?")
print("  Step 2: tax = get_tax(10000 + bonus) = ?")
print("  Step 3: return 10000 + bonus - tax = ?")
answer = input("Final result: ")
actual = get_net(10000)
bonus = get_bonus(10000)
tax = get_tax(10000 + bonus)
print(f"Answer: bonus={bonus}, tax={tax}, net={actual}")
if answer.strip() in [str(actual), str(int(actual))]:
    score += 1
    print("Correct!")
print()

# Multi-level chain
def step1(n): return n + 5
def step2(n): return n * 3
def step3(n): return n - 7
def pipeline(n):
    return step3(step2(step1(n)))

print("Challenge 4: pipeline(2)")
print("  step1(2) → step2(result) → step3(result)")
answer = input("Final result: ")
actual = pipeline(2)
print(f"Answer: step1(2)={step1(2)}, step2(7)={step2(7)}, step3(21)={step3(21)}")
print(f"         pipeline(2) = {actual}")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

print(f"Call Stack Score: {score} / 4")
print("Tip: Work from the INSIDE OUT when functions are nested.")
