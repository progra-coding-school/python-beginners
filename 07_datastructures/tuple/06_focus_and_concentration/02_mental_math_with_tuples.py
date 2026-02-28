# Program Code: TU-FC-02
# Title: Mental Math with Tuples
# Cognitive Skill: Focus and Concentration
# Topic: Tuples in Python

# Work through each problem IN YOUR HEAD first.
# Only run to check your answer.

print("=== Mental Math with Tuples ===")
print("Answer each question before running!\n")

# --- Q1: Indexing ---
t = (10, 20, 30, 40, 50)
print(f"Q1: t[2] = {t[2]}")
print(f"    t[-2] = {t[-2]}")
# Think: which position is index 2? Which is -2?

print()

# --- Q2: Length after concatenation ---
a = (1, 2, 3)
b = (4, 5)
c = a + b
print(f"Q2: len(a + b) = {len(c)}")
# Think: 3 + 2 = ?

print()

# --- Q3: Count and index ---
nums = (1, 3, 5, 3, 7, 3, 9)
print(f"Q3: nums.count(3) = {nums.count(3)}")
print(f"    nums.index(5)  = {nums.index(5)}")
# Think: how many 3s? What position is 5?

print()

# --- Q4: Slicing ---
letters = ('a', 'b', 'c', 'd', 'e', 'f')
print(f"Q4: letters[2:5]  = {letters[2:5]}")
print(f"    letters[::-1] = {letters[::-1]}")
# Think: which items are at index 2, 3, 4? What does ::-1 do?

print()

# --- Q5: Sum via tuple ---
scores = (85, 92, 78, 88, 95)
average = sum(scores) / len(scores)
print(f"Q5: average = {average:.1f}")
# Think: 85+92+78+88+95 = 438, divide by 5 = ?

print()

# --- Q6: Repetition ---
base = (0, 1)
repeated = base * 4
print(f"Q6: (0, 1) * 4 = {repeated}")
print(f"    len        = {len(repeated)}")
# Think: how many items total?

print()

# --- Q7: Unpacking maths ---
first, *middle, last = (10, 20, 30, 40, 50)
print(f"Q7: first = {first}")
print(f"    sum(middle) = {sum(middle)}")
print(f"    last  = {last}")
# Think: first=10, middle=[20,30,40], last=50 → sum of middle?

# Think:
# 1. In Q6, why is the length 8 and not 2?
# 2. In Q7, what type is `middle`? (Hint: it's not a tuple!)
