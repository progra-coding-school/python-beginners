# Program Code: STR-HOT-02
# Title: Design Your ID Card — Create a Text ID Using Strings!
# Cognitive Skill: Higher Order Thinking (Design from scratch)
# Topic: Strings in Python

# PROBLEM STATEMENT:
# Progra Kids Coding School needs digital ID cards for all students.
# YOU are the designer!
# Using only strings and print statements, design a beautiful
# text-based ID card that displays student information.

# THINK BEFORE YOU CODE:
# → What information goes on an ID card?
# → How will you format names and codes?
# → How will you create borders and alignment?

# STEP 1: Collect student information
print("Enter your details to generate your ID card:")
print()

raw_name = input("Full Name   : ")
grade    = input("Grade/Class : ")
batch    = input("Batch (Morning/Evening) : ")
city     = input("City        : ")

# STEP 2: Format the data using string methods
name  = raw_name.strip().title()
grade = grade.strip().upper()
batch = batch.strip().title()
city  = city.strip().title()

# Generate a student code: first 3 letters of name + year
name_code  = name.replace(" ", "")[:3].upper()
student_id = "STU-" + name_code + "-2026"

# Extract initials
parts = name.split()
if len(parts) >= 2:
    initials = parts[0][0] + "." + parts[1][0] + "."
else:
    initials = parts[0][0] + "."

# STEP 3: Print the ID card
print()
print("+" + "=" * 43 + "+")
print("|" + " " * 43 + "|")
print("|" + "   PROGRA KIDS CODING SCHOOL".center(43) + "|")
print("|" + "   Train the Brain. Build the Future.".center(43) + "|")
print("|" + " " * 43 + "|")
print("|" + "-" * 43 + "|")
print("|" + " " * 43 + "|")
print("|" + ("   Name     :  " + name).ljust(43) + "|")
print("|" + ("   Initials :  " + initials).ljust(43) + "|")
print("|" + ("   ID       :  " + student_id).ljust(43) + "|")
print("|" + ("   Grade    :  " + grade).ljust(43) + "|")
print("|" + ("   Batch    :  " + batch).ljust(43) + "|")
print("|" + ("   City     :  " + city).ljust(43) + "|")
print("|" + " " * 43 + "|")
print("|" + "-" * 43 + "|")
print("|" + "   Valid: 2026 — 2027".ljust(43) + "|")
print("|" + " " * 43 + "|")
print("+" + "=" * 43 + "+")

print()
print("ID Card for " + name + " generated successfully!")

# String Operations Used
print()
print("--- String Operations Used ---")
print("  .strip()        → Removed extra spaces")
print("  .title()        → '" + raw_name.strip() + "' → '" + name + "'")
print("  .upper()        → '" + grade + "'")
print("  .replace()      → Removed spaces from name for ID")
print("  [:3].upper()    → First 3 letters: '" + name_code + "'")
print("  .split()        → Split name into parts for initials")

# REFLECTION:
# 1. How did you generate the student ID? Can you improve it?
# 2. What other information would a real school ID have?
# 3. How would you add a QR code pattern using string repetition?
