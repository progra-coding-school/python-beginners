# Program Code: 07-02
# Exercise: with-list.py

# ============================================================
# SAME PROBLEM — Now solved WITH a list!
#
# You are a class teacher. You have 5 students in your class.
# You need to:
#   1. Store all student names
#   2. Print all student names
#   3. Count how many students you have
#   4. Add a new student who joined today
#   5. Find if "Kabir" is in your class
#   6. Print names in alphabetical order
#
# Let's see how EASY it becomes with a list!
# ============================================================

# Task 1: Store 5 student names — just ONE variable!
students = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

# Task 2: Print all student names — just 2 lines, works for ANY number!
print("--- My Students ---")
for student in students:
    print(student)

# Task 3: Count how many students — one word: len()
print("\nTotal students:", len(students))

# Task 4: A new student "Priya" joins — just append!
students.append("Priya")
print("\n--- After new student joined ---")
for student in students:
    print(student)
print("Total students:", len(students))

# Task 5: Check if "Kabir" is in the class — just use 'in'!
if "Kabir" in students:
    print("\nKabir found!")
else:
    print("\nKabir not found!")

# Task 6: Print in alphabetical order — just sort()!
students.sort()
print("\n--- Sorted (A to Z) ---")
for student in students:
    print(student)

# ============================================================
# COMPARE:
#                    Without List     |    With List
# ---------------------------------------------------------
# Store 5 names      5 variables      |    1 variable
# Print all          5 print()        |    2 lines (loop)
# Count              count manually   |    len(students)
# Add a student      new variable     |    append()
# Search             5 if-elif        |    "in" keyword
# Sort               impossible!      |    sort()
# 50 students?       50 variables!    |    still 1 variable
# ============================================================
