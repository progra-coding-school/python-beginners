# Program Code: CF-KN-03
# Title: For Loops
# Cognitive Skill: Knowledge
# Topic: Control Flow in Python

# FOR LOOP — repeat for each item in a sequence

# ── Loop using a list of numbers ───────────────────────────────────────────
for i in [1, 2, 3, 4, 5]:
    print("Hello World")

# ── Loop over a string (each character) ───────────────────────────────────
for i in "daniel":
    print("Hello World")   # runs once per letter — 6 times!

# Print each character in a name
name = "Python"
for char in name:
    print(char)

# Explanation:
# "Python" is stored as a sequence: ['P', 'y', 't', 'h', 'o', 'n']
# The loop picks one character at a time and runs the block for each.

# ── Loop over a list of items ──────────────────────────────────────────────
fruits = ["apple", "banana", "grapes", "mangoes"]
for fruit in fruits:
    print(fruit)

fruits2 = ["apple", "banana", "orange"]
for fruit in fruits2:
    print(f"I like {fruit}.")

# ── Loop with range() — generates a sequence of numbers ───────────────────
# range(stop)
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

# range(start, stop)
for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

# Parameters:
# start — where to begin (default 0)
# stop  — stop BEFORE this number (not inclusive)
# step  — gap between each number (default 1)

# ── Loop with enumerate (index + value) ───────────────────────────────────
students = ["Priya", "Diya", "Aarav"]
for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")

# ── Accumulate a sum in a loop ─────────────────────────────────────────────
total = 0
for num in [10, 20, 30, 40]:
    total = total + num
print("Total:", total)

# Think:
# 1. range(1, 10, 3) — write out every value it produces.
# 2. How would you print the 5-times table using a for loop?
# 3. Why does 'for i in "daniel"' run 6 times?
