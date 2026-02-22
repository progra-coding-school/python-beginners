# Program Code: VAR-UN-04
# Title: Input — Variables the User Fills
# Cognitive Skill: Understanding
# Topic: Variables in Python

# input() asks the user to type something and stores it
name = input("What is your name? ")
city = input("Which city are you from? ")

print("Hello,", name, "from", city)

# IMPORTANT: input() always gives a STRING
age = input("How old are you? ")
print(type(age))      # <class 'str'> — it's text, not a number!

# To do maths, convert to int first
age = int(age)
print(type(age))      # <class 'int'> — now it's a number

birth_year = 2025 - age
print("You were born around", birth_year)

# Print multiple variables with commas
student_name = "Meera"
marks = 88
total = 100

print(student_name, "scored", marks, "out of", total)
print("Percentage:", marks / total * 100)

# Calculations in print
length = 12
breadth = 5
print("Area:", length * breadth, "sq cm")

# Think:
# 1. What happens if you type your name when asked for age and do int(age)?
# 2. Ask for 2 numbers from the user and print their sum.
