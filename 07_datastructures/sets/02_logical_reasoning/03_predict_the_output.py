# Predict the Output
# Write your prediction on paper FIRST. Then run each block to verify.
# Self-testing is the fastest way to find gaps in your understanding.

# --- Challenge 1 ---
# Sets remove duplicates — count the unique values, not the total items
print("Challenge 1:")
s = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(len(s))
# Predict: ?
# Answer : 7  (duplicates 1 and 5 removed — unique values are 1,2,3,4,5,6,9)

print()

# --- Challenge 2 ---
# ^ symmetric difference: items that are in a OR b, but NOT in both
print("Challenge 2:")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a ^ b)
# Predict: ?
# Answer : {1, 2, 5, 6}  (3 and 4 are in both → excluded)

print()

# --- Challenge 3 ---
# .split() turns a sentence into a list of words; set() removes duplicate words
print("Challenge 3:")
words = "the cat sat on the mat".split()
print(len(set(words)))
# Predict: ?
# Answer : 5  ('the' appears twice → deduplicated; unique: the, cat, sat, on, mat)

print()

# --- Challenge 4 ---
# issubset → every item of x must be in y. issuperset → reverse. isdisjoint → no overlap.
print("Challenge 4:")
x = {10, 20, 30}
y = {20, 30, 40}
print(x.issubset(y))     # not all of x is in y (10 missing)
print(x.issuperset(y))   # not all of y is in x (40 missing)
print(x.isdisjoint(y))   # they share 20 and 30 — not disjoint
# Predict each line: ?
# Answers: False | False | False

print()

# --- Challenge 5 (tricky!) ---
# Two sets with the SAME elements are equal (==). A proper subset is smaller but fully inside.
print("Challenge 5:")
s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
print(s1 == s2)             # same elements → equal
print(s1.issubset(s3))      # s1 fits inside s3 (s3 has all of s1 plus more)
print(s1 == s3)             # s1 has 3 items, s3 has 4 — NOT the same
# Predict: ?
# Answers: True | True | False

print()

# --- Challenge 6 ---
# set("python") creates a set of unique characters; discard("z") is silent if missing
print("Challenge 6:")
letters = set("python")
letters.discard("p")
letters.discard("z")        # 'z' not in set — no error with discard
print(sorted(letters))
# Predict: ?
# Answer : ['h', 'n', 'o', 't', 'y']  ('p' removed; 'z' silently ignored)

# Think:
# 1. In Challenge 3, what would len(words) give without set()? Why the difference?
# 2. In Challenge 5, two sets are equal (==) but one is a subset of the other — how is that possible?
