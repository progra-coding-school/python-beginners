# Program Code: LIST-UN-01
# Title: Why Lists Exist — The Pain Before the Solution!
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Kabir is the class teacher at Progra Kids School.
# He has 5 students: Aarav, Diya, Kabir, Meera, Rohan.
# He needs to:
#   1. Store all student names
#   2. Print all names
#   3. Count how many students
#   4. Add a new student who joined today
#   5. Check if "Meera" is in his class
#   6. Sort names alphabetically
#
# First he tries WITHOUT a list. Then WITH a list.
# Let's see which way is smarter!
# ============================================================

print("=" * 55)
print("   WHY LISTS EXIST — THE PAIN BEFORE THE SOLUTION!")
print("=" * 55)

# ============================================================
# PART 1: WITHOUT A LIST — The Hard, Painful Way
# ============================================================

print("\n" + "=" * 55)
print("   PART 1: WITHOUT A LIST (The Painful Way)")
print("=" * 55)

# -----------------------------------------------------------
# Task 1: Store 5 student names
# We need 5 separate variables — one for EACH student!
# -----------------------------------------------------------
print("\n--- Task 1: Storing 5 Student Names ---")
print("(We need 5 separate variables!)")

student_1 = "Aarav"
student_2 = "Diya"
student_3 = "Kabir"
student_4 = "Meera"
student_5 = "Rohan"

print(f"  student_1 = '{student_1}'")
print(f"  student_2 = '{student_2}'")
print(f"  student_3 = '{student_3}'")
print(f"  student_4 = '{student_4}'")
print(f"  student_5 = '{student_5}'")
print("  --> 5 students = 5 variables. What about 50 students?!")

# -----------------------------------------------------------
# Task 2: Print all student names
# We have to write print() FIVE separate times!
# -----------------------------------------------------------
print("\n--- Task 2: Printing All Names ---")
print("(We need 5 separate print() calls!)")

print(f"  {student_1}")
print(f"  {student_2}")
print(f"  {student_3}")
print(f"  {student_4}")
print(f"  {student_5}")
print("  --> 5 students = 5 print() lines. Imagine 100 students!")

# -----------------------------------------------------------
# Task 3: Count how many students
# No automatic way — we must track the count ourselves.
# -----------------------------------------------------------
print("\n--- Task 3: Counting Students ---")
print("(No shortcut! We count manually and remember the number.)")

student_count_without_list = 5     # We just KNOW it's 5 and hardcode it
print(f"  Total students: {student_count_without_list}")
print("  --> If we add or remove a student, we must update this by hand!")

# -----------------------------------------------------------
# Task 4: Add a new student "Priya" who joined today
# We need a brand-new variable AND manually update the count.
# -----------------------------------------------------------
print("\n--- Task 4: Adding a New Student (Priya joined today!) ---")
print("(We need a new variable + update the count manually!)")

student_6 = "Priya"
student_count_without_list = 6     # Must update manually — easy to forget!

print(f"  student_6 = '{student_6}'")
print(f"  Total students (updated manually): {student_count_without_list}")
print("  --> Easy to forget to update the count. Bugs waiting to happen!")

# -----------------------------------------------------------
# Task 5: Search — Is "Meera" in the class?
# We must check EVERY variable one by one with if-elif.
# -----------------------------------------------------------
print("\n--- Task 5: Searching for 'Meera' ---")
print("(We must check all 6 variables one by one!)")

name_to_find = "Meera"

if student_1 == name_to_find:
    print(f"  Found '{name_to_find}'!")
elif student_2 == name_to_find:
    print(f"  Found '{name_to_find}'!")
elif student_3 == name_to_find:
    print(f"  Found '{name_to_find}'!")
elif student_4 == name_to_find:
    print(f"  Found '{name_to_find}'!")
elif student_5 == name_to_find:
    print(f"  Found '{name_to_find}'!")
elif student_6 == name_to_find:
    print(f"  Found '{name_to_find}'!")
else:
    print(f"  '{name_to_find}' not found!")

print("  --> 6 students = 6 elif checks. 50 students = 50 elif checks!")

# -----------------------------------------------------------
# Task 6: Sort names alphabetically
# Nearly IMPOSSIBLE with separate variables!
# -----------------------------------------------------------
print("\n--- Task 6: Sorting Names Alphabetically ---")
print("  We CANNOT sort separate variables easily.")
print("  There is no sort() for individual variables!")
print("  You would have to compare them manually — very complex code.")
print("  --> This is practically impossible without a list!")

# ============================================================
# PART 2: WITH A LIST — The Smart, Elegant Way
# ============================================================

print("\n" + "=" * 55)
print("   PART 2: WITH A LIST (The Smart Way)")
print("=" * 55)

# -----------------------------------------------------------
# Task 1: Store 5 student names
# ONE variable holds ALL names!
# -----------------------------------------------------------
print("\n--- Task 1: Storing 5 Student Names ---")
print("(Just 1 variable — the list holds everything!)")

student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

print(f"  student_names = {student_names}")
print("  --> 1 variable for any number of students!")

# -----------------------------------------------------------
# Task 2: Print all student names
# A simple loop handles it in 2 lines, for ANY number of names.
# -----------------------------------------------------------
print("\n--- Task 2: Printing All Names ---")
print("(A loop handles it — works for 5 or 500 students!)")

for student_name in student_names:
    print(f"  {student_name}")

print("  --> Works for any number of students with the same 2 lines!")

# -----------------------------------------------------------
# Task 3: Count students
# len() gives the count instantly and always stays accurate.
# -----------------------------------------------------------
print("\n--- Task 3: Counting Students ---")

total_students = len(student_names)
print(f"  Total students: {total_students}  (using len())")
print("  --> Always accurate — updates automatically when list changes!")

# -----------------------------------------------------------
# Task 4: Add new student "Priya"
# append() adds to the list. len() updates itself automatically.
# -----------------------------------------------------------
print("\n--- Task 4: Adding a New Student (Priya joined today!) ---")

student_names.append("Priya")
print(f"  After append: {student_names}")
print(f"  New total (automatic): {len(student_names)}")
print("  --> One line to add. Count is always correct automatically!")

# -----------------------------------------------------------
# Task 5: Search — Is "Meera" in the class?
# The 'in' keyword checks the entire list in one clean line.
# -----------------------------------------------------------
print("\n--- Task 5: Searching for 'Meera' ---")

search_name = "Meera"

if search_name in student_names:
    print(f"  '{search_name}' is in the class!")
else:
    print(f"  '{search_name}' is NOT in the class!")

print("  --> One line. Works whether there are 5 or 500 students!")

# -----------------------------------------------------------
# Task 6: Sort names alphabetically
# sort() does it instantly!
# -----------------------------------------------------------
print("\n--- Task 6: Sorting Names Alphabetically ---")

print(f"  Before sort: {student_names}")
student_names.sort()
print(f"  After sort : {student_names}")
print("  --> One method call. Done!")

# ============================================================
# COMPARISON TABLE
# ============================================================
#
#  Task                | Without List           | With List
#  --------------------|------------------------|------------------------
#  Store 5 names       | 5 separate variables   | 1 variable (the list)
#  Print all           | 5 print() statements   | 2 lines (for loop)
#  Count students      | hardcoded number       | len()  — always right
#  Add a student       | new variable + update  | append() — 1 line
#  Search for name     | 5-6 if-elif checks     | 'in' keyword — 1 line
#  Sort names          | practically impossible | sort()  — 1 line
#  Scale to 50 students| 50 variables!          | still 1 variable!
#
# ============================================================

print("\n" + "=" * 55)
print("   COMPARISON: WITHOUT LIST vs WITH LIST")
print("=" * 55)
print(f"  {'Task':<22} {'Without List':<22} {'With List'}")
print("-" * 70)
print(f"  {'Store 5 names':<22} {'5 variables':<22} {'1 variable'}")
print(f"  {'Print all':<22} {'5 print() calls':<22} {'2 lines (loop)'}")
print(f"  {'Count':<22} {'hardcoded number':<22} {'len()'}")
print(f"  {'Add a student':<22} {'new variable + update':<22} {'append()'}")
in_keyword_label = "'in' keyword"
print(f"  {'Search':<22} {'5 if-elif checks':<22} {in_keyword_label}")
print(f"  {'Sort':<22} {'nearly impossible':<22} {'sort()'}")
print(f"  {'50 students?':<22} {'50 variables!':<22} {'still 1 variable'}")
print("-" * 70)

# ============================================================
# KEY INSIGHT
# ============================================================

print("\n" + "=" * 55)
print("   KEY INSIGHT")
print("=" * 55)
print("""
  A LIST is a COLLECTION — one variable that can hold
  many values together, in order, under one name.

  Instead of:
    student_1 = "Aarav"
    student_2 = "Diya"
    ... (never ending)

  You write:
    student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

  Now you can loop, search, count, sort, add, and remove
  — all with Python's built-in tools!

  RULE OF THUMB:
  If you are creating variable_1, variable_2, variable_3...
  STOP! You almost certainly need a LIST instead.
""")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Why is hardcoding the count (count = 5) a bad idea?
#    What goes wrong when a new student joins?
# 2. What would happen if you had 100 students and used
#    separate variables? How many if-elif checks would you need
#    just to search for one name?
# 3. Sorting individual variables is described as "nearly
#    impossible". Why? What would you have to do manually?
# 4. Can you think of another real-life situation (outside school)
#    where you would need to store many similar items together?
#    (Hint: shopping cart, cricket team, playlist...)
# ============================================================
