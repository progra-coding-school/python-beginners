# How Sets Work Internally
# Sets are unordered (no index), store only unique items, and require hashable (immutable) elements.
# frozenset is the immutable, read-only version of a set.

# --- Sets are UNORDERED ---
# Python stores items in whatever order it chooses based on hashing — not your insertion order
print("Sets are unordered:")
s = {"banana", "apple", "mango", "grapes"}
print("Set:", s)
# The order you see may differ from what you typed. There is NO index — you cannot do s[0].
try:
    print(s[0])
except TypeError as e:
    print("No indexing:", e)

print()

# --- Sets store only UNIQUE items ---
# Duplicates are silently discarded — only one copy of each value is kept
print("Duplicates are automatically removed:")
with_dupes = {"cricket", "football", "cricket", "hockey", "football"}
print("Input   : {'cricket', 'football', 'cricket', 'hockey', 'football'}")
print("Stored  :", with_dupes)
print("Len     :", len(with_dupes))   # only 3 unique items

print()

# --- Only IMMUTABLE (hashable) items can be in a set ---
# Strings, numbers, and tuples are immutable → they can be hashed → they work in sets
# Lists and dicts are mutable → cannot be hashed → they raise TypeError
print("Only immutable items allowed:")

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
# A frozenset can never be changed — useful as a dict key or set element
print("frozenset — read-only set:")
frozen = frozenset(["red", "green", "blue"])
print("Frozen set:", frozen)
print("Membership:", "red" in frozen)   # True — membership check still works
try:
    frozen.add("yellow")               # cannot modify — AttributeError
except AttributeError as e:
    print("Can't modify frozenset:", e)

print()

# --- Why no duplicates? — Hashing ---
# Python converts each item to a number (its hash). If two items have the SAME hash, only one is kept.
# Each item maps to a slot — like a pigeonhole. Same slot = same item = kept once.
print("The hashing idea (simplified):")
print("Python converts each item to a unique number (hash).")
print("If two items have the SAME hash, only one is kept.")
print("hash('apple') =", hash('apple'))
print("hash('mango') =", hash('mango'))
print("hash(42)      =", hash(42))

# Think:
# 1. Why can a tuple be in a set but a list cannot?
# 2. What would happen if you tried to add a dictionary to a set?
