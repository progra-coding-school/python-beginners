# Program Code: CF-HOT-03
# Title: Pattern Printer
# Cognitive Skill: Higher Order Thinking (Creative application of loops)
# Topic: Control Flow in Python

# Use nested loops to create visual star patterns.
print("=== Pattern Printer ===\n")

n = int(input("Enter size (e.g. 4): "))

# Pattern 1: Square of stars
print(f"\n--- {n}x{n} Square ---")
for row in range(n):
    for col in range(n):
        print("*", end=" ")
    print()

# Pattern 2: Right-angle triangle
print(f"\n--- Right Triangle (height {n}) ---")
for row in range(1, n + 1):
    for col in range(row):
        print("*", end=" ")
    print()

# Pattern 3: Number triangle
print(f"\n--- Number Triangle ---")
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

# Pattern 4: Inverted triangle
print(f"\n--- Inverted Triangle ---")
for row in range(n, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()

# Think:
# 1. Which loop is the outer loop and which is the inner?
# 2. What does 'end=" "' do in the print statement?
# 3. Can you make a hollow square (stars only on the border, spaces inside)?
