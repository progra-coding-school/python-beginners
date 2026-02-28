# Program Code: TU-HOT-01
# Title: Reverse Engineer the Tuple
# Cognitive Skill: Higher Order Thinking
# Topic: Tuples in Python

# Study the OUTPUT. Write the code that produced it.
# Then compare with the reference.

# --- Challenge 1 ---
# Output: (1, 4, 9, 16, 25)
# Clue: squares of 1 through 5

print("=== Challenge 1 ===")
print("Target: (1, 4, 9, 16, 25)")
result = tuple(n**2 for n in range(1, 6))
print("Result:", result)

print()

# --- Challenge 2 ---
# Output:
#   Aarav   → 85
#   Diya    → 92
#   Karthik → 78
# Clue: zipped from two lists

print("=== Challenge 2 ===")
print("Target: zipped output")
names  = ["Aarav", "Diya", "Karthik"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"  {name:<10} → {score}")

print()

# --- Challenge 3 ---
# Output: 5 15
# Clue: min and max returned from one function call

print("=== Challenge 3 ===")
print("Target: 5 15")
def bounds(data):
    return min(data), max(data)
low, high = bounds([10, 5, 15, 8, 12])
print(low, high)

print()

# --- Challenge 4 ---
# Output: {'(0, 0)': 'A', '(0, 1)': 'B', '(1, 0)': 'C', '(1, 1)': 'D'}
# Clue: grid positions as tuple keys

print("=== Challenge 4 ===")
print("Target: grid dict with tuple keys")
letters = ['A', 'B', 'C', 'D']
grid    = {}
i = 0
for row in range(2):
    for col in range(2):
        grid[(row, col)] = letters[i]
        i += 1
print({str(k): v for k, v in grid.items()})

print()

# --- Challenge 5 (design challenge) ---
# Output: sorted by score descending
#   1. Priya   95
#   2. Diya    92
#   3. Ananya  88

print("=== Challenge 5 ===")
print("Target: top 3 sorted by score")
data = [("Aarav", 85), ("Diya", 92), ("Karthik", 78),
        ("Priya", 95), ("Ananya", 88)]
top3 = sorted(data, key=lambda t: -t[1])[:3]
for i, (name, score) in enumerate(top3, 1):
    print(f"  {i}. {name:<10} {score}")

# Think:
# 1. In Challenge 1, what is the construct tuple(n**2 for n in ...) called?
# 2. In Challenge 5, explain what lambda t: -t[1] does step by step.
