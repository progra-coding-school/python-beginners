# Program Code: FN-KN-01
# Title: What Is a Function?
# Cognitive Skill: Knowledge
# Topic: Functions in Python

# A function is a named block of code that does ONE specific job.
# You define it once and can use (call) it as many times as you need.

# --- Defining a function ---
# Use the 'def' keyword, followed by a name and ()
def greet():
    print("Hello! Welcome to Progra.")

# --- Calling a function ---
# Write the function name followed by ()
greet()
greet()
greet()
# The same code runs 3 times — but we wrote it only once!

print()

# --- Function with a name parameter ---
def greet_student(name):
    print("Hello,", name, "! Ready to code today?")

greet_student("Aarav")
greet_student("Diya")
greet_student("Riya")

print()

# --- Function that calculates and returns a result ---
def square(number):
    result = number * number
    return result

answer = square(5)
print("Square of 5:", answer)

answer = square(9)
print("Square of 9:", answer)

# --- Key vocabulary ---
# def       → keyword to define (create) a function
# greet     → function name (describes what it does)
# ()        → where parameters go (inputs)
# :         → marks the start of the function body
# indentation → the code INSIDE the function must be indented
# return    → sends a value back to whoever called the function
# call      → using the function by writing its name + ()

# Think:
# 1. What everyday "functions" do you perform? (e.g., make_tea, brush_teeth)
# 2. What is the difference between defining a function and calling a function?
