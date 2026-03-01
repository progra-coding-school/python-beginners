# How Dictionaries Work
# Understanding the internal rules prevents hard-to-find bugs.
# Rules to remember:
#   Keys must be UNIQUE — adding the same key twice overwrites the first value
#   Keys must be IMMUTABLE — strings, ints, tuples are OK; lists and dicts are NOT
#   Values can be ANYTHING — any type is allowed as a value
#   Order is PRESERVED — Python 3.7+ remembers the order items were added

# Rule 1: Keys must be unique — the second value OVERWRITES the first
# If you use the same key twice, you don't get two entries — you get one updated entry
print("Keys must be unique:")
d = {"name": "Aarav", "name": "Diya"}   # "name" appears twice at creation
print(d)   # {'name': 'Diya'} — "Aarav" is overwritten silently!

print()

# Rule 2: Keys must be immutable (cannot change after creation)
# Valid key types: strings (str), integers (int), floats (float), tuples
# Invalid key types: lists (mutable — can change), dictionaries (mutable)
print("Valid vs invalid key types:")
valid = {
    "name":   "Aarav",    # string key — OK
    42:       "Answer",   # integer key — OK
    3.14:     "Pi",       # float key — OK
    (1, 2):   "Coords",   # tuple key — OK (tuples are immutable)
}
print("Valid keys:", list(valid.keys()))

# Using a list as a key causes TypeError — lists can change, so Python refuses them
try:
    invalid = {[1, 2]: "pair"}   # list as key — ERROR!
except TypeError as e:
    print("List as key:", e)

print()

# Rule 3: Values can be any type — strings, numbers, booleans, lists, nested dicts!
print("Values can be any type:")
student = {
    "name":     "Aarav",                              # string value
    "age":      13,                                   # int value
    "marks":    [85, 90, 78],                         # list value
    "address":  {"city": "Chennai", "pin": 600001},   # nested dict as value!
    "active":   True,                                 # bool value
}
print("Name:", student["name"])
print("Marks list:", student["marks"])
print("City:", student["address"]["city"])   # access nested dict with two keys

print()

# Rule 4: Insertion order is preserved in Python 3.7+
# Items appear in the same order you added them — no random shuffling
print("Insertion order is preserved:")
menu = {}
menu["idli"]  = 15
menu["dosa"]  = 30
menu["chai"]  = 10
for item, price in menu.items():
    print("  " + item + ": Rs." + str(price))

print()

# Rule 5: Never delete keys while looping directly over the live dictionary
# Python's internal state can break → RuntimeError
# SAFE FIX: use list(scores.keys()) to take a snapshot of keys before looping
print("Safe way to delete while looping:")
scores = {"Aarav": 85, "Diya": 72, "Karthik": 90}
for name in list(scores.keys()):    # list() takes a snapshot — safe to delete now
    if scores[name] < 80:
        del scores[name]            # modifying the dict is fine — we loop over the copy
print("High scorers only:", scores)
