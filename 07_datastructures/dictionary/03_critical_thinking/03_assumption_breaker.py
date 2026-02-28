# Program Code: DC-CT-03
# Title: Assumption Breaker
# Cognitive Skill: Critical Thinking
# Topic: Dictionaries in Python

# Common wrong beliefs about dictionaries.
# Read the assumption, then run the code to BUST or CONFIRM it.

# --- Assumption 1: "Dictionaries are always in random order" ---
print("=== Assumption 1: Order is random ===")
d = {}
d["c"] = 3
d["a"] = 1
d["b"] = 2
print("Keys in order:", list(d.keys()))
# BUSTED: Python 3.7+ preserves insertion order.
# Output: ['c', 'a', 'b'] — the order items were added.
print("Fact: Dicts preserve INSERTION order since Python 3.7.\n")

# --- Assumption 2: "You can use any object as a key" ---
print("=== Assumption 2: Any object can be a key ===")
try:
    bad = {[1, 2]: "pair"}         # list — mutable
except TypeError as e:
    print(f"List key → TypeError: {e}")

try:
    bad2 = {{"a": 1}: "nested"}    # dict — mutable
except TypeError as e:
    print(f"Dict key → TypeError: {e}")

good = {(1, 2): "tuple key works!"}  # tuple — immutable
print(f"Tuple key → OK: {good}")
print("Fact: Only IMMUTABLE types (str, int, tuple) can be keys.\n")

# --- Assumption 3: "dict[key] and dict.get(key) do the same thing" ---
print("=== Assumption 3: [ ] and .get() are identical ===")
info = {"name": "Diya", "age": 12}

print(info.get("city"))         # None — no crash
try:
    print(info["city"])         # KeyError — CRASH
except KeyError:
    print("[ ] raised a KeyError!")
print("Fact: .get() is SAFE (returns None/default). [ ] raises KeyError.\n")

# --- Assumption 4: "Adding a duplicate key creates two entries" ---
print("=== Assumption 4: Duplicate keys create two entries ===")
d2 = {"name": "Aarav", "name": "Karthik"}  # same key twice at creation
print(d2)
d2["name"] = "Diya"                         # assign again
print(d2)
print("Fact: Keys are UNIQUE. The LAST assignment wins. No duplicates.\n")

# --- Assumption 5: "Looping a dict and deleting is always safe" ---
print("=== Assumption 5: Safe to delete while looping ===")
scores = {"Aarav": 85, "Diya": 60, "Karthik": 90}
try:
    for name in scores:             # looping directly
        if scores[name] < 70:
            del scores[name]        # DANGEROUS — RuntimeError in some versions
except RuntimeError as e:
    print(f"RuntimeError: {e}")

# Safe fix: loop over a snapshot of keys
scores = {"Aarav": 85, "Diya": 60, "Karthik": 90}
for name in list(scores.keys()):    # snapshot with list()
    if scores[name] < 70:
        del scores[name]
print("Safe delete result:", scores)
print("Fact: Always loop over list(dict.keys()) when deleting inside a loop.")

# Think:
# 1. Which assumption surprised you the most? Why?
# 2. How would you explain to a friend why lists can't be dictionary keys?
