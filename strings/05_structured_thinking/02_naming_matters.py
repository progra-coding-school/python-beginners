# Program Code: STR-ST-02
# Title: Naming Matters — Good vs Bad String Variable Names!
# Cognitive Skill: Structured Thinking (Naming conventions)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav and Mani both wrote programs to display student info.
# Aarav used proper names. Mani used short, confusing names.
# Let's compare — and see WHY naming matters!
# ============================================================

print("=" * 55)
print("  NAMING MATTERS — CLEAR CODE vs CONFUSING CODE!")
print("=" * 55)

# -------------------------------------------------------
# MANI'S CODE — Hard to read, short names
# -------------------------------------------------------
print("\n--- MANI'S CODE (Confusing) ---")

n  = "aarav sharma"
s  = "progra python beginners"
b  = "morning"
c  = "chennai"
g  = "grade 6"

fn = n.strip().title()
sn = s.strip().title()
print(f"  {fn} | {sn} | {b.title()} | {c.title()} | {g.title()}")

print("""
  ❌ Problems with Mani's code:
     - What is 'n'? 's'? 'b'? 'c'? 'g'?
     - What does 'fn' and 'sn' mean?
     - You have to GUESS what each variable holds
     - Hard to maintain and debug later
""")

# -------------------------------------------------------
# AARAV'S CODE — Proper names, clear purpose
# -------------------------------------------------------
print("--- AARAV'S CODE (Clear and Readable) ---")

student_name  = "aarav sharma"
course_name   = "progra python beginners"
batch_time    = "morning"
student_city  = "chennai"
student_grade = "grade 6"

formatted_name   = student_name.strip().title()
formatted_course = course_name.strip().title()

print(f"  {formatted_name} | {formatted_course} | {batch_time.title()} | {student_city.title()} | {student_grade.title()}")

print("""
  ✅ Benefits of Aarav's code:
     - Each variable NAME tells you exactly what it stores
     - Anyone can read it — even someone new to the project
     - Easy to find and fix bugs
     - Professional code style
""")

# -------------------------------------------------------
# NAMING RULES FOR STRING VARIABLES
# -------------------------------------------------------
print("=" * 55)
print("  STRING VARIABLE NAMING RULES:")
print("=" * 55)
print()

# Comparing BAD vs GOOD names
examples = [
    ("s",           "student_name",    "Name of a student"),
    ("fn",          "first_name",      "First name only"),
    ("mssg",        "welcome_message", "Welcome message text"),
    ("ct",          "student_city",    "City where student lives"),
    ("x",           "raw_input",       "Unprocessed user input"),
    ("tmp",         "cleaned_name",    "Name after cleanup"),
    ("str1",        "school_name",     "Name of the school"),
]

print(f"  {'BAD NAME':<15} {'GOOD NAME':<22} {'PURPOSE'}")
print("  " + "-" * 55)
for bad, good, purpose in examples:
    print(f"  {bad:<15} {good:<22} {purpose}")

print()
print("  RULES:")
print("  1. Use snake_case   → student_name (not StudentName or studentname)")
print("  2. Be descriptive   → welcome_message (not wm or x)")
print("  3. Match the purpose → cleaned_name, raw_name (show the state)")
print("  4. No single letters → except i, j in loops (convention)")

# -------------------------------------------------------
# INTERACTIVE: How good is YOUR naming?
# -------------------------------------------------------
print("\n--- YOUR TURN: Name These Variables! ---")
print()
print("What would YOU name a variable that stores:")
print()

prompts = [
    "A student's full name after formatting",
    "The city where the school is located",
    "A welcome message to be printed",
]

for prompt in prompts:
    user_var = input(f"  → {prompt}: ").strip()
    print(f"     You said: '{user_var}'  ✅\n")

print("=" * 55)
print("  Good naming = self-documenting code!")
print("  The best code reads almost like English sentences.")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Why does naming matter if the program runs either way?
# 2. What naming convention does Python recommend? (snake_case)
# 3. Can you rename all of Mani's variables in your notebook?
# ============================================================
