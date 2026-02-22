# Program Code: LP-PS-01
# Title: Times Table Generator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Loops in Python

# Big question: How do we generate and display a full times table?
# Break it into steps — one loop decision at a time.

# Step 1: Get the number from the user
number = int(input("Enter a number to generate its times table: "))

# Step 2: Decide the range (1 to 12 for standard tables)
start = 1
end = 12

# Step 3: Loop and calculate each row
print(f"\n=== Times Table of {number} ===")
for i in range(start, end + 1):
    result = number * i
    print(f"  {number} × {i:2} = {result}")

print()

# Step 4: Extended — generate MULTIPLE tables
print("=== Mini Multiplication Table ===")
print("    ", end="")
for col in range(1, 6):
    print(f"{col:4}", end="")
print()
print("    " + "----" * 5)

for row in range(1, 6):
    print(f" {row:2} |", end="")
    for col in range(1, 6):
        print(f"{row * col:4}", end="")
    print()

print()

# Step 5: Find multiples within a range
print(f"Multiples of {number} up to 100:")
multiples = []
for i in range(1, 101):
    if i % number == 0:
        multiples.append(i)
print(multiples)

# Think:
# 1. How would you modify this to show the table from 1 to 20?
# 2. How would you make it show ONLY the odd-numbered rows (1×n, 3×n, 5×n...)?
