# My Identity Card
# Problem: design and display a personal ID card using only print() and string formatting.
# Break it into smaller output decisions — one field at a time.

# Step 1: Gather the information
name      = input("Your full name: ")
age       = input("Your age: ")
grade     = input("Your grade/class: ")
school    = input("Your school name: ")
city      = input("Your city: ")
hobby     = input("Your favourite hobby: ")
fav_sport = input("Your favourite sport: ")

# Step 2: Decide card width — all rows must fit inside this
card_width = 38

# Step 3: Build the border strings once and reuse them
border     = "+" + "=" * (card_width - 2) + "+"
thin_line  = "+" + "-" * (card_width - 2) + "+"

# Step 4: Helper functions — each handles one output pattern
# title_line centres text between + markers
def title_line(text):
    print("+" + text.center(card_width - 2) + "+")

# field_line left-aligns a labelled value inside | markers
def field_line(label, value):
    content = "  " + label + ": " + str(value)
    print("|" + content.ljust(card_width - 2) + "|")

# blank_line prints an empty row inside the card border
def blank_line():
    print("|" + " " * (card_width - 2) + "|")

# Step 5: Print the ID card — structure follows the plan above
print()
print(border)
title_line("PROGRA KIDS CODING SCHOOL")
title_line("STUDENT IDENTITY CARD")
print(thin_line)
blank_line()
field_line("Name      ", name)
field_line("Age       ", age)
field_line("Grade     ", grade)
field_line("School    ", school)
field_line("City      ", city)
blank_line()
print(thin_line)
field_line("Hobby     ", hobby)
field_line("Fav Sport ", fav_sport)
blank_line()
print(border)
print("+" + "Progra - Think. Code. Lead.".center(card_width - 2) + "+")
print(border)

# Think:
# 1. What extra field would make this ID card more useful?
# 2. How would you change the card width to make it bigger or smaller?
