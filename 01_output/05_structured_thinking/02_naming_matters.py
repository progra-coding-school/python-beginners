# Naming Matters — Clear Output Code
# Good variable names make output code self-explaining.
# Good output labels make the result easy to read.

# --- Example 1: Variable names in output ---

# BAD — meaningless names force you to read the whole program to understand it
a = "Aarav"
b = 13
c = 87

print(a, b, c)             # What does this show? No idea!

# GOOD — names describe exactly what they hold
student_name  = "Aarav"
student_age   = 13
student_marks = 87

print("Name: " + student_name + ", Age: " + str(student_age) + ", Marks: " + str(student_marks))

print()

# --- Example 2: Output labels ---

# BAD — output with no labels (what are these numbers?)
print(87, 72, 91)

# GOOD — labelled output tells the reader what they're seeing
maths_marks   = 87
science_marks = 72
english_marks = 91
print("Maths:", maths_marks, " Science:", science_marks, " English:", english_marks)

print()

# --- Example 3: Named constants for formatting ---

# BAD — magic numbers scattered in code; if you want to change width, you must find every 30
print("=" * 30)
print("Title".center(30))
print("=" * 30)

# GOOD — one named constant, change it once and everything updates
CARD_WIDTH = 40

print("=" * CARD_WIDTH)
print("Student Profile".center(CARD_WIDTH))
print("=" * CARD_WIDTH)

print()

# --- Example 4: Reusable print functions ---

# BAD — copy-pasting the same format everywhere (error-prone to maintain)
print("=" * 35)
print("Report Card".center(35))
print("=" * 35)
print("=" * 35)
print("Certificate".center(35))
print("=" * 35)

# GOOD — one helper function handles the pattern everywhere
def print_header(title, width=35):
    print("=" * width)
    print(title.center(width))
    print("=" * width)

print_header("Report Card")
print_header("Certificate")
print_header("Attendance Sheet", width=40)

print()

# --- Golden Rules ---
print("Output Naming Rules:")
print("1. Variable names describe WHAT the data represents")
print("   student_name, total_marks, is_passed")
print("2. Output labels tell the READER what they're seeing")
print("   print(\"Total:\", total)")
print("3. Use named constants for repeated values (width, symbol)")
print("   BORDER = '=' * 40")
print("4. Wrap repeated formats in a function")
print("   def print_header(title): ...")

# Think:
# 1. Rename: x = 150, y = 3, print(x * y) — what should x, y, and the output label be?
# 2. What would you name a function that prints a dashed separator line?
