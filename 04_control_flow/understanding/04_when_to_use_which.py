# Program Code: CF-UN-04
# Title: When to Use Which Loop
# Cognitive Skill: Understanding
# Topic: Control Flow in Python

# CHOOSING THE RIGHT TOOL:
# FOR loop   — when you know HOW MANY TIMES to repeat (or have a list)
# WHILE loop — when you repeat UNTIL something happens (unknown count)
# BREAK      — when you need to exit early based on a condition
# CONTINUE   — when you need to skip certain iterations but keep going

# USE FOR LOOP — fixed repetitions or iterating over items
print("--- For loop: present roll call ---")
students = ["Aarav", "Diya", "Priya", "Karthik", "Meera"]
for student in students:
    print("Present:", student)

# USE WHILE LOOP — repeat until condition changes
print("--- While loop: ask until correct ---")
password = "python123"
while True:
    attempt = input("Enter password: ")
    if attempt == password:
        print("Welcome!")
        break
    print("Wrong password. Try again.")

# USE BREAK — stop searching once found
print("--- Break: find first topper ---")
scores = [72, 58, 91, 83, 95, 66]
for score in scores:
    if score >= 90:
        print("First topper score found:", score)
        break

# USE CONTINUE — skip unwanted items
print("--- Continue: skip absent students ---")
attendance = {"Aarav": True, "Diya": False, "Priya": True, "Karthik": False}
for name, present in attendance.items():
    if not present:
        continue
    print(name, "is present.")

# Think:
# 1. You're reading books one by one until you find one about Python.
#    Which loop would you use?
# 2. You want to print all even numbers between 1 and 50. Use for + continue.
