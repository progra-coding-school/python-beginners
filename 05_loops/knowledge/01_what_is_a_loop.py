# Program Code: LP-KN-01
# Title: What Is a Loop?
# Cognitive Skill: Knowledge
# Topic: Loops in Python

# WITHOUT a loop — you must repeat the same line manually
print("Good morning, Aarav!")
print("Good morning, Diya!")
print("Good morning, Karthik!")
print("Good morning, Riya!")
print("Good morning, Aman!")
# Imagine 30 students — you'd write 30 lines!

print()

# A LOOP repeats a block of code automatically.
# Python has two types of loops:

# --- for loop ---
# Use when you know HOW MANY times to repeat
students = ["Aarav", "Diya", "Karthik", "Riya", "Aman"]
for student in students:
    print("Good morning,", student + "!")

print()

# --- while loop ---
# Use when you repeat UNTIL a condition becomes False
count = 1
while count <= 5:
    print("Round", count, "- Keep going!")
    count += 1

print()

# --- Key vocabulary ---
# loop      → repeat a block of code
# iteration → one single run through the loop body
# for       → loop a fixed number of times
# while     → loop as long as a condition is True
# break     → exit the loop immediately
# continue  → skip this iteration, go to the next

# Think:
# 1. Name 3 real-life tasks that involve repetition (e.g., checking each student's name).
# 2. If you have 100 students, how many lines would you need WITHOUT a loop?
