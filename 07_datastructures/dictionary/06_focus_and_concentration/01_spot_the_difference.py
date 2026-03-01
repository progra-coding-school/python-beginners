# Spot the Difference — Two Versions of Similar Code
# Find every difference between Version A and Version B in each pair.
# Some differences cause BUGS. Some are just style choices.
# This trains the precise reading skills needed for code review and debugging.

# Pair 1: capitalisation in keys
# "name" and "Name" are DIFFERENT keys — dictionaries are case-sensitive!
# .get("name") on a dict with key "Name" (capital N) returns None
print("Pair 1:")
a = {"name": "Aarav", "age": 13}
print(a.get("name"))        # "Aarav" — key "name" matches exactly

b = {"Name": "Aarav", "age": 13}   # capital N in "Name"!
print(b.get("name"))        # None   — "name" (lowercase) is not the same as "Name"
# Difference: key is "Name" (capital N) in B. .get("name") returns None.

print()

# Pair 2: adding a new key vs updating an existing key
# A adds "Karthik" (new key) → length increases from 2 to 3
# B updates "Diya" (existing key) → same 2 keys, length stays 2
print("Pair 2:")
scores_a = {"Aarav": 85, "Diya": 90}
scores_a["Karthik"] = 78            # new key added → dict grows
print(len(scores_a))                # 3

scores_b = {"Aarav": 85, "Diya": 90}
scores_b.update({"Diya": 78})       # existing key updated → dict size unchanged
print(len(scores_b))                # 2
# Difference: A adds a new key (Karthik), B updates an existing key (Diya). Length differs.

print()

# Pair 3: safe loop vs dangerous loop when deleting keys
# A: list(data_a.keys()) creates a SNAPSHOT — safe to delete while iterating
# B: looping over live keys while deleting → RuntimeError in some Python versions
print("Pair 3:")

data_a = {"x": 1, "y": 2, "z": 3}
for k in list(data_a.keys()):   # list() creates a safe copy of the keys
    if data_a[k] < 2:
        del data_a[k]
print("A:", data_a)    # {'y': 2, 'z': 3}

data_b = {"x": 1, "y": 2, "z": 3}
try:
    for k in data_b.keys():     # looping live dict while deleting — dangerous!
        if data_b[k] < 2:
            del data_b[k]
    print("B:", data_b)
except RuntimeError as e:
    print("B: RuntimeError —", e)
# Difference: A wraps keys in list() (safe snapshot); B loops directly (risky).

print()

# Pair 4: two ways to return a default for a missing key
# Both produce "Not available" — but B is shorter and more Pythonic
print("Pair 4:")

menu_a = {"idli": 15, "dosa": 30}
print(menu_a["chai"] if "chai" in menu_a else "Not available")   # check first, then access

menu_b = {"idli": 15, "dosa": 30}
print(menu_b.get("chai", "Not available"))   # .get() with default — one clean line
# Difference: Different syntax, same result. B is shorter and more Pythonic.
