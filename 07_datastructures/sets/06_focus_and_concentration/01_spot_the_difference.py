# Program Code: SE-FC-01
# Title: Spot the Difference
# Cognitive Skill: Focus and Concentration
# Topic: Sets in Python

# Two versions of similar code are shown.
# Find every difference — some are bugs, some are style choices.

# ─── Pair 1 ─────────────────────────────────────────────────────
print("=== Pair 1 ===")

# Version A
a1 = {1, 2, 3, 4}
a2 = {3, 4, 5, 6}
print("A:", a1 & a2)    # intersection

# Version B
b1 = {1, 2, 3, 4}
b2 = {3, 4, 5, 6}
print("B:", b1 | b2)    # union — different operator!
# Difference: A uses & (intersection → {3,4}), B uses | (union → {1,2,3,4,5,6})

print()

# ─── Pair 2 ─────────────────────────────────────────────────────
print("=== Pair 2 ===")

# Version A — safe remove
colours_a = {"red", "green", "blue"}
colours_a.discard("purple")         # no error even if missing
print("A:", colours_a)

# Version B — risky remove
colours_b = {"red", "green", "blue"}
try:
    colours_b.remove("purple")      # KeyError if missing!
except KeyError as e:
    print("B: KeyError →", e)
# Difference: discard() is silent; remove() raises KeyError.

print()

# ─── Pair 3 ─────────────────────────────────────────────────────
print("=== Pair 3 ===")

# Version A — empty set
empty_a = set()
print("A type:", type(empty_a))     # <class 'set'>

# Version B — empty dict (bug if set was intended!)
empty_b = {}
print("B type:", type(empty_b))     # <class 'dict'>
# Difference: {} gives a dict; set() gives a set. Critical distinction!

print()

# ─── Pair 4 ─────────────────────────────────────────────────────
print("=== Pair 4 ===")

fruits = {"mango", "apple", "banana"}

# Version A: correct membership check
print("A:", "mango" in fruits)      # True

# Version B: comparing to a string — logic error!
print("B:", fruits == "mango")      # False — comparing set to string
# Difference: 'in' checks membership; '==' compares the whole set to a value.

print()

# ─── Pair 5 ─────────────────────────────────────────────────────
print("=== Pair 5 ===")

items_a = ["pen", "pen", "book"]
result_a = list(set(items_a))       # removes duplicates, converts back

items_b = ["pen", "pen", "book"]
result_b = set(items_b)             # stays as a set (no list conversion)

print("A:", result_a)               # list
print("B:", result_b)               # set
# Difference: A is a list (ordered-ish, indexable); B is a set (unordered).

# Think:
# 1. In Pair 3, how would a bug caused by {} vs set() show up later in the program?
# 2. In Pair 5, when would you want a list result vs a set result?
