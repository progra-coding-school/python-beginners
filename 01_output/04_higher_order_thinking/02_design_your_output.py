# Design Your Output — Certificate Generator
# Design challenge: build a certificate of achievement using only print().
# Make it look professional — borders, alignment, formatting.

print()

# --- Get details ---
name        = input("Recipient's name: ")
achievement = input("Achievement (e.g., 'completing Python Basics'): ")
school      = input("School/Organisation: ")
given_by    = input("Given by (teacher/principal name): ")

# --- Design the certificate ---
# All helper functions share the same width — consistent margins and borders
w = 50

def border():
    print("*" * w)

def double_border():
    print("#" * w)

def blank():
    print("*" + " " * (w-2) + "*")

# centre() pads the text to fill the inner width exactly
def centre(text):
    print("*" + text.center(w-2) + "*")

# left() left-aligns text with a small margin
def left(text):
    print("*  " + text.ljust(w-5) + "*")

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
centre(name.upper())    # recipient's name in capitals — most prominent element
blank()
centre("has successfully achieved excellence in")
blank()
centre(achievement)
blank()
border()
blank()
left("Awarded by: " + given_by)
left("School    : " + school)
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
print(("Congratulations, " + name + "!").center(w))

# Think:
# 1. How would you add the current date to the certificate?
# 2. Can you design a different border using different symbols?
