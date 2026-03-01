# Naming Your Lists


# Mani's code — confusing names
print("Mani's code (hard to read):")
l    = ["Aarav", "Diya", "Kabir"]   # l looks like the number 1!
x    = [85, 92, 78]                  # x tells us nothing
temp = []                            # temp — temporary WHAT?

print("  l    =", l)
print("  x    =", x)
print("  temp =", temp)
best_idx = x.index(max(x))
print("  Best score:", x[best_idx], "by", l[best_idx])
print("  Problems: 'l' looks like 1, 'x' could mean anything, 'temp' has no purpose")
print()

# Aarav's code — same program, clear names
print("Aarav's code (easy to read):")
student_names   = ["Aarav", "Diya", "Kabir"]
student_marks   = [85, 92, 78]
sorted_students = []

print("  student_names   =", student_names)
print("  student_marks   =", student_marks)
top_idx = student_marks.index(max(student_marks))
print("  Best mark:", student_marks[top_idx], "by", student_names[top_idx])
print("  Each name tells you exactly what the list holds.")
print()

# Naming rules
print("Naming rules:")
print("  1. snake_case        → student_names  (not StudentNames or studentnames)")
print("  2. Descriptive       → cricket_scores (not x or data)")
print("  3. Plural nouns      → student_marks  (it is a list, so use plural)")
print("  4. Match the content → sorted_players (name shows it is already sorted)")
print("  5. No single letters → only i, j, k are ok — inside loops only")
print()

# Your Turn — suggest better names
print("Your Turn — Suggest Better Names")
print()

print("Scenario 1: m = ['Aarav', 'Rohan', 'Kabir'] — cricket team players")
s1 = input("  Better name for 'm': ").strip()
if "player" in s1.lower() or "cricket" in s1.lower() or "team" in s1.lower():
    print("  Good! 'cricket_players' or 'team_members' is perfect.")
else:
    print("  Suggested: 'cricket_players' or 'team_members'")
    print("  Tip: the name should say WHAT (players) and CONTEXT (cricket/team).")
print()

print("Scenario 2: y2 = [45, 78, 90, 55] — Maths test marks")
s2 = input("  Better name for 'y2': ").strip()
if "mark" in s2.lower() or "score" in s2.lower() or "maths" in s2.lower():
    print("  Excellent! 'maths_scores' or 'maths_marks' tells the full story.")
else:
    print("  Suggested: 'maths_scores' or 'maths_marks'")
    print("  Tip: include the subject AND what the numbers represent.")
print()

print("Scenario 3: zz = ['Monday', 'Wednesday'] — days Priya was absent")
s3 = input("  Better name for 'zz': ").strip()
if "absent" in s3.lower() or "miss" in s3.lower() or "days" in s3.lower():
    print("  Well done! 'absent_days' or 'missed_days' is clear and professional.")
else:
    print("  Suggested: 'absent_days' or 'missed_days'")
    print("  Tip: the name should say what the days represent, not just 'days'.")
print()

print("Good names make code read like English sentences.")
print("  BAD:  for i in x: if i > y: z.append(l[x.index(i)])")
print("  GOOD: for mark in student_marks:")
print("            if mark > passing_mark:")
print("                top_students.append(student_names[student_marks.index(mark)])")
