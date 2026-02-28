# Program Code: OUT-ST-01
# Title: Plan Before You Code — Event Announcement
# Cognitive Skill: Structured Thinking (Planning)
# Topic: Output in Python

# Before writing print() statements, plan your OUTPUT layout:
# - What SECTIONS are needed?
# - What is the ORDER?
# - What FORMATTING makes it readable?
# - What WIDTH looks good?

# PROBLEM: Display a school event announcement.
#
# PLAN (output layout):
# ┌──────────────────────────────────────┐
# │         [BORDER — top]               │
# │       EVENT NAME (centred)           │
# │       SCHOOL NAME (centred)          │
# │         [DIVIDER]                    │
# │  Date:   ...                         │
# │  Time:   ...                         │
# │  Venue:  ...                         │
# │         [DIVIDER]                    │
# │  Details paragraph                   │
# │         [BORDER — bottom]            │
# │  Contact info                        │
# └──────────────────────────────────────┘

# ---- CODE FOLLOWS THE PLAN ----

event_name = "Annual Science Fair 2026"
school     = "Progra Kids Coding School"
date       = "Saturday, 15th March 2026"
time       = "9:00 AM – 4:00 PM"
venue      = "School Main Hall, Chennai"
details    = ("Join us for an exciting day of student innovations, "
              "science experiments, and coding demos. Open to all "
              "students from Grade 1 to Grade 10.")
contact    = "Contact: Mrs. Priya  |  9876543210"

w = 48

print()
print("*" * w)
print("*" + event_name.center(w-2) + "*")
print("*" + school.center(w-2) + "*")
print("*" * w)
print("*" + " " * (w-2) + "*")
print("*  " + "Date  :".ljust(9) + " " + date.ljust(w-14) + "*")
print("*  " + "Time  :".ljust(9) + " " + time.ljust(w-14) + "*")
print("*  " + "Venue :".ljust(9) + " " + venue.ljust(w-14) + "*")
print("*" + " " * (w-2) + "*")
print("*" + "-" * (w-2) + "*")
print("*" + " " * (w-2) + "*")

# Wrap the details text across multiple lines
words = details.split()
line  = ""
for word in words:
    if len(line) + len(word) + 1 <= w - 6:
        line += word + " "
    else:
        print("*  " + line.ljust(w-5) + "*")
        line = word + " "
if line:
    print("*  " + line.ljust(w-5) + "*")

print("*" + " " * (w-2) + "*")
print("*" * w)
print("*  " + contact.ljust(w-4) + "*")
print("*" * w)
print()

# Think:
# 1. How would you add a RSVP section at the bottom?
# 2. What would you change to make this announcement fit on a narrow phone screen?
