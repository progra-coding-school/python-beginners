# Program Code: DT-HOT-02
# Title: Design a Data Form
# Cognitive Skill: Higher Order Thinking (Creating with types)
# Topic: Data Types in Python

# TASK: Design a "Student Registration Form" using the right data types for each field.

# YOUR CHALLENGE:
# For each field below, write the variable name and the correct type.
# Then write the code to collect and display it.

# Field list:
# 1. Student's full name → str
# 2. Roll number → int (or str if it has leading zeros — your choice!)
# 3. Age → int
# 4. GPA / CGPA → float
# 5. School name → str
# 6. Has paid fees → bool
# 7. Favourite subject → str

print("=== Student Registration Form ===\n")

full_name = input("Full name: ")
roll_number = int(input("Roll number: "))
age = int(input("Age: "))
gpa = float(input("GPA (e.g. 9.2): "))
school = input("School name: ")
fees_paid_str = input("Has paid fees? (yes/no): ")
fees_paid = fees_paid_str.lower() == "yes"
favourite_subject = input("Favourite subject: ")

print("\n--- Registration Summary ---")
print(f"Name: {full_name}")
print(f"Roll No: {roll_number}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"School: {school}")
print(f"Fees Paid: {fees_paid}")
print(f"Favourite Subject: {favourite_subject}")

# Think:
# 1. Why did we convert fees_paid_str to bool instead of keeping it as "yes"/"no"?
# 2. What if the roll number is "007"? Should you use int or str?
#    Try int("007") — what happens to the leading zero?
# 3. What other fields would you add? What types would they be?
