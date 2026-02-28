# Program Code: TU-CT-01
# Title: Spot the Bug
# Cognitive Skill: Critical Thinking
# Topic: Tuples in Python

# Each block has ONE bug. Find it, explain WHY it is wrong, then fix it.

# --- Bug 1 ---
print("=== Bug 1 ===")
# Intended: create a single-item tuple
wrong = (42)
print("type(wrong):", type(wrong))   # int — not a tuple!

# Fix: trailing comma makes it a tuple
correct = (42,)
print("type(correct):", type(correct))  # tuple

print()

# --- Bug 2 ---
print("=== Bug 2 ===")
colours = ("red", "green", "blue")
# Intended: change 'green' to 'yellow'
try:
    colours[1] = "yellow"   # Bug! Tuples are immutable
except TypeError as e:
    print("TypeError:", e)

# Fix: convert to list, modify, convert back
colours_list    = list(colours)
colours_list[1] = "yellow"
colours         = tuple(colours_list)
print("Fixed:", colours)

print()

# --- Bug 3 ---
print("=== Bug 3 ===")
# Intended: unpack a 3-item tuple into 2 variables
record = ("Aarav", 13, "Chennai")
try:
    name, age = record      # Bug! 3 values, only 2 variables
except ValueError as e:
    print("ValueError:", e)

# Fix: either use all 3 variables or use * to catch the rest
name, age, city = record
print(f"Name: {name}, Age: {age}, City: {city}")

print()

# --- Bug 4 ---
print("=== Bug 4 ===")
data = (10, 20, 30, 40, 50)
# Intended: find position of value 30
try:
    pos = data.index(99)    # Bug! 99 is not in tuple — ValueError
except ValueError as e:
    print("ValueError:", e)

# Fix: check membership first
target = 30
if target in data:
    print(f"Position of {target}:", data.index(target))

print()

# --- Bug 5 ---
print("=== Bug 5 ===")
# Intended: empty tuple
empty_wrong = ()     # this IS actually valid!
print("Empty tuple:", empty_wrong, "| type:", type(empty_wrong))
# But here is a real tricky bug:
# Intended: tuple of one string
t = ("hello")        # Bug! This is a string, not a tuple
print("type('hello') :", type(t))       # str — not tuple!
# Fix:
t = ("hello",)
print("type('hello',):", type(t))       # tuple

# Think:
# 1. Why does Python require a trailing comma for single-item tuples?
# 2. If you must "change" a tuple value, what are the steps?
