# Program Code: SE-UN-02
# Title: How Sets Work Internally
# Cognitive Skill: Understanding
# Topic: Sets in Python

# --- Sets are UNORDERED ---
print("=== Sets are unordered ===")
s = {"banana", "apple", "mango", "grapes"}
print("Set:", s)
# The order you see may differ from what you typed.
# There is NO index — you cannot do s[0].
try:
    print(s[0])
except TypeError as e:
    print("No indexing:", e)

print()

# --- Sets store only UNIQUE items ---
print("=== Duplicates are automatically removed ===")
with_dupes = {"cricket", "football", "cricket", "hockey", "football"}
print("Input   : {'cricket', 'football', 'cricket', 'hockey', 'football'}")
print("Stored  :", with_dupes)
print("Len     :", len(with_dupes))   # only 3 unique items

print()

# --- Only IMMUTABLE (hashable) items can be in a set ---
print("=== Only immutable items allowed ===")

# Valid: strings, numbers, tuples
valid_set = {"hello", 42, 3.14, (1, 2)}
print("Valid set:", valid_set)

# Invalid: lists and dicts (mutable — can't be hashed)
try:
    bad = {[1, 2], "ok"}   # list inside a set — ERROR
except TypeError as e:
    print("List in set — TypeError:", e)

print()

# --- frozenset: an IMMUTABLE version of a set ---
print("=== frozenset — read-only set ===")
frozen = frozenset(["red", "green", "blue"])
print("Frozen set:", frozen)
print("Membership:", "red" in frozen)   # True
try:
    frozen.add("yellow")               # cannot modify
except AttributeError as e:
    print("Can't modify frozenset:", e)

print()

# --- Why no duplicates? — Hashing ---
print("=== The hashing idea (simplified) ===")
print("Python converts each item to a unique number (hash).")
print("If two items have the SAME hash, only one is kept.")
print(f"hash('apple') = {hash('apple')}")
print(f"hash('mango') = {hash('mango')}")
print(f"hash(42)      = {hash(42)}")

# Think:
# 1. Why can a tuple be in a set but a list cannot?
# 2. What would happen if you tried to add a dictionary to a set?
