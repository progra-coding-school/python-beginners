# Program Code: OUT-PS-01
# Title: My Identity Card
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Output in Python

# Big question: How do we design and display a personal ID card?
# Break it into smaller output decisions — one field at a time.

# Step 1: Gather the information
name      = input("Your full name: ")
age       = input("Your age: ")
grade     = input("Your grade/class: ")
school    = input("Your school name: ")
city      = input("Your city: ")
hobby     = input("Your favourite hobby: ")
fav_sport = input("Your favourite sport: ")

# Step 2: Decide card width
card_width = 38

# Step 3: Build the border
border     = "+" + "=" * (card_width - 2) + "+"
thin_line  = "+" + "-" * (card_width - 2) + "+"

# Step 4: Helper to print a centred title line
def title_line(text):
    print(f"+{text:^{card_width - 2}}+")

# Helper to print a labelled field
def field_line(label, value):
    content = f"  {label}: {value}"
    print(f"|{content:<{card_width - 2}}|")

def blank_line():
    print(f"|{' ' * (card_width - 2)}|")

# Step 5: Print the ID card
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
print(f"+{'Progra - Think. Code. Lead.':^{card_width - 2}}+")
print(border)

# Think:
# 1. What extra field would make this ID card more useful?
# 2. How would you change the card width to make it bigger or smaller?
