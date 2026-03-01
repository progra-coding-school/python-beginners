# Spot the Bug
# Each block has ONE bug. Identify what is wrong and WHY the code will fail.
# Understanding common dictionary bugs helps you write safer code from the start.
# Bugs covered: wrong case key, () vs [], del then access, modify while loop, list as key.

# Bug 1: KeyError — dictionary keys are case-sensitive
# "Age" and "age" are DIFFERENT keys. The dict has "age" (lowercase) only.
print("Bug 1:")
student = {"name": "Aarav", "age": 13, "grade": 7}
# Buggy: print(student["Age"])   ← capital A — "Age" is not the same as "age"
# Fix: use the exact key as defined in the dictionary
print(student["age"])       # correct — lowercase matches the key exactly

print()

# Bug 2: () vs [] — parentheses call a function, brackets access a dict
# prices("apple") tries to CALL prices like a function — but it's a dictionary!
print("Bug 2:")
prices = {"mango": 120, "banana": 40}
# Buggy: prices("apple") = 80   ← () is a function call, not dict access
# Fix: use square brackets [] for dictionary assignment
prices["apple"] = 80
print(prices)

print()

# Bug 3: del then access — del removes first, leaving nothing to read
# After del scores["Karthik"], trying to read scores["Karthik"] → KeyError!
# Solution: use .pop() which removes AND returns the value in ONE step.
print("Bug 3:")
scores = {"Aarav": 85, "Diya": 92, "Karthik": 78}
# Buggy:
#   del scores["Karthik"]
#   saved = scores["Karthik"]   ← KeyError — key was already deleted!
# Fix: .pop() removes AND saves the value at the same time
saved = scores.pop("Karthik")
print("Saved score:", saved)
print("Remaining:", scores)

print()

# Bug 4: modifying a dictionary while looping directly over it
# Python's internal state can break → RuntimeError in some Python versions
# Fix: loop over list(menu.keys()) which creates a SNAPSHOT of the keys first
print("Bug 4:")
menu = {"idli": 15, "dosa": 30}
# Buggy: for item in menu: menu[item] *= 2   ← modifying while iterating is dangerous
# Fix: wrap keys in list() to create a safe copy of keys before looping
for item in list(menu.keys()):   # list() snapshot — safe to modify menu now
    menu[item] *= 2
print("Doubled prices:", menu)

print()

# Bug 5: list as a dictionary key
# Lists are MUTABLE — they can change. Dictionary keys must be IMMUTABLE.
# Python raises TypeError when you try to use a list or dict as a key.
# Fix: use a TUPLE instead — looks like a list but is immutable.
print("Bug 5:")
try:
    bad_dict = {[1, 2, 3]: "coordinates"}  # list as key → TypeError!
except TypeError as e:
    print("TypeError caught:", e)
    print("Fix: use a TUPLE as the key instead.")
    good_dict = {(1, 2, 3): "coordinates"}  # tuple key — immutable and allowed
    print("Good dict:", good_dict)
