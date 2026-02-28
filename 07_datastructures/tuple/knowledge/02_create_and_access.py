# Program Code: TU-KN-02
# Title: Create and Access a Tuple
# Cognitive Skill: Knowledge
# Topic: Tuples in Python

# --- 4 ways to create a tuple ---

# Way 1: parentheses with values
fruits = ("mango", "banana", "apple", "grapes")
print("Way 1 — ()      :", fruits)

# Way 2: tuple packing (no parentheses)
scores = 85, 90, 78, 92
print("Way 2 — packing :", scores)

# Way 3: tuple() from a list
from_list = tuple([10, 20, 30, 40])
print("Way 3 — tuple() :", from_list)

# Way 4: tuple() from a string (each character)
from_str  = tuple("hello")
print("Way 4 — string  :", from_str)

print()

# --- Indexing (same as lists) ---
print("=== Indexing ===")
colours = ("red", "green", "blue", "yellow", "orange")
print("First  [0] :", colours[0])       # red
print("Last   [-1]:", colours[-1])      # orange
print("Third  [2] :", colours[2])       # blue

print()

# --- Slicing ===
print("=== Slicing ===")
print("First 3    :", colours[:3])      # ('red', 'green', 'blue')
print("Last 2     :", colours[-2:])     # ('yellow', 'orange')
print("Every other:", colours[::2])     # ('red', 'blue', 'orange')

print()

# --- Checking membership ---
print("=== Membership ===")
print("'green' in colours  :", "green" in colours)    # True
print("'purple' in colours :", "purple" in colours)   # False

print()

# --- Length ---
print("Length:", len(colours))

print()

# --- Nested tuple access ---
print("=== Nested tuple ===")
student = ("Aarav", (85, 90, 78))      # name, marks tuple inside
print("Name  :", student[0])
print("Marks :", student[1])
print("First mark:", student[1][0])    # 85

# Think:
# 1. What is the difference between colours[1] and colours[1:2]?
# 2. What would tuple("banana") produce? Try to predict before running.
