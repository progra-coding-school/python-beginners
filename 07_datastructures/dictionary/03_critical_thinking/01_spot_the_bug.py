# Program Code: DC-CT-01
# Title: Spot the Bug
# Cognitive Skill: Critical Thinking
# Topic: Dictionaries in Python

# Each block below has ONE bug. Find it, explain WHY it is wrong,
# then fix it and confirm the correct output.

# --- Bug 1 ---
print("=== Bug 1 ===")
student = {"name": "Aarav", "age": 13, "grade": 7}

# Intended: print the student's age
# Bug: what is wrong here?
# print(student["Age"])     # <- Bug!

# Fix:
print(student["age"])       # dictionary keys are case-sensitive

print()

# --- Bug 2 ---
print("=== Bug 2 ===")
prices = {"mango": 120, "banana": 40}

# Intended: add apples with price 80
# Bug: what is wrong here?
# prices("apple") = 80      # <- Bug! () is a function call, not dict access

# Fix:
prices["apple"] = 80
print(prices)

print()

# --- Bug 3 ---
print("=== Bug 3 ===")
scores = {"Aarav": 85, "Diya": 92, "Karthik": 78}

# Intended: remove Karthik and save his score
# Bug: what is wrong here?
# del scores["Karthik"]         # del removes but gives nothing back
# saved = scores["Karthik"]     # KeyError — already deleted!

# Fix: use .pop() to remove AND save in one step
saved = scores.pop("Karthik")
print("Saved score:", saved)
print("Remaining:", scores)

print()

# --- Bug 4 ---
print("=== Bug 4 ===")
menu = {"idli": 15, "dosa": 30}

# Intended: loop over menu and double every price
# Bug: modifying dict while looping causes RuntimeError
# for item in menu:
#     menu[item] *= 2           # <- Bug: can sometimes cause issues

# Fix: loop over a copy of keys
for item in list(menu.keys()):
    menu[item] *= 2
print("Doubled prices:", menu)

print()

# --- Bug 5 ---
print("=== Bug 5 ===")
# Intended: create a dictionary with a list as a key — will this work?
# Bug: lists are mutable and CANNOT be dictionary keys
try:
    bad_dict = {[1, 2, 3]: "coordinates"}  # <- Bug!
except TypeError as e:
    print("TypeError caught:", e)
    print("Fix: use a TUPLE as the key instead.")
    good_dict = {(1, 2, 3): "coordinates"}
    print("Good dict:", good_dict)

# Think:
# 1. Why are dictionary keys case-sensitive? Give a real-life example where this matters.
# 2. What is the rule: when should you use .pop() instead of del?
