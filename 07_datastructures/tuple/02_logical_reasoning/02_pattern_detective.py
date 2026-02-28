# Program Code: TU-LR-02
# Title: Pattern Detective
# Cognitive Skill: Logical Reasoning
# Topic: Tuples in Python

# Spot the pattern in each code block.
# Name it, then complete the missing piece.

# --- Pattern 1: Multiple return values ---
print("=== Pattern 1: Function returning multiple values ===")

def circle_stats(radius):
    import math
    area        = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)  # returns a TUPLE

area, circ = circle_stats(7)
print(f"Radius 7 → Area: {area}, Circumference: {circ}")
# Pattern: functions return multiple values as tuples

print()

# --- Pattern 2: Zipping two lists into tuples ---
print("=== Pattern 2: Zipping ===")
names  = ["Aarav", "Diya", "Karthik"]
scores = [85, 92, 78]

pairs = list(zip(names, scores))     # [(name, score), ...]
print("Zipped:", pairs)

for name, score in pairs:            # unpack each tuple
    print(f"  {name}: {score}")
# Pattern: zip() creates tuples from parallel lists

print()

# --- Pattern 3: Sorting by tuple position ---
print("=== Pattern 3: Sorting records by a field ===")
students = [("Karthik", 78), ("Aarav", 85), ("Diya", 92)]

by_score = sorted(students, key=lambda s: s[1])     # sort by index 1 (score)
by_name  = sorted(students, key=lambda s: s[0])     # sort by index 0 (name)

print("By score:", by_score)
print("By name :", by_name)
# Pattern: lambda s: s[position] picks the sort key from a tuple

print()

# --- Pattern 4: Enumerate produces tuples ---
print("=== Pattern 4: enumerate() gives (index, value) tuples ===")
fruits = ("mango", "banana", "apple")

for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")
# Pattern: enumerate wraps each item in a (count, item) tuple

print()

# --- Pattern 5: Tuple as a composite dictionary key ---
print("=== Pattern 5: Tuple as a dict key ===")
# (row, col) → value — like a spreadsheet cell
grid = {
    (0, 0): "X",
    (0, 1): "O",
    (1, 0): "O",
    (1, 1): "X",
}
for (row, col), value in grid.items():
    print(f"  Row {row}, Col {col} → {value}")
# Pattern: tuple (row, col) used as a 2D grid key

# Think:
# 1. In Pattern 2, what happens if names and scores have different lengths?
# 2. In Pattern 5, how would you extend this to a 3D grid?
