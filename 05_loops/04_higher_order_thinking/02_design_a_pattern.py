# Program Code: LP-HOT-02
# Title: Design a Pattern — Nested Loops
# Cognitive Skill: Higher Order Thinking (Design from Scratch)
# Topic: Loops in Python

# Nested loops are perfect for printing 2D patterns.
# Outer loop = rows, Inner loop = columns.

print("=== Pattern 1: Right Triangle of Stars ===")
rows = int(input("How many rows? "))
for i in range(1, rows + 1):
    print("*" * i)

print()

print("=== Pattern 2: Number Triangle ===")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

print("=== Pattern 3: Inverted Triangle ===")
for i in range(rows, 0, -1):
    print("* " * i)

print()

print("=== Pattern 4: Square of Stars ===")
for i in range(rows):
    print("* " * rows)

print()

print("=== Pattern 5: Hollow Square ===")
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("* " * rows)
    else:
        print("* " + "  " * (rows - 2) + "*")

print()

print("=== Pattern 6: Pyramid ===")
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars  = "* " * i
    print(spaces + stars)

print()

print("=== Pattern 7: Multiplication Table Grid ===")
size = min(rows, 10)
print("   ", end="")
for col in range(1, size + 1):
    print(f"{col:4}", end="")
print()
print("   " + "----" * size)

for row in range(1, size + 1):
    print(f"{row:3}|", end="")
    for col in range(1, size + 1):
        print(f"{row * col:4}", end="")
    print()

# Think:
# 1. How would you make the pyramid print upside-down?
# 2. Can you create a diamond shape using two triangles — one normal, one inverted?
