# Program Code: SE-LR-03
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning
# Topic: Sets in Python

# Write your prediction on paper FIRST.
# Then run each block to verify.

# --- Challenge 1 ---
print("=== Challenge 1 ===")
s = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(len(s))
# Predict: ?
# Answer : 7  (duplicates 1 and 5 removed)

print()

# --- Challenge 2 ---
print("=== Challenge 2 ===")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a ^ b)
# Predict: ?
# Answer : {1, 2, 5, 6}  (items in a or b but NOT both)

print()

# --- Challenge 3 ---
print("=== Challenge 3 ===")
words = "the cat sat on the mat".split()
print(len(set(words)))
# Predict: ?
# Answer : 5  ('the' is duplicate; unique: the, cat, sat, on, mat)

print()

# --- Challenge 4 ---
print("=== Challenge 4 ===")
x = {10, 20, 30}
y = {20, 30, 40}
print(x.issubset(y))
print(x.issuperset(y))
print(x.isdisjoint(y))
# Predict each line: ?
# Answers: False | False | False  (they share 20, 30 but neither is a subset)

print()

# --- Challenge 5 (tricky!) ---
print("=== Challenge 5 ===")
s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
print(s1 == s2)             # same elements?
print(s1.issubset(s3))      # s1 fits inside s3?
print(s1 == s3)             # same?
# Predict: ?
# Answers: True | True | False

print()

# --- Challenge 6 ---
print("=== Challenge 6 ===")
letters = set("python")
letters.discard("p")
letters.discard("z")        # 'z' not in set — no error
print(sorted(letters))
# Predict: ?
# Answer : ['h', 'n', 'o', 't', 'y']

# Think:
# 1. In Challenge 3, what would len(words) give without set()? Why the difference?
# 2. In Challenge 5, two sets are equal (==) but one is a subset of the other — how is that possible?
