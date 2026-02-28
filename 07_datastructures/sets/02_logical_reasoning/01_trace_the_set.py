# Program Code: SE-LR-01
# Title: Trace the Set
# Cognitive Skill: Logical Reasoning
# Topic: Sets in Python

# Read each block carefully.
# PREDICT the output BEFORE running it.
# Then verify!

# --- Trace 1 ---
print("=== Trace 1 ===")
s = {1, 2, 3, 4, 5}
s.add(3)        # already in set
s.add(6)        # new
s.discard(2)    # removes 2
print(len(s))
# Predicted: ?
# Actual   : 5  (original 5, +6, -2 = 5; 3 ignored as duplicate)

print()

# --- Trace 2 ---
print("=== Trace 2 ===")
a = {"x", "y", "z"}
b = {"y", "z", "w"}
print(a & b)
print(a | b)
print(a - b)
# Predicted (& ): ?   → {'y', 'z'}
# Predicted (| ): ?   → {'x', 'y', 'z', 'w'}
# Predicted (- ): ?   → {'x'}

print()

# --- Trace 3 ---
print("=== Trace 3 ===")
items = ["pen", "book", "pen", "ruler", "book", "pen"]
unique = set(items)
print(len(unique))
print(sorted(unique))
# Predicted len    : ?   → 3
# Predicted sorted : ?   → ['book', 'pen', 'ruler']

print()

# --- Trace 4 ---
print("=== Trace 4 ===")
nums = {10, 20, 30, 40, 50}
result = {n for n in nums if n > 25}
print(result)
# Predicted: ?
# Actual   : {30, 40, 50}

print()

# --- Trace 5 ---
print("=== Trace 5 ===")
class_a = {"Aarav", "Diya", "Karthik"}
class_b = {"Diya", "Riya"}
class_c = class_a | class_b
class_c.discard("Diya")
print(sorted(class_c))
# Predicted: ?
# Actual   : ['Aarav', 'Karthik', 'Riya']

# Think:
# 1. In Trace 1, why didn't adding 3 increase the length?
# 2. In Trace 4, what is this called — set comprehension. Can you write one for even numbers?
