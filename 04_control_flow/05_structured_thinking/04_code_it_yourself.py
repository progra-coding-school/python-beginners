# Program Code: CF-ST-04
# Title: Code It Yourself
# Cognitive Skill: Structured Thinking (Plan then implement)
# Topic: Control Flow in Python

# CHALLENGE: Read the problem, write your PLAN in comments first,
# then write the code below each plan.

# ══════════════════════════════════════════════════════════════════════════
# Exercise 1: Marks Checker (if statement)
# ══════════════════════════════════════════════════════════════════════════
# Problem: Ask the user for their marks. If marks > 40, print "Pass".

# YOUR PLAN (fill this in before coding):
# Step 1: _______________________________________________
# Step 2: _______________________________________________
# Step 3: _______________________________________________

# SOLUTION (write your code below):

marks = int(input("Enter your marks: "))
if marks > 40:
    print("Pass")

# ══════════════════════════════════════════════════════════════════════════
# Exercise 2: Weather Checker (if-else statement)
# ══════════════════════════════════════════════════════════════════════════
# Problem: Ask the user for the temperature.
# If temperature > 20, print "It's sunny." else print "It's cold."

# YOUR PLAN (fill this in before coding):
# Step 1: _______________________________________________
# Step 2: _______________________________________________
# Step 3: _______________________________________________

# SOLUTION (write your code below):

temperature = int(input("Enter the temperature: "))
if temperature > 20:
    print("It's sunny.")
else:
    print("It's cold.")

# ══════════════════════════════════════════════════════════════════════════
# Exercise 3: Day Activity Planner (if-elif-else)
# ══════════════════════════════════════════════════════════════════════════
# Problem: Ask the user to enter a day of the week.
# Saturday → "Coding class"
# Monday   → "Badminton class"
# Wednesday → "Guitar class"
# Any other day → "Free day — relax!"

# YOUR PLAN (fill this in before coding):
# Step 1: _______________________________________________
# Step 2: _______________________________________________
# Step 3: _______________________________________________

# SOLUTION (write your code below):

day = input("Enter the day: ").lower()
if day == "saturday":
    print("Coding class")
elif day == "monday":
    print("Badminton class")
elif day == "wednesday":
    print("Guitar class")
else:
    print("Free day — relax!")

# ══════════════════════════════════════════════════════════════════════════
# Exercise 4: Times Table Printer (for loop)
# ══════════════════════════════════════════════════════════════════════════
# Problem: Ask the user for a number. Print its multiplication table (1–10).

# YOUR PLAN (fill this in before coding):
# Step 1: _______________________________________________
# Step 2: _______________________________________________

# SOLUTION (write your code below):

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Think:
# 1. In Exercise 1, what would happen if marks == 40? How do you fix it?
# 2. In Exercise 3, what does .lower() do, and why is it needed?
# 3. Can you combine Exercises 1 and 2 into one program that asks for BOTH
#    marks AND temperature and gives a combined report?
