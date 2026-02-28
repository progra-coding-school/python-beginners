# Program Code: DC-LR-01
# Title: Trace the Dictionary
# Cognitive Skill: Logical Reasoning
# Topic: Dictionaries in Python

# Read each code block carefully.
# PREDICT the output BEFORE running it.
# Then run and check if you were right!

# --- Trace 1 ---
print("=== Trace 1 ===")
d = {"a": 1, "b": 2, "c": 3}
d["b"] = 20
d["d"] = 4
del d["a"]
print(d)
# Predicted output: ?
# Actual output  : {'b': 20, 'c': 3, 'd': 4}

print()

# --- Trace 2 ---
print("=== Trace 2 ===")
scores = {"Aarav": 85, "Diya": 90}
scores.update({"Diya": 95, "Karthik": 78})
print(scores)
# Predicted: ?
# Actual   : {'Aarav': 85, 'Diya': 95, 'Karthik': 78}

print()

# --- Trace 3 ---
print("=== Trace 3 ===")
info = {"name": "Riya", "age": 12}
val  = info.pop("age")
print("Popped:", val)
print("Dict now:", info)
# Predicted popped: ?   Dict: ?
# Actual   popped: 12   Dict: {'name': 'Riya'}

print()

# --- Trace 4 ---
print("=== Trace 4 ===")
prices = {"mango": 120, "banana": 40, "apple": 80}
total  = 0
for item, cost in prices.items():
    if cost < 100:
        total += cost
print("Total of items under Rs.100:", total)
# Predicted: ?
# Actual   : 120  (banana 40 + apple 80)

print()

# --- Trace 5 ---
print("=== Trace 5 ===")
bag = {}
items = ["pen", "book", "pen", "eraser", "book", "pen"]
for item in items:
    bag[item] = bag.get(item, 0) + 1
print(bag)
# Predicted: ?
# Actual   : {'pen': 3, 'book': 2, 'eraser': 1}

# Think:
# 1. In Trace 1, why is 'a' gone but 'b' has value 20 and not 2?
# 2. In Trace 4, why is the total 120 and not 40 + 80 = 120? (Confirm your working.)
