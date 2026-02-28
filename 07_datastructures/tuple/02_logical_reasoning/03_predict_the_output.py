# Program Code: TU-LR-03
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning
# Topic: Tuples in Python

# Write your prediction on paper FIRST.
# Then run each block to verify.

# --- Challenge 1 ---
print("=== Challenge 1 ===")
t = (5, 10, 15, 20, 25)
print(t[::2])
print(t[::-1])
# Predict both: ?
# Answers: (5, 15, 25) | (25, 20, 15, 10, 5)

print()

# --- Challenge 2 ---
print("=== Challenge 2 ===")
a = (1, 2)
b = a * 3
print(b)
print(len(b))
# Predict: ?
# Answers: (1, 2, 1, 2, 1, 2) | 6

print()

# --- Challenge 3 ---
print("=== Challenge 3 ===")
data = (("Aarav", 85), ("Diya", 92), ("Karthik", 78))
for record in data:
    name, score = record
    print(f"{name}: {score}")
# Predict: ?
# Answers: Aarav: 85 | Diya: 92 | Karthik: 78

print()

# --- Challenge 4 ---
print("=== Challenge 4 ===")
t = (10, 20, 30)
try:
    t[1] = 99
except TypeError as e:
    print("Error:", e)
print(t)
# Predict: what error message? Is t unchanged?
# Answer: TypeError: 'tuple' object does not support item assignment | (10, 20, 30)

print()

# --- Challenge 5 ---
print("=== Challenge 5 ===")
first, *middle, last = (1, 2, 3, 4, 5, 6)
print(first)
print(middle)
print(last)
# Predict each: ?
# Answers: 1 | [2, 3, 4, 5] | 6

print()

# --- Challenge 6 (tricky!) ---
print("=== Challenge 6 ===")
single = (42)       # is this a tuple?
pair   = (42,)      # is this a tuple?
print(type(single))
print(type(pair))
print(single + 1)   # works if int
try:
    print(pair + (1,))  # tuple concatenation
except:
    pass
# Predict both types and the results: ?
# Answers: <class 'int'> | <class 'tuple'> | 43 | (42, 1)

# Think:
# 1. In Challenge 6, why does (42) NOT create a tuple?
# 2. In Challenge 5, why does *middle collect a LIST, not a tuple?
