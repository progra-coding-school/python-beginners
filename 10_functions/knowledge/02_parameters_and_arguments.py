# Program Code: FN-KN-02
# Title: Parameters and Arguments
# Cognitive Skill: Knowledge
# Topic: Functions in Python

# Parameter = the variable name inside the function definition (a placeholder)
# Argument  = the actual value you pass when calling the function

# --- No parameters ---
def show_school():
    print("School: Progra Kids Coding School")

show_school()    # No argument needed

print()

# --- One parameter ---
def show_name(name):        # 'name' is the PARAMETER
    print("Student:", name)

show_name("Aarav")          # "Aarav" is the ARGUMENT
show_name("Diya")
show_name("Karthik")

print()

# --- Two parameters ---
def show_student(name, grade):
    print(f"Name: {name}, Grade: {grade}")

show_student("Aarav", 7)
show_student("Diya", 6)

print()

# --- Three parameters ---
def introduce(name, age, city):
    print(f"Hi! I am {name}, {age} years old, from {city}.")

introduce("Riya", 12, "Chennai")
introduce("Aman", 13, "Mumbai")

print()

# --- Default parameter (optional argument) ---
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Aarav")              # Uses default greeting
greet("Diya", "Namaste")    # Overrides default

print()

# --- Key rule ---
# The number of arguments in the CALL must match the parameters in the DEFINITION
# show_name("Aarav", "Diya")  ← ERROR: too many arguments
# show_student("Aarav")       ← ERROR: missing one argument

# Think:
# 1. What is the difference between a parameter and an argument?
# 2. Design a function calculate_area(length, width) — what are the parameters?
