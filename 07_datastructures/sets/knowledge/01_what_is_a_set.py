# Program Code: SE-KN-01
# Title: What Is a Set?
# Cognitive Skill: Knowledge
# Topic: Sets in Python

# A SET is a collection that is:
#   1. UNORDERED  — items have no fixed position (no index)
#   2. UNIQUE     — no duplicates allowed
#   3. MUTABLE    — you can add/remove items after creation

# --- Creating a set with {} ---
fruits = {"mango", "banana", "apple", "banana", "mango"}
print("Fruits set:", fruits)
# Notice: duplicates are automatically removed!
# Notice: order may differ each time you run

print()

# --- An empty set ---
# IMPORTANT: {} creates an empty DICT, not a set!
empty_wrong = {}            # this is a dict
empty_right = set()         # this is a set
print("type({})  :", type(empty_wrong))    # <class 'dict'>
print("type(set()):", type(empty_right))   # <class 'set'>

print()

# --- Creating a set from a list ---
numbers_list = [1, 2, 3, 2, 1, 4, 3]
numbers_set  = set(numbers_list)
print("From list:", numbers_list)
print("As set   :", numbers_set)    # duplicates removed automatically

print()

# --- Real-life analogy ---
print("=== Real-life analogy ===")
print("Think of a SET like a box where only ONE of each item is allowed.")
print("If you try to put in a second banana, it is simply ignored.")
print()

# --- Checking membership ---
colours = {"red", "green", "blue"}
print("Is 'red' in colours?   ", "red" in colours)     # True
print("Is 'yellow' in colours?", "yellow" in colours)  # False

print()
print("Number of items in set:", len(colours))

# Think:
# 1. Why would you use a set instead of a list to store student roll numbers?
# 2. What happens if you do set("hello")? Try it!
