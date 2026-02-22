# Program Code: LIST-ST-01
# Title: Plan Before You Code — Organise Your Thinking First!
# Cognitive Skill: Structured Thinking (Planning)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav's teacher asked him to build a class marks report.
# The report must store student names and marks, find the
# topper, sort everyone by rank, and print a neat table.
#
# Before Aarav writes a SINGLE line of code, he sits down
# with a paper and plans EVERYTHING out.
#
# This file shows you:
#   → HOW to plan before coding
#   → HOW the plan becomes the code
#   → WHAT happens when you code WITHOUT a plan
# ============================================================

print("=" * 55)
print("  LIST-ST-01 | PLAN BEFORE YOU CODE")
print("  Organise Your Thinking First!")
print("=" * 55)

# ============================================================
# ===              AARAV'S PLANNING BLOCK                  ===
# ===         (Always write this BEFORE your code!)        ===
# ============================================================
#
# WHAT do we need to STORE?
#   → student_names  : list of student name strings
#   → student_marks  : list of integer marks (same order)
#
# WHAT OPERATIONS do we need?
#   → Add names and marks to the lists
#   → Find the maximum mark (topper)
#   → Sort students by marks (highest first)
#   → Display a neat ranked table
#
# WHAT is the EXPECTED OUTPUT?
#   → A ranked table like this:
#      Rank | Name   | Marks
#      1    | Aarav  | 95
#      2    | Diya   | 88
#      3    | Kabir  | 76
#
# HOW will we structure the CODE?
#   → Step 1: Set up the data (lists of names and marks)
#   → Step 2: Find the topper (max marks, index trick)
#   → Step 3: Sort both lists together by marks (highest first)
#   → Step 4: Display the ranked results in a neat table
#
# PLANNING DONE. Now let's write the code — step by step!
# ============================================================

print()
print("  Aarav planned his code first.")
print("  Now watch how cleanly the code follows the plan!")
print()

# -------------------------------------------------------
# STEP 1: Set up the data
# (Plan said: student_names list + student_marks list)
# -------------------------------------------------------
print("-" * 55)
print("  STEP 1: Set up the data")
print("-" * 55)

student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
student_marks = [88, 95, 76, 91, 83]

print("  student_names =", student_names)
print("  student_marks =", student_marks)
print()
print("  ✅ Two separate lists — same order, easy to link!")
print()

# -------------------------------------------------------
# STEP 2: Find the topper
# (Plan said: find max marks, use index to get the name)
# -------------------------------------------------------
print("-" * 55)
print("  STEP 2: Find the topper")
print("-" * 55)

highest_marks  = max(student_marks)
topper_index   = student_marks.index(highest_marks)
topper_name    = student_names[topper_index]

print(f"  Highest marks : {highest_marks}")
print(f"  Topper        : {topper_name}")
print()
print("  KEY TRICK: index() finds the POSITION of the max value.")
print("  Same position in student_names gives us the topper's name!")
print()

# -------------------------------------------------------
# STEP 3: Sort both lists together — by marks, highest first
# (Plan said: sort by marks descending, keep pairs linked)
# -------------------------------------------------------
print("-" * 55)
print("  STEP 3: Sort both lists together")
print("-" * 55)

# zip() pairs names and marks together so they sort as one unit
paired_data = list(zip(student_marks, student_names))

# Sort by marks (first item in each pair), reverse = highest first
paired_data.sort(reverse=True)

# Unpack back into separate sorted lists
sorted_marks = [marks for marks, name in paired_data]
sorted_names = [name  for marks, name in paired_data]

print("  Sorted (highest to lowest):")
for i in range(len(sorted_names)):
    print(f"    {sorted_names[i]} — {sorted_marks[i]}")
print()

# -------------------------------------------------------
# STEP 4: Display the ranked table
# (Plan said: print a neat ranked output)
# -------------------------------------------------------
print("=" * 55)
print("  STEP 4: Class Marks Report — Ranked Table")
print("=" * 55)
print(f"  {'RANK':<6} {'NAME':<12} {'MARKS':<8} {'STATUS'}")
print("  " + "-" * 40)

for rank in range(len(sorted_names)):
    rank_number = rank + 1
    name        = sorted_names[rank]
    marks       = sorted_marks[rank]
    status      = "Topper! " if rank_number == 1 else ""
    print(f"  {rank_number:<6} {name:<12} {marks:<8} {status}")

print("=" * 55)
print(f"  Class Topper: {topper_name} with {highest_marks} marks")
print("=" * 55)

# ============================================================
# NOW — SEE WHAT HAPPENS WITHOUT PLANNING
# ============================================================
print()
print("=" * 55)
print("  WITHOUT A PLAN — Mani's Messy Version")
print("=" * 55)
print()
print("  Mani jumped straight into coding without planning.")
print("  Here is a simplified version of what he wrote:")
print()

# This block shows the MESSY unstructured approach as a demo.
# Notice: no clear steps, confusing variable names, hard to fix.

print("  --- START OF MANI'S CODE (observe, don't copy!) ---")
print()

x = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
y = [88, 95, 76, 91, 83]
z = []
temp = []

# Mani tried to sort but forgot to keep names with marks
y_sorted = sorted(y, reverse=True)

# Now he doesn't know which name goes with which mark!
# He has to start over — wasted 20 minutes!

print("  x =", x)
print("  y_sorted =", y_sorted)
print("  Problem: which name goes with which mark? Nobody knows!")
print("  Mani had to DELETE his code and start again. ")
print()
print("  --- END OF MANI'S CODE ---")
print()

# ============================================================
# KEY LESSON
# ============================================================
print("=" * 55)
print("  KEY LESSON: A good plan saves more time than it costs.")
print("=" * 55)
print()
print("  Aarav spent 5 minutes planning.")
print("  He coded in 10 minutes. Done!")
print()
print("  Mani spent 0 minutes planning.")
print("  He coded for 20 minutes, hit a problem,")
print("  deleted everything, and started over.")
print()
print("  PLAN → STEP-BY-STEP THINKING → CLEAN CODE")
print()

# ============================================================
# PLANNING CHECKLIST — use this every time!
# ============================================================
print("=" * 55)
print("  YOUR PLANNING CHECKLIST (use before every program):")
print("=" * 55)
print()
print("  [ ] WHAT do I need to STORE?     → choose your lists")
print("  [ ] WHAT do I need to DO?        → list the operations")
print("  [ ] WHAT is the expected OUTPUT? → picture the result")
print("  [ ] HOW do I break it into STEPS?→ number them 1, 2, 3...")
print()
print("  Done? NOW write the code. Not before.")
print()
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What are the 4 planning questions Aarav asked before coding?
#    Write them from memory without looking at the file.
# 2. Why did Mani's approach fail? What specifically went wrong?
# 3. Why is it important to keep student_names and student_marks
#    in the same order? What would go wrong if they got mixed up?
# 4. Think of ONE program you have written before. Write a short
#    planning block for it now — WHAT, WHAT, WHAT, HOW.
# ============================================================
