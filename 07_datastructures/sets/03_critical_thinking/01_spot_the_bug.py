# Spot the Bug
# Each block has ONE bug. Find it, explain WHY it is wrong, then fix it.
# Spotting bugs in set code builds the habit of precise, careful reading.

# --- Bug 1 ---
# Intended: create an empty set
# Bug: {} creates a DICT, not a set — Python inherited {} for dicts before sets existed
print("Bug 1:")
wrong = {}
print("type({})  :", type(wrong))   # <class 'dict'>

# Fix: use set() — the only way to create an empty set
correct = set()
print("type(set()):", type(correct))  # <class 'set'>

print()

# --- Bug 2 ---
# Intended: access the first item in the set
# Bug: sets have no index — s[0] raises TypeError because sets are unordered
print("Bug 2:")
colours = {"red", "green", "blue"}
try:
    print(colours[0])   # TypeError — no indexing on sets
except TypeError as e:
    print("TypeError:", e)

# Fix: sort first, then index — or loop if order doesn't matter
print("First alphabetically:", sorted(colours)[0])

print()

# --- Bug 3 ---
# Intended: remove "papaya" safely even if it might not exist
# Bug: .remove() raises KeyError if the item is missing — dangerous when data is uncertain
print("Bug 3:")
fruits = {"mango", "banana", "apple"}
try:
    fruits.remove("papaya")
except KeyError as e:
    print("KeyError from remove():", e)

# Fix: use .discard() — removes if present, silently ignores if missing
fruits.discard("papaya")
print("After safe discard:", fruits)

print()

# --- Bug 4 ---
# Intended: put a list inside a set
# Bug: lists are mutable and cannot be hashed — sets require immutable (hashable) elements
print("Bug 4:")
try:
    bad_set = {[1, 2, 3], "hello"}
except TypeError as e:
    print("TypeError:", e)

# Fix: use a tuple — tuples are immutable and can be hashed
good_set = {(1, 2, 3), "hello"}
print("Tuple in set works:", good_set)

print()

# --- Bug 5 ---
# Intended: find items in a but NOT in b (difference)
# Bug: & gives intersection (items in BOTH), not difference (items only in a)
print("Bug 5:")
a = {1, 2, 3}
b = {3, 4, 5}
wrong_result   = a & b    # intersection → {3}
correct_result = a - b    # difference → {1, 2}

print("Bug (& used)   :", wrong_result)    # {3} ← intersection, not what we wanted
print("Fix (- used)   :", correct_result)  # {1, 2} ← correct difference

# Think:
# 1. Why does {} create a dict and not a set? (Hint: which came first in Python's history?)
# 2. What is the rule: use .discard() or .remove()? When does it matter?
