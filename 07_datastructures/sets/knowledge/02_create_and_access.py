# Program Code: SE-KN-02
# Title: Create and Access a Set
# Cognitive Skill: Knowledge
# Topic: Sets in Python

# --- 3 ways to create a set ---

# Way 1: curly braces {}
sports = {"cricket", "football", "hockey", "tennis"}
print("Way 1 — {}      :", sports)

# Way 2: set() from a list
subjects = set(["Maths", "Science", "English", "Maths"])   # duplicate removed
print("Way 2 — set()   :", subjects)

# Way 3: set() from a string (each character becomes an element)
letters = set("hello")
print("Way 3 — string  :", letters)    # {'h', 'e', 'l', 'o'} — duplicate 'l' removed

print()

# --- Accessing items ---
print("=== Accessing items ===")
# Sets have NO index — you CANNOT do sports[0]
try:
    print(sports[0])
except TypeError as e:
    print("TypeError:", e)

# Correct way: use 'in' to check membership
print("Is 'cricket' in sports?", "cricket" in sports)     # True
print("Is 'chess' in sports?  ", "chess" in sports)       # False

print()

# --- Looping through a set ---
print("=== Looping through a set ===")
colours = {"red", "green", "blue", "yellow"}
for colour in colours:
    print(" ", colour)
# Note: order is NOT guaranteed

print()

# --- len() and other checks ---
print("=== Size and checks ===")
print("Number of sports:", len(sports))
print("Is set empty?    ", len(sports) == 0)

empty = set()
print("Empty set:", empty)
print("Is empty? ", not empty)   # True when empty

# Think:
# 1. Why can't you access a set item with an index like sports[0]?
# 2. What would set("banana") produce? Predict before running.
