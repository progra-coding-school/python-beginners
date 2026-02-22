# Program Code: VAR-HOT-02
# Title: Design Your Own Student ID Card
# Cognitive Skill: Higher Order Thinking (Creation)
# Topic: Variables in Python

# You decide what goes on your ID card.
# Each piece of information = one variable.

student_name = input("Your Name: ")
grade = input("Class/Grade: ")
section = input("Section (A/B/C): ")
roll_number = input("Roll Number: ")
school_name = input("School Name: ")
house_name = input("House Name: ")
blood_group = input("Blood Group: ")
parent_phone = input("Parent's Phone Number: ")

student_id = roll_number + grade + section

print("School:", school_name)
print("Student ID Card")
print("Name:", student_name)
print("Class:", grade, "-", section)
print("Roll No:", roll_number)
print("House:", house_name)
print("Blood Group:", blood_group)
print("Student ID:", student_id)
print("Emergency:", parent_phone)

# Think:
# 1. How many variables did you create? Count them.
# 2. What else would you add? (date of birth, favourite subject?)
#    What variable name would you use?
# 3. How is designing your own program different from following instructions?
