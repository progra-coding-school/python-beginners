# Program Code: TU-FC-01
# Title: Spot the Difference
# Cognitive Skill: Focus and Concentration
# Topic: Tuples in Python

# Two versions of similar code are shown.
# Find every difference — some are bugs, some are style choices.

# ─── Pair 1 ─────────────────────────────────────────────────────
print("=== Pair 1 ===")

# Version A
t_a = (10, 20, 30)
print("A:", t_a[0], t_a[-1])   # 10, 30

# Version B
t_b = (10, 20, 30)
print("B:", t_b[0], t_b[2])    # 10, 30 — same result, different index
# Difference: A uses t_b[-1] (last item), B uses t_b[2] (explicit index).
# Both work here but -1 is more flexible when the tuple length changes.

print()

# ─── Pair 2 ─────────────────────────────────────────────────────
print("=== Pair 2 ===")

# Version A — creates a real tuple
single_a = (42,)
print("A type:", type(single_a))    # tuple

# Version B — creates an int, not a tuple!
single_b = (42)
print("B type:", type(single_b))    # int
# Difference: the comma makes A a tuple. B is just parentheses around an int.

print()

# ─── Pair 3 ─────────────────────────────────────────────────────
print("=== Pair 3 ===")

record  = ("Aarav", 13, "Chennai")

# Version A: index access
print("A name:", record[0])

# Version B: unpacking
name, age, city = record
print("B name:", name)
# Difference: A uses index, B unpacks. B is more readable when using multiple fields.

print()

# ─── Pair 4 ─────────────────────────────────────────────────────
print("=== Pair 4 ===")

# Version A — returns a tuple (two values)
def range_a(data):
    return min(data), max(data)

low, high = range_a([5, 1, 9, 3])
print("A: low =", low, "| high =", high)

# Version B — returns a list (two values)
def range_b(data):
    return [min(data), max(data)]

result = range_b([5, 1, 9, 3])
print("B: low =", result[0], "| high =", result[1])
# Difference: A returns a tuple (immutable, conventional for multi-return).
# B returns a list (caller could accidentally modify it).

print()

# ─── Pair 5 ─────────────────────────────────────────────────────
print("=== Pair 5 ===")

scores = (85, 90, 78, 92, 88)

# Version A: correct loop
total_a = 0
for s in scores:
    total_a += s
print("A total:", total_a)

# Version B: uses sum() — cleaner
total_b = sum(scores)
print("B total:", total_b)
# Difference: same result; B is more Pythonic and concise.

# Think:
# 1. In Pair 4, when is returning a list preferable to returning a tuple?
# 2. In Pair 1, which is more robust if the tuple grows from 3 items to 5: [0] or [-1]? Why?
