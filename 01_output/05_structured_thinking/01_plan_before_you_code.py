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
# │  Contact info (right-aligned)        │
# └──────────────────────────────────────┘

# ---- CODE FOLLOWS THE PLAN ----

event_name  = "Annual Science Fair 2026"
school      = "Progra Kids Coding School"
date        = "Saturday, 15th March 2026"
time        = "9:00 AM – 4:00 PM"
venue       = "School Main Hall, Chennai"
details     = ("Join us for an exciting day of student innovations, "
               "science experiments, and coding demos. Open to all "
               "students from Grade 1 to Grade 10.")
contact     = "Contact: Mrs. Priya  |  9876543210"

w = 48

print()
print("*" * w)
print(f"*{event_name:^{w-2}}*")
print(f"*{school:^{w-2}}*")
print("*" * w)
print(f"*{'':^{w-2}}*")
print(f"*  {'Date  :':9} {date:<{w-14}}*")
print(f"*  {'Time  :':9} {time:<{w-14}}*")
print(f"*  {'Venue :':9} {venue:<{w-14}}*")
print(f"*{'':^{w-2}}*")
print("*" + "-" * (w-2) + "*")
print(f"*{'':^{w-2}}*")

# Wrap the details text across multiple lines
words = details.split()
line  = ""
for word in words:
    if len(line) + len(word) + 1 <= w - 6:
        line += word + " "
    else:
        print(f"*  {line:<{w-5}}*")
        line = word + " "
if line:
    print(f"*  {line:<{w-5}}*")

print(f"*{'':^{w-2}}*")
print("*" * w)
print(f"*  {contact:<{w-4}}*")
print("*" * w)
print()

# Think:
# 1. How would you add a RSVP section at the bottom?
# 2. What would you change to make this announcement fit on a narrow phone screen?
