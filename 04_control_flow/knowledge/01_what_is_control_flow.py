# Program Code: CF-KN-01
# Title: What Is Control Flow?
# Cognitive Skill: Knowledge
# Topic: Control Flow in Python

# WITHOUT control flow — code runs top to bottom, no decisions, no repetition
print("Good morning!")
print("Eat breakfast.")
print("Go to school.")

# CONTROL FLOW lets your program make DECISIONS and REPEAT actions.

# Decision — if statement
temperature = 38
if temperature > 37.5:
    print("You have a fever. Rest at home.")

# Decision with two paths — if-else
marks = 72
if marks >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")

# Decision with many paths — if-elif-else
score = 85
if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
else:
    print("Grade: C")

# Repetition — for loop
for i in range(3):
    print("Python is fun!")

# Repetition — while loop
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# Think:
# 1. Without control flow, how would you write a program that only greets you on Sundays?
# 2. Name 3 real decisions your phone makes every day (e.g. "if battery < 20% → show warning").
