# Program Code: SE-CT-03
# Title: Assumption Breaker
# Cognitive Skill: Critical Thinking
# Topic: Sets in Python

# Common wrong beliefs about sets.
# Run each block to BUST or CONFIRM the assumption.

# --- Assumption 1: "Sets keep items in the order I add them" ---
print("=== Assumption 1: Sets preserve insertion order ===")
s = set()
s.add("banana")
s.add("apple")
s.add("mango")
print("Set:", s)
print("BUSTED: Sets are unordered. Order is NOT guaranteed.")
print("Use a list if order matters.\n")

# --- Assumption 2: "{} creates an empty set" ---
print("=== Assumption 2: {} makes an empty set ===")
empty_braces = {}
print("type({})  :", type(empty_braces))    # dict!
empty_set = set()
print("type(set()):", type(empty_set))       # set!
print("BUSTED: {} creates a dict. Use set() for an empty set.\n")

# --- Assumption 3: "Sets can store any data type" ---
print("=== Assumption 3: Sets can store any type ===")
try:
    mixed = {1, "hello", [1, 2]}    # list is unhashable
except TypeError as e:
    print("TypeError:", e)
print("BUSTED: Only IMMUTABLE (hashable) types allowed — no lists or dicts.")
print("Use tuples instead of lists inside sets.\n")

# --- Assumption 4: "You can't convert a set back to a list" ---
print("=== Assumption 4: Can't convert set → list ===")
my_set = {"red", "green", "blue"}
my_list = list(my_set)
print("CONFIRMED WRONG: You CAN convert.", my_list)
print("And sorted() also works:", sorted(my_set), "\n")

# --- Assumption 5: "set1 - set2 is the same as set2 - set1" ---
print("=== Assumption 5: Difference is symmetric ===")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("a - b:", a - b)   # {1, 2}
print("b - a:", b - a)   # {5, 6}
print("BUSTED: Difference is NOT symmetric.")
print("Use ^ (symmetric_difference) if you want both sides combined.\n")

# --- Assumption 6: "Frozen sets can't do set operations" ---
print("=== Assumption 6: frozenset can't do set math ===")
frozen = frozenset({1, 2, 3})
normal = {2, 3, 4}
print("Intersection:", frozen & normal)    # works!
print("Union       :", frozen | normal)    # works!
print("BUSTED: frozenset supports all set operations — just can't be modified.")

# Think:
# 1. Which assumption caught you by surprise? Why?
# 2. When would you use a frozenset instead of a regular set?
