# Program Code: LIST-ST-02
# Title: Naming Your Lists — Names That Tell the Story!
# Cognitive Skill: Structured Thinking (Naming conventions)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Mani and Aarav both wrote the same program — a student
# marks tracker for their class.
#
# Mani used single letters and cryptic short names.
# Aarav used clear, descriptive names.
#
# The PROGRAMS DO THE SAME THING. But one is easy to read
# and fix. The other is a nightmare.
#
# This file shows you WHY naming your lists properly is
# one of the most important thinking habits in coding.
# ============================================================

print("=" * 55)
print("  LIST-ST-02 | NAMING YOUR LISTS")
print("  Names That Tell the Story!")
print("=" * 55)

# ============================================================
# PART 1: MANI'S CODE — Confusing, cryptic names
# ============================================================
print()
print("=" * 55)
print("  PART 1: MANI'S CODE (Hard to read)")
print("=" * 55)
print()

# ❌ What is 'l'? Is it a list? A letter? A number? (looks like 1!)
l = ["Aarav", "Diya", "Kabir"]

# ❌ What is 'x'? Exam marks? X-coordinates? Nobody knows.
x = [85, 92, 78]

# ❌ What is 'temp'? Temporary? Temperature? A temporary student?
temp = []

# Now Mani tries to sort... but which variable holds the names?
# Which holds the marks? He has to scroll back and check every time.

print("  l    =", l)       # ❌ 'l' — ambiguous, looks like the number 1
print("  x    =", x)       # ❌ 'x' — tells us nothing about what is stored
print("  temp =", temp)    # ❌ 'temp' — temporary what? For what purpose?
print()

# Mani tries to find the best student — but he keeps forgetting
# which variable is which. He pauses, scrolls, re-reads...
best_score_index = x.index(max(x))
print(f"  Best score is: {x[best_score_index]} by {l[best_score_index]}")
print()

print("  ❌ Problems with Mani's naming:")
print("     - 'l' looks like the number 1 — very confusing!")
print("     - 'x' tells you nothing — is it marks? scores? IDs?")
print("     - 'temp' could mean anything — temporary? temperature?")
print("     - To understand the code, you must READ ALL of it first")
print("     - Finding bugs takes 3× longer with bad names")
print("     - Coming back after 1 week? You won't remember anything!")
print()

# Mani also tried to add a student interactively:
k = input("  Mani's prompt → Enter: ")   # ❌ Enter WHAT? A name? A mark?
print(f"  You entered: '{k}' — but was that supposed to be a name or a mark?")
print()

# ============================================================
# PART 2: AARAV'S CODE — The same program, properly named
# ============================================================
print("=" * 55)
print("  PART 2: AARAV'S CODE (Clear and readable)")
print("=" * 55)
print()

# ✅ student_names — instantly tells us: list of student names
student_names = ["Aarav", "Diya", "Kabir"]

# ✅ student_marks — instantly tells us: list of marks (numbers)
student_marks = [85, 92, 78]

# ✅ sorted_students — tells us: a list of students in sorted order
sorted_students = []

print("  student_names   =", student_names)   # ✅ crystal clear
print("  student_marks   =", student_marks)   # ✅ crystal clear
print("  sorted_students =", sorted_students) # ✅ clear purpose
print()

# Aarav finds the topper — reads like plain English!
top_mark_index = student_marks.index(max(student_marks))
top_student    = student_names[top_mark_index]
top_mark       = student_marks[top_mark_index]

print(f"  Best mark is: {top_mark} scored by {top_student}")
print()

print("  ✅ Benefits of Aarav's naming:")
print("     - 'student_names' — you know it's a list of student names")
print("     - 'student_marks' — you know it's a list of integer marks")
print("     - 'sorted_students' — you know it holds a sorted result")
print("     - Code reads almost like ENGLISH sentences")
print("     - Anyone — even a new coder — can understand it instantly")
print("     - Finding and fixing bugs is MUCH faster")
print()

# Aarav adds a student interactively with a clear prompt:
new_name = input("  Aarav's prompt → Enter student name: ")   # ✅ clear!
print(f"  You entered: '{new_name}' — clearly a student name!")
print()

# ============================================================
# NAMING RULES TABLE — the guide every coder needs
# ============================================================
print("=" * 55)
print("  LIST VARIABLE NAMING RULES:")
print("=" * 55)
print()

# Comparing BAD vs GOOD names side by side
#
# ❌ BAD NAME    | ✅ GOOD NAME           | WHY
# ─────────────────────────────────────────────────────────
# l              | student_names          | Tells what's in the list
# x              | exam_scores            | Tells the purpose clearly
# temp           | sorted_players         | Describes what it holds
# d              | days_of_week           | Clear and meaningful
# lst            | cricket_team           | Specific, not generic
# a              | attendance_records     | Full word, full meaning
# ─────────────────────────────────────────────────────────

naming_examples = [
    ("l",    "student_names",      "Tells you what is in the list"),
    ("x",    "exam_scores",        "Tells you the purpose clearly"),
    ("temp", "sorted_players",     "Describes what it holds"),
    ("d",    "days_of_week",       "Clear and meaningful — full word"),
    ("lst",  "cricket_team",       "Specific to topic, not generic"),
    ("a",    "attendance_records", "Full word, full purpose"),
]

print(f"  {'BAD NAME':<10} {'GOOD NAME':<24} WHY")
print("  " + "-" * 55)
for bad, good, reason in naming_examples:
    print(f"  {bad:<10} {good:<24} {reason}")

print()
print("  THE RULES (memorise these!):")
print()
print("  1. Use snake_case    → student_names  (not studentnames or StudentNames)")
print("  2. Be descriptive    → cricket_scores (not x or data)")
print("  3. Use plural nouns  → student_marks  (it's a list, so use plural)")
print("  4. Match the content → sorted_players (name shows it's sorted)")
print("  5. No single letters → ONLY i, j, k are ok — inside loops only!")
print()

# ============================================================
# INTERACTIVE: YOUR TURN! — Suggest better names
# ============================================================
print("=" * 55)
print("  YOUR TURN! — Suggest Better Names")
print("=" * 55)
print()
print("  Look at these 3 bad list variable names.")
print("  Think carefully about what they might store,")
print("  then suggest a better name for each one.")
print()

# Scenario 1 — list of cricket player names
print("  SCENARIO 1:")
print("    m = ['Aarav', 'Rohan', 'Kabir', 'Dev', 'Arjun']")
print("    This list stores the names of cricket team players.")
print()
name_suggestion_1 = input("  Your better name for 'm': ").strip()
print(f"  You said: '{name_suggestion_1}'")
if "player" in name_suggestion_1.lower() or "cricket" in name_suggestion_1.lower() or "team" in name_suggestion_1.lower():
    print("  Great thinking! A name like 'cricket_players' or 'team_members' is perfect.")
else:
    print("  Suggested name: 'cricket_players' or 'team_members'")
    print("  Tip: the name should tell us both WHAT (players) and CONTEXT (cricket/team).")
print()

# Scenario 2 — list of test scores
print("  SCENARIO 2:")
print("    y2 = [45, 78, 90, 55, 88, 62]")
print("    This list stores marks scored in a Maths test.")
print()
name_suggestion_2 = input("  Your better name for 'y2': ").strip()
print(f"  You said: '{name_suggestion_2}'")
if "mark" in name_suggestion_2.lower() or "score" in name_suggestion_2.lower() or "maths" in name_suggestion_2.lower():
    print("  Excellent! A name like 'maths_scores' or 'maths_marks' tells the full story.")
else:
    print("  Suggested name: 'maths_scores' or 'maths_marks'")
    print("  Tip: include the subject name AND what the numbers represent.")
print()

# Scenario 3 — list of days student was absent
print("  SCENARIO 3:")
print("    zz = ['Monday', 'Wednesday', 'Friday']")
print("    This list stores the days Priya was absent this week.")
print()
name_suggestion_3 = input("  Your better name for 'zz': ").strip()
print(f"  You said: '{name_suggestion_3}'")
if "absent" in name_suggestion_3.lower() or "miss" in name_suggestion_3.lower() or "days" in name_suggestion_3.lower():
    print("  Well done! 'absent_days' or 'missed_days' is clear and professional.")
else:
    print("  Suggested name: 'absent_days' or 'missed_days'")
    print("  Tip: the name should tell us what the days represent, not just 'days'.")
print()

# ============================================================
# FINAL SUMMARY
# ============================================================
print("=" * 55)
print("  REMEMBER:")
print("=" * 55)
print()
print("  Good naming = self-documenting code.")
print("  The BEST code reads almost like English sentences.")
print()
print("  BAD:  for i in x: if i > y: z.append(l[x.index(i)])")
print("  GOOD: for mark in student_marks:")
print("            if mark > passing_mark:")
print("                top_students.append(student_names[student_marks.index(mark)])")
print()
print("  Both do the same thing. One is a puzzle. One is a sentence.")
print()
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Why does naming matter if the program runs the same way
#    whether you use 'l' or 'student_names'?
# 2. What Python naming convention should you use for lists?
#    (snake_case, PascalCase, or camelCase?) Why?
# 3. Open a program you wrote last week. Can you still understand
#    every variable name without re-reading the full code?
#    If not — what would you rename?
# 4. Why is 'temp' considered a bad list name? Can you think
#    of 3 specific scenarios where 'temp' tells you nothing?
# ============================================================
