# Program Code: SE-CT-01
# Title: Spot the Bug
# Cognitive Skill: Critical Thinking
# Topic: Sets in Python

# Each block has ONE bug. Find it, explain WHY it is wrong, then fix it.

# --- Bug 1 ---
print("=== Bug 1 ===")
# Intended: create an empty set
# Bug: {} creates a dict, not a set!
wrong = {}
print("type({})  :", type(wrong))   # <class 'dict'>

# Fix:
correct = set()
print("type(set()):", type(correct))  # <class 'set'>

print()

# --- Bug 2 ---
print("=== Bug 2 ===")
colours = {"red", "green", "blue"}
# Intended: access the first item
# Bug: sets have no index!
try:
    print(colours[0])   # TypeError — no indexing
except TypeError as e:
    print("TypeError:", e)

# Fix: loop or convert to sorted list if order matters
print("First alphabetically:", sorted(colours)[0])

print()

# --- Bug 3 ---
print("=== Bug 3 ===")
fruits = {"mango", "banana", "apple"}
# Intended: remove "papaya" safely
# Bug: .remove() raises KeyError if item is missing
try:
    fruits.remove("papaya")
except KeyError as e:
    print("KeyError from remove():", e)

# Fix: use .discard() — silent if missing
fruits.discard("papaya")
print("After safe discard:", fruits)

print()

# --- Bug 4 ---
print("=== Bug 4 ===")
# Intended: put a list inside a set
# Bug: lists are mutable — they can't be hashed
try:
    bad_set = {[1, 2, 3], "hello"}
except TypeError as e:
    print("TypeError:", e)

# Fix: use a tuple instead
good_set = {(1, 2, 3), "hello"}
print("Tuple in set works:", good_set)

print()

# --- Bug 5 ---
print("=== Bug 5 ===")
a = {1, 2, 3}
b = {3, 4, 5}
# Intended: find items in a but not b
# Bug: wrong operator — & gives intersection, not difference
wrong_result  = a & b
correct_result = a - b

print("Bug (& used)   :", wrong_result)    # {3}   ← intersection
print("Fix (- used)   :", correct_result)  # {1, 2} ← difference

# Think:
# 1. Why does {} create a dict and not a set? (Hint: which came first in Python's history?)
# 2. What is the rule: use .discard() or .remove()? When does it matter?
