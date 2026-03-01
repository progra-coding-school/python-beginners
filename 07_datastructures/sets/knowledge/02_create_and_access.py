# Create and Access a Set
# Three ways to create sets. Sets have NO index — use 'in' to check membership, loop to visit items.

# --- 3 ways to create a set ---

# Way 1: curly braces {} — most common when you know the items upfront
sports = {"cricket", "football", "hockey", "tennis"}
print("Way 1 — {}      :", sports)

# Way 2: set() from a list — useful for removing duplicates from an existing list
subjects = set(["Maths", "Science", "English", "Maths"])   # duplicate removed
print("Way 2 — set()   :", subjects)

# Way 3: set() from a string — each CHARACTER becomes an element (duplicate letters removed)
letters = set("hello")
print("Way 3 — string  :", letters)    # {'h', 'e', 'l', 'o'} — duplicate 'l' removed

print()

# --- Accessing items ---
# Sets have NO index — you CANNOT do sports[0]
# Trying to index a set raises TypeError
try:
    print(sports[0])
except TypeError as e:
    print("TypeError:", e)

# Correct way: use 'in' to check membership — fast and readable
print("Is 'cricket' in sports?", "cricket" in sports)     # True
print("Is 'chess' in sports?  ", "chess" in sports)       # False

print()

# --- Looping through a set ---
# You can iterate over a set with for — but order is NOT guaranteed
colours = {"red", "green", "blue", "yellow"}
print("Looping through a set:")
for colour in colours:
    print(" ", colour)
# Note: order is NOT guaranteed — it may differ each run

print()

# --- len() and other checks ---
print("Number of sports:", len(sports))
print("Is set empty?    ", len(sports) == 0)

# Empty check — an empty set is falsy in Python
empty = set()
print("Empty set:", empty)
print("Is empty? ", not empty)   # True when empty

# Think:
# 1. Why can't you access a set item with an index like sports[0]?
# 2. What would set("banana") produce? Predict before running.
