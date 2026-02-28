# Program Code: DC-UN-02
# Title: How Dictionaries Work Internally
# Cognitive Skill: Understanding
# Topic: Dictionaries in Python

# --- Keys must be UNIQUE ---
print("=== Keys must be unique ===")
# If you add the same key twice, the SECOND value wins
d = {"name": "Aarav", "name": "Diya"}
print(d)   # {'name': 'Diya'} — Aarav is overwritten!

print()

# --- Keys must be IMMUTABLE (unchangeable) ---
print("=== Valid vs Invalid key types ===")

# Valid keys: strings, integers, floats, tuples (immutable)
valid = {
    "name":   "Aarav",    # string key ✓
    42:       "Answer",   # integer key ✓
    3.14:     "Pi",       # float key ✓
    (1, 2):   "Coords",   # tuple key ✓
}
print("Valid keys:", list(valid.keys()))

# Invalid keys: lists, dicts (mutable — they can change)
try:
    invalid = {[1, 2]: "pair"}   # list as key — ERROR!
except TypeError as e:
    print("List as key:", e)

print()

# --- Values can be ANYTHING ---
print("=== Values can be any type ===")
student = {
    "name":     "Aarav",                     # string
    "age":      13,                           # int
    "marks":    [85, 90, 78],                 # list
    "address":  {"city": "Chennai", "pin": 600001},  # nested dict
    "active":   True,                         # bool
}
print("Name:", student["name"])
print("Marks list:", student["marks"])
print("City:", student["address"]["city"])

print()

# --- Dictionaries maintain INSERTION ORDER (Python 3.7+) ---
print("=== Insertion order is preserved ===")
menu = {}
menu["idli"]  = 15
menu["dosa"]  = 30
menu["chai"]  = 10
for item, price in menu.items():
    print(f"  {item}: Rs.{price}")
# Items appear in the order they were added

print()

# --- Modifying while iterating is DANGEROUS ---
print("=== Never modify dict while looping over it ===")
scores = {"Aarav": 85, "Diya": 72, "Karthik": 90}
# Safe way: loop over a copy of keys
for name in list(scores.keys()):
    if scores[name] < 80:
        del scores[name]    # remove low scorers
print("High scorers only:", scores)

# Think:
# 1. Why can't you use a list as a dictionary key?
# 2. What happens if two keys have the same name?
