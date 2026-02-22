# Program Code: VAR-PS-03
# Title: Priya's School Report Card
# Cognitive Skill: Problem Solving (Plan First, Then Code)
# Topic: Variables in Python

# Plan your variables BEFORE coding:
# student_name, grade
# maths_mark, science_mark, english_mark, tamil_mark, social_mark
# total_marks, max_marks, percentage

student_name = input("Student name: ")
grade = input("Class/Grade: ")

print("Enter marks out of 100:")
maths_mark = int(input("Maths: "))
science_mark = int(input("Science: "))
english_mark = int(input("English: "))
tamil_mark = int(input("Tamil: "))
social_mark = int(input("Social: "))

total_marks = maths_mark + science_mark + english_mark + tamil_mark + social_mark
max_marks = 500
percentage = (total_marks / max_marks) * 100

print("Name:", student_name)
print("Class:", grade)
print("Maths:", maths_mark)
print("Science:", science_mark)
print("English:", english_mark)
print("Tamil:", tamil_mark)
print("Social:", social_mark)
print("Total:", total_marks, "/", max_marks)
print("Percentage:", percentage)

# Think:
# 1. Did planning the variables first make coding easier?
# 2. What new variables would you add for Computer Science and Art?
