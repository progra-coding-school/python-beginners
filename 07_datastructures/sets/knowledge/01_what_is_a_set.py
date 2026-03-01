# What Is a Set?
# A set is a collection that is UNORDERED (no index), UNIQUE (no duplicates), and MUTABLE (add/remove items).
# Use a set when you care about membership and uniqueness, not position.

# --- Creating a set with {} ---
# Duplicates are automatically removed — only one of each value is kept
fruits = {"mango", "banana", "apple", "banana", "mango"}
print("Fruits set:", fruits)
# Notice: duplicates removed. Notice: order may differ each run — sets are unordered.

print()

# --- An empty set ---
# IMPORTANT: {} creates an empty DICT, not a set — this is a very common mistake!
empty_wrong = {}            # this is a dict
empty_right = set()         # this is a set — must use set()
print("type({})  :", type(empty_wrong))    # <class 'dict'>
print("type(set()):", type(empty_right))   # <class 'set'>

print()

# --- Creating a set from a list ---
# set() strips duplicates from any iterable — useful for cleaning up lists
numbers_list = [1, 2, 3, 2, 1, 4, 3]
numbers_set  = set(numbers_list)
print("From list:", numbers_list)
print("As set   :", numbers_set)    # duplicates removed automatically

print()

# --- Real-life analogy ---
# Think of a SET like a box where only ONE of each item is allowed.
# If you try to put in a second banana, it is simply ignored.
print("Think of a SET like a box where only ONE of each item is allowed.")
print("If you try to put in a second banana, it is simply ignored.")
print()

# --- Checking membership ---
# 'in' is the main way to query a set — fast, clear, and works for any size
colours = {"red", "green", "blue"}
print("Is 'red' in colours?   ", "red" in colours)     # True
print("Is 'yellow' in colours?", "yellow" in colours)  # False

print()
print("Number of items in set:", len(colours))

# Think:
# 1. Why would you use a set instead of a list to store student roll numbers?
# 2. What happens if you do set("hello")? Try it!
