# Program Code: STR-PS-01
# Title: Name Tag Maker — Format Names for the School Event!
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Progra Kids Coding School is organising a Science Fair.
# Students type their names in different formats:
#   "  aarav sharma  ", "DIYA NAIR", "mANI kUMAR"
# The name tags must be printed in Proper Case with no extra spaces.
# Aarav must write a program to clean and format all names!
# ============================================================
# DECOMPOSE THE PROBLEM:
# Step 1: Take the student's name as input
# Step 2: Remove extra spaces (strip)
# Step 3: Convert to proper case (title)
# Step 4: Display the formatted name tag
# ============================================================

print("=" * 50)
print("    PROGRA SCIENCE FAIR — NAME TAG MAKER")
print("=" * 50)

# STEP 1: Take student name as input
raw_name = input("\nEnter student name (any format): ")

# STEP 2: Remove extra spaces
cleaned = raw_name.strip()

# STEP 3: Convert to Proper Case
formatted = cleaned.title()

# STEP 4: Display the name tag
print()
print("*" * 40)
print("*" + " " * 38 + "*")
print(f"*   PROGRA SCIENCE FAIR 2026           *")
print(f"*                                      *")
print(f"*   Name  : {formatted:<27} *")
print("*" + " " * 38 + "*")
print("*" * 40)

# -------------------------------------------------------
# BONUS: Process multiple students
# -------------------------------------------------------
print("\n--- BONUS: Format All Students in the List ---")

student_names = [
    "  aarav sharma  ",
    "DIYA NAIR",
    "mANI kUMAR",
    "  priya   ",
    "RAVI KRISHNAN",
]

print("\n  #  | Name on Tag")
print("  ---+------------------------")
for i, raw in enumerate(student_names, start=1):
    tag_name = raw.strip().title()
    print(f"  {i}  | {tag_name}")

print("\n✅ All name tags formatted and ready to print!")

# ============================================================
# REFLECTION:
# 1. What if a student types extra spaces in the middle of their name?
#    (Hint: Try "Aarav  Sharma" — does title() handle it?)
# 2. How would you also add their class or grade to the name tag?
# 3. Can you count how many students are in the list?
# ============================================================
