# Program Code: LIST-UN-04
# Title: Looping Through Lists — Visit Every Item!
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Kabir is a teacher at Progra Kids School.
# Every morning he does three things:
#   1. Greets every student by name
#   2. Calculates the total marks of the class
#   3. Finds which students were absent today
#
# He doesn't know in advance how many students will be there.
# (Some days 5, some days 8.)
#
# He needs a LOOP that can walk through the entire list,
# no matter how long it is.
#
# There are THREE ways to loop through a list in Python.
# Let's understand when and why to use each one!
# ============================================================

print("=" * 55)
print("   LOOPING THROUGH LISTS — VISIT EVERY ITEM!")
print("=" * 55)

print("""
SCENARIO: Kabir the teacher needs to:
  1. Greet every student by name
  2. Add up all the marks
  3. Find absent students

Let's explore 3 different ways to loop through a list.
""")

# ============================================================
# SETUP: Class data for today's session
# ============================================================

student_names     = ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Priya"]
student_marks     = [88, 72, 95, 61, 80, 74]
present_students  = ["Aarav", "Kabir", "Rohan", "Priya"]     # Who came today

# ============================================================
# PART 1: Simple for Loop — for item in list
# ============================================================

print("=" * 55)
print("   PART 1: Simple for Loop — for item in list")
print("=" * 55)

print("""
WHEN TO USE:
  When you only care about the VALUES — not the position.
  This is the most READABLE and most common loop.

SYNTAX:
  for item in list:
      # use item here
""")

# -----------------------------------------------------------
# Use Case A: Kabir greets every student
# -----------------------------------------------------------
print("-" * 40)
print("Use Case A: Morning Greeting")
print("-" * 40)

print()
for student_name in student_names:
    print(f"  Good morning, {student_name}! Ready to learn today?")

print()
print("  --> The loop visits EVERY name automatically.")
print("      Add or remove a student from the list — the loop adjusts!")

# -----------------------------------------------------------
# Use Case B: Calculate total marks of the class
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Use Case B: Total Marks of the Class")
print("-" * 40)

total_marks = 0

for single_mark in student_marks:
    total_marks = total_marks + single_mark    # Accumulate total

print(f"\n  Marks list : {student_marks}")
print(f"  Total marks: {total_marks}")
print(f"  Average    : {total_marks / len(student_marks):.1f}")

print()
print("  --> We didn't need to know HOW MANY students there are.")
print("      The loop handled every mark, one by one, automatically.")

# -----------------------------------------------------------
# Use Case C: Find absent students (check membership)
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Use Case C: Who Is Absent Today?")
print("-" * 40)

print(f"\n  All students   : {student_names}")
print(f"  Present today  : {present_students}")
print()
print("  Absent students:")

absent_count = 0
for student_name in student_names:
    if student_name not in present_students:
        print(f"    - {student_name} is ABSENT")
        absent_count += 1

print(f"\n  Total absent today: {absent_count}")

# ============================================================
# PART 2: Index Loop — for i in range(len(list))
# ============================================================

print("\n" + "=" * 55)
print("   PART 2: Index Loop — for i in range(len(list))")
print("=" * 55)

print("""
WHEN TO USE:
  When you need to know the INDEX (position) of each item.
  Useful for numbered output, comparing two lists by position,
  or updating items in the list.

SYNTAX:
  for i in range(len(list)):
      item = list[i]     # access item using index i
""")

# -----------------------------------------------------------
# Use Case A: Print roll numbers alongside names
# -----------------------------------------------------------
print("-" * 40)
print("Use Case A: Attendance Sheet with Roll Numbers")
print("-" * 40)

print()
print(f"  {'Roll No':<10} {'Name':<12} {'Marks'}")
print(f"  {'-'*7:<10} {'-'*10:<12} {'-'*5}")

for i in range(len(student_names)):
    roll_number   = i + 1                   # Roll number starts from 1 (not 0)
    name_at_index = student_names[i]
    mark_at_index = student_marks[i]
    print(f"  {roll_number:<10} {name_at_index:<12} {mark_at_index}")

print()
print("  --> We used the index 'i' to access BOTH lists at the same position.")
print("      student_names[i] and student_marks[i] are paired by index.")

# -----------------------------------------------------------
# Use Case B: Award bonus marks to everyone
# (Updating items in-place using the index)
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Use Case B: Add 5 Bonus Marks to Everyone")
print("-" * 40)

bonus_marks = 5
print(f"\n  Original marks : {student_marks}")

for i in range(len(student_marks)):
    student_marks[i] = student_marks[i] + bonus_marks    # Update in-place

print(f"  After +{bonus_marks} bonus  : {student_marks}")
print()
print("  --> We UPDATED the list using student_marks[i] = ...")
print("      This only works when you have the index.")
print("      A simple 'for mark in list' loop cannot do this!")

# ============================================================
# PART 3: enumerate() — Index + Value, Clean and Together
# ============================================================

print("\n" + "=" * 55)
print("   PART 3: enumerate() — Best of Both Worlds!")
print("=" * 55)

print("""
WHEN TO USE:
  When you need BOTH the index AND the value,
  but you want cleaner code than range(len(list)).

  enumerate() gives you a pair: (index, item)
  every time the loop runs.

SYNTAX:
  for index, item in enumerate(list):
      # use both index and item here
""")

# -----------------------------------------------------------
# Use Case A: Numbered list of students (cleaner version)
# -----------------------------------------------------------
print("-" * 40)
print("Use Case A: Print Numbered Student List (using enumerate)")
print("-" * 40)

print()
for index, student_name in enumerate(student_names):
    roll_number = index + 1         # Start roll number from 1
    print(f"  Roll {roll_number}: {student_name}")

print()
print("  Compare to Part 2 Use Case A:")
print("  enumerate() is cleaner — no need to write student_names[i]")

# -----------------------------------------------------------
# Use Case B: Find the position of the highest scorer
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Use Case B: Find the Highest Scorer and Their Position")
print("-" * 40)

print(f"\n  Marks (after bonus): {student_marks}")

highest_mark        = student_marks[0]
highest_mark_index  = 0

for index, mark in enumerate(student_marks):
    if mark > highest_mark:
        highest_mark        = mark
        highest_mark_index  = index

top_student_name = student_names[highest_mark_index]
print(f"\n  Top scorer    : {top_student_name}")
print(f"  Their mark    : {highest_mark}")
print(f"  Roll number   : {highest_mark_index + 1}")

# -----------------------------------------------------------
# Use Case C: Starting enumerate from a custom number
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Use Case C: Start Counting from a Custom Number")
print("-" * 40)

print("\n  Kabir wants roll numbers to start from 101 (not 1):")
print()

for roll_number, student_name in enumerate(student_names, start=101):
    print(f"  Roll {roll_number}: {student_name}")

print()
print("  enumerate(list, start=101) → index begins at 101!")

# ============================================================
# WHEN TO USE WHICH — Summary
# ============================================================

print("\n" + "=" * 55)
print("   WHEN TO USE WHICH LOOP")
print("=" * 55)
print()
print(f"  {'Loop Style':<38} {'Use When...'}")
print(f"  {'-'*35:<38} {'-'*30}")
print(f"  {'for item in list':<38} {'You only need VALUES (simplest)'}")
print(f"  {'for i in range(len(list))':<38} {'You need INDEX + able to update list'}")
print(f"  {'for index, item in enumerate(list)':<38} {'You need INDEX + VALUE (cleanest)'}")
print()
print("  RULE OF THUMB:")
print("  Start with 'for item in list'.")
print("  If you need the index, upgrade to enumerate().")
print("  Use range(len()) only when you need to MODIFY the list.")
print("=" * 55)

# ============================================================
# BONUS: Looping with a real-world cricket scorecard
# ============================================================

print("\n" + "=" * 55)
print("   BONUS: Cricket Scorecard (All 3 Styles)")
print("=" * 55)

batsmen_names  = ["Rohit", "Shubman", "Virat", "KL Rahul", "Hardik"]
batsmen_scores = [45, 80, 30, 62, 55]

print(f"\n  Batsmen : {batsmen_names}")
print(f"  Scores  : {batsmen_scores}")

# Style 1: Simple loop — just print each score
print("\n  Style 1 (for score in list): All scores")
for score in batsmen_scores:
    print(f"    Score: {score}")

# Style 2: Index loop — print with batter number
print("\n  Style 2 (range/len): Paired with batsman name")
for i in range(len(batsmen_names)):
    print(f"    {batsmen_names[i]}: {batsmen_scores[i]} runs")

# Style 3: enumerate — clean and numbered
print("\n  Style 3 (enumerate): Batting position + name + score")
for position, (batsman, score) in enumerate(zip(batsmen_names, batsmen_scores), start=1):
    print(f"    #{position} {batsman}: {score} runs")

# ============================================================
# REFLECTION:
# 1. What is the key difference between "for item in list"
#    and "for i in range(len(list))"?
#    When would you NEED to use range(len()) instead of
#    the simpler style?
# 2. Aarav writes: for i in range(len(student_names)):
#                      print(student_names[i])
#    Rewrite this using enumerate(). Which is more readable?
# 3. If you want to add up all values in a list using a loop,
#    which loop style would you use and why?
# 4. Kabir has two lists: names and scores (same length).
#    He wants to print them side by side: "Aarav: 88".
#    Which loop style is best for this and why?
# ============================================================
