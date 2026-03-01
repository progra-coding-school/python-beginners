# Spot the Difference — Two Versions of Similar Set Code
# Find every difference between Version A and Version B in each pair.
# Some differences cause BUGS. Some are just style choices. Train precise code reading.

# ─── Pair 1 ─────────────────────────────────────────────────────
# Difference: & (intersection) vs | (union) — same sets, completely different results
print("Pair 1:")

# Version A
a1 = {1, 2, 3, 4}
a2 = {3, 4, 5, 6}
print("A:", a1 & a2)    # intersection → {3, 4}

# Version B
b1 = {1, 2, 3, 4}
b2 = {3, 4, 5, 6}
print("B:", b1 | b2)    # union → {1, 2, 3, 4, 5, 6}

# Difference: A uses & (intersection → {3,4}), B uses | (union → {1,2,3,4,5,6})

print()

# ─── Pair 2 ─────────────────────────────────────────────────────
# Difference: .discard() is silent if the item is missing; .remove() raises KeyError
print("Pair 2:")

# Version A — safe remove (always works, never crashes)
colours_a = {"red", "green", "blue"}
colours_a.discard("purple")         # no error even if missing
print("A:", colours_a)

# Version B — risky remove (crashes if item not found)
colours_b = {"red", "green", "blue"}
try:
    colours_b.remove("purple")      # KeyError if missing!
except KeyError as e:
    print("B: KeyError →", e)
# Difference: discard() is silent; remove() raises KeyError.

print()

# ─── Pair 3 ─────────────────────────────────────────────────────
# Difference: {} creates a DICT, not a set — a classic Python gotcha
print("Pair 3:")

# Version A — correct: empty set
empty_a = set()
print("A type:", type(empty_a))     # <class 'set'>

# Version B — wrong: {} is an empty dict, not an empty set!
empty_b = {}
print("B type:", type(empty_b))     # <class 'dict'>
# Difference: {} gives a dict; set() gives a set. Critical distinction!

print()

# ─── Pair 4 ─────────────────────────────────────────────────────
# Difference: 'in' checks membership inside a set; '==' compares the whole set to something
print("Pair 4:")

fruits = {"mango", "apple", "banana"}

# Version A: correct membership check
print("A:", "mango" in fruits)      # True — "mango" is ONE element inside the set

# Version B: comparing set to a string — logic error!
print("B:", fruits == "mango")      # False — a set can never equal a plain string
# Difference: 'in' checks membership; '==' compares the whole set to a value.

print()

# ─── Pair 5 ─────────────────────────────────────────────────────
# Difference: list(set(...)) gives a list; set(...) stays as a set
print("Pair 5:")

items_a = ["pen", "pen", "book"]
result_a = list(set(items_a))       # removes duplicates, converts back to list

items_b = ["pen", "pen", "book"]
result_b = set(items_b)             # stays as a set (no list conversion)

print("A:", result_a)               # list — indexable, can append/sort in place
print("B:", result_b)               # set — unordered, membership-optimised
# Difference: A is a list (ordered-ish, indexable); B is a set (unordered).

# Think:
# 1. In Pair 3, how would a bug caused by {} vs set() show up later in the program?
# 2. In Pair 5, when would you want a list result vs a set result?
