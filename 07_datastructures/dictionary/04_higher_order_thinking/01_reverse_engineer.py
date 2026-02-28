# Program Code: DC-HOT-01
# Title: Reverse Engineer the Dictionary
# Cognitive Skill: Higher Order Thinking
# Topic: Dictionaries in Python

# Study the OUTPUT below. Write the code that produced it.
# Then compare your solution with the reference at the bottom.

# --- Challenge 1 ---
# Output:
#   {'a': 1, 'b': 4, 'c': 9}
#
# The values are squares of 1, 2, 3.
# The keys are 'a', 'b', 'c'.

print("=== Challenge 1 — Write code to get this output ===")
print("{'a': 1, 'b': 4, 'c': 9}")
print()

# Your solution here:
keys   = ['a', 'b', 'c']
values = [1, 2, 3]
result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i] ** 2
print("Your result:", result)

print()

# --- Challenge 2 ---
# Output:
#   {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

print("=== Challenge 2 — Odd/even labels ===")
print("{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}")
print()

# Your solution here:
labels = {}
for n in range(1, 6):
    labels[n] = "even" if n % 2 == 0 else "odd"
print("Your result:", labels)

print()

# --- Challenge 3 ---
# Output:
#   Cricket team  : ['Aarav', 'Karthik']
#   Football team : ['Diya', 'Riya']

print("=== Challenge 3 — Group by sport ===")
print("Cricket team  : ['Aarav', 'Karthik']")
print("Football team : ['Diya', 'Riya']")
print()

# Input data
players = [
    ("Aarav",   "Cricket"),
    ("Diya",    "Football"),
    ("Karthik", "Cricket"),
    ("Riya",    "Football"),
]

# Your solution here:
teams = {}
for name, sport in players:
    if sport not in teams:
        teams[sport] = []
    teams[sport].append(name)

for sport, names in teams.items():
    print(f"  {sport:15}: {names}")

print()

# --- Challenge 4 — Reverse a dictionary ---
# Input : {"apple": "red", "banana": "yellow", "grape": "purple"}
# Output: {"red": "apple", "yellow": "banana", "purple": "grape"}

print("=== Challenge 4 — Reverse keys and values ===")
original = {"apple": "red", "banana": "yellow", "grape": "purple"}
flipped  = {}

# Your solution here:
for fruit, colour in original.items():
    flipped[colour] = fruit

print("Original:", original)
print("Flipped :", flipped)

# Think:
# 1. In Challenge 4, what would go wrong if two fruits had the same colour?
# 2. Can you rewrite Challenge 2 in one line using a dict comprehension?
