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
    print(f"  --- {title} ---")

def field(label, value):
    print(f"  {label:<15}: {value}")

def separator():
    print("  " + "-" * (W - 2))

# --- Section 1: Personal Info ---
print("=" * W)
print(f"{'STUDENT REPORT':^{W}}")
print("=" * W)

section_header("Personal Information")
field("Name",   name)
field("Age",    f"{age} years old")
field("City",   city)
field("School", school)

# --- Section 2: Academic Marks ---
section_header("Academic Performance")
separator()
print(f"  {'Subject':<15}  {'Marks':>6}  {'Out of':>7}")
separator()
field("Maths",   f"{maths:>4} / 100")
field("Science", f"{science:>4} / 100")
field("English", f"{english:>4} / 100")
separator()
field("Total",   f"{total:>4} / 300")
field("Average", f"{average:.1f}")

# --- Section 3: Result ---
section_header("Result Summary")
field("Grade",  grade)
field("Result", result)

print()
print("=" * W)
print(f"{'Keep learning and keep growing!':^{W}}")
print("=" * W)

# Think:
# 1. Which group of information would you add a new section for?
# 2. How would you highlight the result row if the student FAILED?
