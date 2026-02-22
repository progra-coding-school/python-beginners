# Program Code: STR-ST-03
# Title: Organise the Data — Structure Your String Information!
# Cognitive Skill: Structured Thinking (Data organisation)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Progra school has data about students, teachers, and events.
# The data is a MESS — everything is mixed up.
# Aarav must ORGANISE all the string data using prefixes
# and smart naming so the program is easy to read and update.
# ============================================================

print("=" * 55)
print("  ORGANISE THE DATA — STRUCTURED STRING VARIABLES!")
print("=" * 55)

# -------------------------------------------------------
# ❌ MESSY VERSION — all data mixed together
# -------------------------------------------------------
print("\n--- ❌ MESSY VERSION ---")

# Nobody knows what these belong to!
name1    = "Aarav Sharma"
name2    = "Ms. Priya Devi"
name3    = "Annual Science Fair"
subject1 = "Python Beginners"
subject2 = "Mathematics"
city     = "Chennai"
date1    = "21-02-2026"
date2    = "15-03-2026"

print(f"  {name1}, {name2}, {name3}")
print(f"  {subject1}, {subject2}, {city}, {date1}, {date2}")
print("  ← Hard to tell: which name is a student? Which is an event?")

# -------------------------------------------------------
# ✅ ORGANISED VERSION — prefix-based grouping
# -------------------------------------------------------
print("\n--- ✅ ORGANISED VERSION (Prefix-based naming) ---\n")

# GROUP 1: Student data (prefix: student_)
student_name    = "Aarav Sharma"
student_grade   = "Grade 6"
student_batch   = "Morning"
student_city    = "Chennai"
student_id      = "STU-AAR-2026"

# GROUP 2: Teacher data (prefix: teacher_)
teacher_name    = "Ms. Priya Devi"
teacher_subject = "Python Beginners"
teacher_room    = "Room 204"

# GROUP 3: Event data (prefix: event_)
event_name      = "Annual Science Fair"
event_date      = "21-02-2026"
event_venue     = "School Auditorium, Chennai"
event_theme     = "Technology and Innovation"

# -------------------------------------------------------
# Display each group neatly
# -------------------------------------------------------
print("=" * 50)
print("  STUDENT PROFILE")
print("-" * 50)
print(f"  Name    : {student_name}")
print(f"  Grade   : {student_grade}")
print(f"  Batch   : {student_batch}")
print(f"  City    : {student_city}")
print(f"  ID      : {student_id}")

print()
print("=" * 50)
print("  TEACHER PROFILE")
print("-" * 50)
print(f"  Name    : {teacher_name}")
print(f"  Subject : {teacher_subject}")
print(f"  Room    : {teacher_room}")

print()
print("=" * 50)
print("  UPCOMING EVENT")
print("-" * 50)
print(f"  Event   : {event_name}")
print(f"  Date    : {event_date}")
print(f"  Venue   : {event_venue}")
print(f"  Theme   : {event_theme}")
print("=" * 50)

# -------------------------------------------------------
# USING STRING OPERATIONS to derive more info
# -------------------------------------------------------
print("\n--- Auto-Generated Information ---")

# Derive initials from student name
parts           = student_name.split()
student_initials = parts[0][0] + "." + parts[1][0] + "."
print(f"  Student Initials  : {student_initials}")

# Derive event year from event_date
event_year = event_date[-4:]
print(f"  Event Year        : {event_year}")

# Build a formatted announcement
announcement = (
    f"📢 {event_name} on {event_date} at {event_venue}. "
    f"Theme: {event_theme}. "
    f"Hosted by Progra Kids Coding School."
)
print(f"\n  ANNOUNCEMENT:\n  {announcement}")

print("\n" + "=" * 55)
print("  KEY IDEA: Group related data with consistent prefixes.")
print("  student_*, teacher_*, event_* → easy to find and update!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. How do prefixes help organise string variables?
# 2. What would you name variables for an attendance system?
# 3. How did we derive student_initials from student_name?
# ============================================================
