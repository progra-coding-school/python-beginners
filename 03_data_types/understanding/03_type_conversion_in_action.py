# Program Code: DT-UN-03
# Title: Type Conversion in Action
# Cognitive Skill: Understanding
# Topic: Data Types in Python

# WHY we need to convert types — real examples

# Example 1: User enters marks as text, we need to calculate average
tamil_str = "88"
maths_str = "92"
science_str = "79"

# Wrong way — adding strings!
# total = tamil_str + maths_str + science_str  → "887992" (not 259!)

# Right way — convert first
tamil = int(tamil_str)
maths = int(maths_str)
science = int(science_str)
total = tamil + maths + science
average = total / 3
print("Total:", total)
print("Average:", round(average, 2))

# Example 2: Building a message from numbers
student_name = "Diya"
marks = 94
subject = "Science"

# Wrong way
# message = "Hi " + student_name + " your " + subject + " mark is " + marks
# ↑ ERROR: cannot join str and int

# Right way — convert int to str
message = "Hi " + student_name + " your " + subject + " mark is " + str(marks)
print(message)

# OR use f-strings (automatic conversion)
message2 = f"Hi {student_name} your {subject} mark is {marks}"
print(message2)

# Example 3: Price with rupee symbol
price = 149.99
print("Price: Rs." + str(round(price, 2)))

# Think:
# 1. Why does "88" + "92" give "8892" and not 180?
# 2. When would you use str(marks) vs f"{marks}" to insert a number into text?
