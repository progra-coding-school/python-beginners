# Program Code: TU-LR-01
# Title: Trace the Tuple
# Cognitive Skill: Logical Reasoning
# Topic: Tuples in Python

# Read each block carefully.
# PREDICT the output BEFORE running it.
# Then verify!

# --- Trace 1 ---
print("=== Trace 1 ===")
t = (10, 20, 30, 40, 50)
print(t[1])
print(t[-1])
print(t[1:4])
# Predicted: ?
# Actual   : 20 | 50 | (20, 30, 40)

print()

# --- Trace 2 ---
print("=== Trace 2 ===")
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(len(c))
print(c[3])
# Predicted: ?
# Actual   : 6 | 4

print()

# --- Trace 3 ---
print("=== Trace 3 ===")
nums = (3, 1, 4, 1, 5, 9, 2, 6, 5)
print(nums.count(1))
print(nums.count(5))
print(nums.index(4))
# Predicted: ?
# Actual   : 2 | 2 | 2

print()

# --- Trace 4 ---
print("=== Trace 4 ===")
record = ("Aarav", 13, "Chennai")
name, age, city = record
print(f"{name} is {age} from {city}")
# Predicted: ?
# Actual   : Aarav is 13 from Chennai

print()

# --- Trace 5 ---
print("=== Trace 5 ===")
data = (10, 20, 30, 40, 50)
first, *rest = data
print("First:", first)
print("Rest :", rest)
# Predicted: ?
# Actual   : First: 10 | Rest: [20, 30, 40, 50]  (rest is a LIST!)

print()

# --- Trace 6 (tricky!) ---
print("=== Trace 6 ===")
x, y = 5, 10
x, y = y, x
print(x, y)
# Predicted: ?
# Actual   : 10 5  — they swapped!

# Think:
# 1. In Trace 5, why is `rest` a list and not a tuple?
# 2. In Trace 6, what temporary tuple does Python create to do the swap?
