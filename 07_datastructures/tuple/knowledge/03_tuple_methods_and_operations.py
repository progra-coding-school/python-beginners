# Program Code: TU-KN-03
# Title: Tuple Methods and Operations
# Cognitive Skill: Knowledge
# Topic: Tuples in Python

# Tuples are immutable, so they have only 2 built-in methods.
# But they support many useful operations!

nums = (4, 1, 7, 2, 4, 9, 4, 3)
print("Tuple:", nums)
print()

# --- .count(value) — how many times a value appears ---
print("=== .count() ===")
print("Count of 4 :", nums.count(4))    # 3
print("Count of 9 :", nums.count(9))    # 1
print("Count of 5 :", nums.count(5))    # 0 — not in tuple, no error

print()

# --- .index(value) — first position of a value ---
print("=== .index() ===")
print("Index of 7 :", nums.index(7))    # 2
print("Index of 4 :", nums.index(4))    # 1 — first occurrence
try:
    print(nums.index(99))               # ValueError — not found
except ValueError as e:
    print("ValueError:", e)

print()

# --- len(), min(), max(), sum() — built-in functions ---
print("=== Built-in functions ===")
print("len():", len(nums))
print("min():", min(nums))
print("max():", max(nums))
print("sum():", sum(nums))

print()

# --- Concatenation: + ---
print("=== Concatenation (+) ===")
a = (1, 2, 3)
b = (4, 5, 6)
print("a + b:", a + b)      # (1, 2, 3, 4, 5, 6)

print()

# --- Repetition: * ---
print("=== Repetition (*) ===")
echo = ("hi",) * 3
print("('hi',) * 3:", echo)     # ('hi', 'hi', 'hi')

print()

# --- Sorted (returns a list, not a tuple!) ---
print("=== sorted() ===")
words = ("banana", "apple", "mango", "grapes")
print("Original :", words)
print("Sorted   :", sorted(words))         # returns a list
print("Reversed :", sorted(words, reverse=True))

print()

# --- Looping ---
print("=== Looping ===")
for i, item in enumerate(words):
    print(f"  [{i}] {item}")

# Think:
# 1. Why does tuples only have 2 methods while lists have many more?
# 2. What does sorted() return — a list or a tuple? Does that surprise you?
