# Assumption Breaker — True or False About Dictionaries?
# These are the most common wrong beliefs beginners hold about dictionaries.
# Run each block to confirm or bust the assumption — then remember the fact!

# Assumption 1: "Dictionaries are always in random order"
# BUSTED — Python 3.7+ preserves the order in which items were added (insertion order)
print("Assumption 1: Order is random")
d = {}
d["c"] = 3
d["a"] = 1
d["b"] = 2
print("Keys in order:", list(d.keys()))
# Output: ['c', 'a', 'b'] — exactly the order they were inserted, not alphabetical!
print("Fact: Dicts preserve INSERTION order since Python 3.7.")
print()

# Assumption 2: "You can use any object as a dictionary key"
# BUSTED — only IMMUTABLE types work as keys (str, int, float, tuple)
# Lists and dicts are MUTABLE — they can change, so Python refuses them as keys
print("Assumption 2: Any object can be a key")
try:
    bad = {[1, 2]: "pair"}         # list is mutable → TypeError
except TypeError as e:
    print("List key → TypeError:", e)

try:
    bad2 = {{"a": 1}: "nested"}    # dict is mutable → TypeError
except TypeError as e:
    print("Dict key → TypeError:", e)

good = {(1, 2): "tuple key works!"}  # tuple is immutable → OK!
print("Tuple key → OK:", good)
print("Fact: Only IMMUTABLE types (str, int, tuple) can be keys.")
print()

# Assumption 3: "dict[key] and dict.get(key) do the same thing"
# BUSTED — [ ] crashes with KeyError for missing keys; .get() returns None safely
print("Assumption 3: [ ] and .get() are identical")
info = {"name": "Diya", "age": 12}
print(info.get("city"))         # None — no crash, key just doesn't exist
try:
    print(info["city"])         # KeyError — crashes! "city" not in dict
except KeyError:
    print("[ ] raised a KeyError!")
print("Fact: .get() is SAFE (returns None/default). [ ] raises KeyError.")
print()

# Assumption 4: "Adding a duplicate key creates two entries"
# BUSTED — keys must be unique. The LAST value wins. No duplicates are ever stored.
print("Assumption 4: Duplicate keys create two entries")
d2 = {"name": "Aarav", "name": "Karthik"}  # "name" defined twice — Python keeps only last
print(d2)                                    # {'name': 'Karthik'} — only one "name" key
d2["name"] = "Diya"                          # assigning again also overwrites
print(d2)
print("Fact: Keys are UNIQUE. The LAST assignment wins. No duplicates.")
print()

# Assumption 5: "It's safe to delete keys while looping over a dict"
# BUSTED — deleting a key while iterating the live dictionary can cause RuntimeError
# SAFE FIX: use list(scores.keys()) to loop over a snapshot, not the live dict
print("Assumption 5: Safe to delete while looping")
scores = {"Aarav": 85, "Diya": 60, "Karthik": 90}
try:
    for name in scores:             # looping directly — DANGEROUS
        if scores[name] < 70:
            del scores[name]        # may trigger RuntimeError
except RuntimeError as e:
    print("RuntimeError:", e)

# Safe version: list() creates a snapshot of keys before we start deleting
scores = {"Aarav": 85, "Diya": 60, "Karthik": 90}
for name in list(scores.keys()):    # snapshot — safe even while modifying the dict
    if scores[name] < 70:
        del scores[name]
print("Safe delete result:", scores)
print("Fact: Always loop over list(dict.keys()) when deleting inside a loop.")
