# Program Code: 07-01
# Exercise: with-out-list.py

# ============================================================
# PROBLEM:
# You are a class teacher. You have 5 students in your class.
# You need to:
#   1. Store all student names
#   2. Print all student names
#   3. Count how many students you have
#   4. Add a new student who joined today
#   5. Find if "Kabir" is in your class
#   6. Print names in alphabetical order
#
# Let's try doing this WITHOUT a list...
# ============================================================

# Task 1: Store 5 student names
student1 = "Aarav"
student2 = "Diya"
student3 = "Kabir"
student4 = "Meera"
student5 = "Rohan"

# Task 2: Print all student names
# We have to write print() FIVE times!
print("--- My Students ---")
print(student1)
print(student2)
print(student3)
print(student4)
print(student5)

# Task 3: Count how many students
# There is no easy way! We have to count manually.
count = 5
print("\nTotal students:", count)

# Task 4: A new student "Priya" joins the class
# We need to create ANOTHER variable!
student6 = "Priya"
# And now we must update the count manually
count = 6
# And add ANOTHER print statement
print("\n--- After new student joined ---")
print(student1)
print(student2)
print(student3)
print(student4)
print(student5)
print(student6)
print("Total students:", count)

# Task 5: Check if "Kabir" is in the class
# We have to check EVERY variable one by one!
if student1 == "Kabir":
    print("\nKabir found!")
elif student2 == "Kabir":
    print("\nKabir found!")
elif student3 == "Kabir":
    print("\nKabir found!")
elif student4 == "Kabir":
    print("\nKabir found!")
elif student5 == "Kabir":
    print("\nKabir found!")
elif student6 == "Kabir":
    print("\nKabir found!")
else:
    print("\nKabir not found!")

# Task 6: Print in alphabetical order
# IMPOSSIBLE without writing complex code!
# We can't sort individual variables easily.
print("\nSorting? We can't sort separate variables easily!")

# ============================================================
# THINK ABOUT THIS:
# What if you had 50 students? 100 students?
# - 100 variables? (student1, student2, ... student100)
# - 100 print statements?
# - 100 if-elif checks to search?
#
# This is PAINFUL! There must be a better way...
# YES! That's why we need a LIST!
# ============================================================
