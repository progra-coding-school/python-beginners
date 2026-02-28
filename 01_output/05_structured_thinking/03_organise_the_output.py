# Program Code: OUT-ST-03
# Title: Organise the Output
# Cognitive Skill: Structured Thinking (Data Organisation)
# Topic: Output in Python

# Complex output must be ORGANISED into sections.
# Use headers, dividers, blank lines, and alignment to group related info.

# --- BAD: Dumping everything without structure ---
print("BAD output — unorganised dump:")
print("Aarav 13 Chennai Progra School 85 72 90 PASS A")
print()

# --- GOOD: Organised into clear sections ---
print("GOOD output — structured and readable:")
print()

# Data
name    = "Aarav"
age     = 13
city    = "Chennai"
school  = "Progra Kids Coding School"
maths   = 85
science = 72
english = 90
total   = maths + science + english
average = total / 3
grade   = "A" if average >= 80 else "B"
result  = "PASS" if all(m >= 35 for m in [maths, science, english]) else "FAIL"

# Helper functions for consistent formatting
W = 40
def section_header(title):
    print()
    print("  --- " + title + " ---")

def field(label, value):
    print("  " + label.ljust(15) + ": " + str(value))

def separator():
    print("  " + "-" * (W - 2))

# --- Section 1: Personal Info ---
print("=" * W)
print("STUDENT REPORT".center(W))
print("=" * W)

section_header("Personal Information")
field("Name",   name)
field("Age",    str(age) + " years old")
field("City",   city)
field("School", school)

# --- Section 2: Academic Marks ---
section_header("Academic Performance")
separator()
print("  " + "Subject".ljust(15) + "Marks".rjust(7) + "Out of".rjust(8))
separator()
field("Maths",   str(maths).rjust(4)   + " / 100")
field("Science", str(science).rjust(4) + " / 100")
field("English", str(english).rjust(4) + " / 100")
separator()
field("Total",   str(total).rjust(4)           + " / 300")
field("Average", str(round(average, 1)))

# --- Section 3: Result ---
section_header("Result Summary")
field("Grade",  grade)
field("Result", result)

print()
print("=" * W)
print("Keep learning and keep growing!".center(W))
print("=" * W)

# Think:
# 1. Which group of information would you add a new section for?
# 2. How would you highlight the result row if the student FAILED?
