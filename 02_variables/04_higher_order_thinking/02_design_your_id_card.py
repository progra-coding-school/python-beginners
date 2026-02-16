# Program Code: CS-HO-02
# Title: Design Your Own Student ID Card
# Cognitive Skill: Higher Order Thinking (Creation - designing from scratch)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Your school wants every student to have an ID card.
# But YOU get to DESIGN what goes on it!
# What information should an ID card have?
# You decide, you create the variables, you design the card!
# This is YOUR creation!
# ============================================================

# ------------------------------------------------------------
# DESIGN THINKING:
# Before you code, think:
# - What does a good ID card need?
# - Name? Class? Roll number? Photo? (we'll skip photo!)
# - What about school name? House name? Blood group?
# - What about emergency contact?
# YOU choose what is important!
# ------------------------------------------------------------

print("=== Design Your Own Student ID Card ===")
print()
print("Let's create YOUR ID card!")
print("Answer the questions to fill in your card.")
print()

# Collect student information - the student CREATES their card
student_name = input("Your Name: ")
grade = input("Class/Grade: ")
section = input("Section (A/B/C): ")
roll_number = input("Roll Number: ")
school_name = input("School Name: ")
house_name = input("House Name (e.g., Blue House, Tiger House): ")
blood_group = input("Blood Group (e.g., O+, A+, B+): ")
parent_phone = input("Parent's Phone Number: ")

# Generate a student ID from the info
student_id = roll_number + grade + section

# Print the beautifully designed ID card
print()
print("Creating your ID card...")
print()
print("+" + "=" * 44 + "+")
print("|" + " " * 44 + "|")
print("|" + f"  {school_name}".ljust(44) + "|")
print("|" + "  STUDENT IDENTITY CARD".ljust(44) + "|")
print("|" + " " * 44 + "|")
print("+" + "-" * 44 + "+")
print("|" + " " * 44 + "|")
print("|" + f"  Name     : {student_name}".ljust(44) + "|")
print("|" + f"  Class    : {grade} - {section}".ljust(44) + "|")
print("|" + f"  Roll No  : {roll_number}".ljust(44) + "|")
print("|" + f"  House    : {house_name}".ljust(44) + "|")
print("|" + f"  Blood Grp: {blood_group}".ljust(44) + "|")
print("|" + " " * 44 + "|")
print("+" + "-" * 44 + "+")
print("|" + f"  Student ID: {student_id}".ljust(44) + "|")
print("|" + f"  Emergency : {parent_phone}".ljust(44) + "|")
print("|" + " " * 44 + "|")
print("+" + "=" * 44 + "+")

print()
print("Your ID card is ready!")

# ============================================================
# REFLECTION PROMPTS:
# 1. How many variables did YOU create for this ID card?
#    Count them! Each piece of information = one variable.
# 2. What ELSE would you add to the card if you could?
#    (Hint: Date of birth? Hobby? Favorite subject?)
#    What variable name would you use for it?
# 3. You DESIGNED this from scratch. How is designing
#    different from following instructions?
#    (Hint: You had to DECIDE what to include!)
# ============================================================
