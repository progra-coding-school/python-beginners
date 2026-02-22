# Program Code: OUT-HOT-02
# Title: Design Your Output — Certificate Generator
# Cognitive Skill: Higher Order Thinking (Design from Scratch)
# Topic: Output in Python

# Design challenge: Build a certificate of achievement using only print().
# Make it look professional — borders, alignment, formatting.

print()

# --- Get details ---
name        = input("Recipient's name: ")
achievement = input("Achievement (e.g., 'completing Python Basics'): ")
school      = input("School/Organisation: ")
given_by    = input("Given by (teacher/principal name): ")

# --- Design the certificate ---
w = 50

def border():
    print("*" * w)

def double_border():
    print("#" * w)

def blank():
    print(f"*{' ' * (w-2)}*")

def centre(text):
    print(f"*{text:^{w-2}}*")

def left(text):
    print(f"*  {text:<{w-5}}*")

# --- Print the certificate ---
print()
double_border()
double_border()
blank()
centre("CERTIFICATE OF ACHIEVEMENT")
blank()
centre("Progra Kids Coding School")
blank()
border()
blank()
centre("This is to certify that")
blank()
centre(name.upper())
blank()
centre("has successfully achieved excellence in")
blank()
centre(achievement)
blank()
border()
blank()
left(f"Awarded by: {given_by}")
left(f"School    : {school}")
blank()
centre("Keep Learning. Keep Growing. Keep Coding!")
blank()
double_border()
double_border()
print()

# --- Bonus: ASCII art star ---
print("                  *")
print("                *   *")
print("              *       *")
print("                *   *")
print("                  *")
print()
print(f"{'Congratulations, ' + name + '!':^{w}}")

# Think:
# 1. How would you add the current date to the certificate?
# 2. Can you design a different border using different symbols?
