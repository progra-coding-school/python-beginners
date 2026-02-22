# Program Code: LP-KN-02
# Title: The for Loop
# Cognitive Skill: Knowledge
# Topic: Loops in Python

# A for loop repeats for each item in a sequence.

# --- Loop over a list ---
fruits = ["mango", "banana", "apple", "grapes"]
for fruit in fruits:
    print("Fruit:", fruit)

print()

# --- Loop over a string (each character) ---
name = "Aarav"
for letter in name:
    print(letter)

print()

# --- Loop with range() ---
# range(5) → gives 0, 1, 2, 3, 4
for i in range(5):
    print("Count:", i)

print()

# range(start, stop) → start included, stop excluded
for i in range(1, 6):
    print("Number:", i)    # 1 to 5

print()

# range(start, stop, step) → jump by step
for i in range(0, 11, 2):
    print("Even:", i)      # 0, 2, 4, 6, 8, 10

print()

# --- Loop with index using enumerate ---
subjects = ["Maths", "Science", "English"]
for index, subject in enumerate(subjects, 1):
    print(f"{index}. {subject}")

print()

# --- Real-life examples ---
marks = [85, 72, 90, 65, 88]
for mark in marks:
    if mark >= 80:
        print(f"{mark} → Distinction")
    else:
        print(f"{mark} → Pass")

# Think:
# 1. What does range(1, 10, 3) produce? Write it out before running.
# 2. How would you loop through the letters of your own name?
