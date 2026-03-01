# Formatting Output — Making It Readable
# Good output isn't just correct — it's READABLE and PRESENTABLE.
# Use alignment, rounding, borders, and spacing to make data easy to scan.

# --- 1. Alignment with string methods ---
# .ljust(n) → left-align in a field of n characters (pad with spaces on the right)
# .rjust(n) → right-align in a field of n characters (pad with spaces on the left)
# .center(n) → centre-align in a field of n characters
print("Alignment with string methods:")
print("Name".ljust(12)    + "Marks".rjust(6) + "Grade".center(8))
print("-" * 28)
print("Aarav".ljust(12)   + str(85).rjust(6) + "A".center(8))
print("Diya".ljust(12)    + str(72).rjust(6) + "B".center(8))
print("Karthik".ljust(12) + str(91).rjust(6) + "A+".center(8))

print()

# --- 2. Decimal precision with round() ---
# round(number, decimal_places) limits the number of digits shown after the dot
print("Decimal precision with round():")
pi = 3.14159265
print("Pi (full):     ", pi)
print("Pi (2 decimal):", round(pi, 2))
print("Pi (4 decimal):", round(pi, 4))

average = 253 / 3
print("Average (raw): ", average)
print("Average (1dp): ", round(average, 1))

print()

# --- 3. Separators and borders using helper functions ---
# Define helper functions to keep formatting DRY (Don't Repeat Yourself)
print("Separators and borders:")
def print_header(title):
    width = 35
    print("=" * width)
    print(title.center(width))
    print("=" * width)

def print_row(label, value):
    print("  " + label.ljust(15) + " : " + str(value))

print_header("Progra School Report")
print_row("Student",     "Aarav")
print_row("Class",       "Grade 7")
print_row("Total Marks", "253 / 300")
print_row("Average",     "84.3")
print_row("Grade",       "A")
print("=" * 35)

print()

# --- 4. Multiline output for readability ---
# One long line is hard to scan; multiple labelled lines are easy to read
print("Multiline output for readability:")
# Bad — all on one line
print("Name: Aarav Age: 13 School: Progra Marks: 85 90 78")

# Good — structured with consistent labels and spacing
print()
print("Name   : Aarav")
print("Age    : 13")
print("School : Progra Kids Coding School")
print("Marks  : Maths=85, Science=90, English=78")

print()

# --- 5. Using blank lines to group output ---
# print() with no arguments outputs a blank line — use it to separate sections
print("Using blank lines to group output:")
print("Section 1: Personal Info")
print("  Name: Aarav")
print("  Age: 13")
print()    # blank line separates sections visually
print("Section 2: Academic Info")
print("  Total: 253")
print("  Grade: A")

# Think:
# 1. How would you right-align a number in a field of 8 characters?
#    Try: print(str(42).rjust(8))
# 2. What does .center(20) do? Try it: print("Aarav".center(20))
