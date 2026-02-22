# Program Code: LIST-ST-03
# Title: Organise Data with Lists — Messy vs Structured Thinking
# Cognitive Skill: Structured Thinking (Data organisation)
# Topic: Lists in Python
#
# ════════════════════════════════════════════════════════
#  THE PROBLEM
# ════════════════════════════════════════════════════════
#
#  Arjun is building a student database for his school's
#  sports day. He stores the team names like this:
#
#  BAD WAY (messy and confusing):
#  data = ["Riya", "Red", "Arun", "Blue", "Sam", "Red", "Priya", "Green"]
#
#  - Which names are students? Which are team colours?
#  - You can't tell just by looking.
#  - This is UNSTRUCTURED data — hard to read, hard to use.
#
#  THE FIX: Use SEPARATE, CLEARLY NAMED lists.
#
# ════════════════════════════════════════════════════════
#  STRUCTURED APPROACH
# ════════════════════════════════════════════════════════

print("=" * 55)
print("  SPORTS DAY — TEAM ORGANISER")
print("=" * 55)
print()

# Clearly separated, named lists
students = ["Riya", "Arun", "Sam", "Priya", "Kiran", "Meena"]
teams    = ["Red",  "Blue", "Red", "Green", "Blue",  "Green"]

# students[0] → "Riya"   is in   teams[0] → "Red"
# students[1] → "Arun"   is in   teams[1] → "Blue"
# ... and so on (parallel lists)

print("  Student       Team")
print("  " + "-" * 30)

for i in range(len(students)):
    print(f"  {students[i]:<14} {teams[i]}")

print()

# ════════════════════════════════════════════════════════
#  ORGANISE FURTHER — Group by team
# ════════════════════════════════════════════════════════

red_team   = []
blue_team  = []
green_team = []

for i in range(len(students)):
    if teams[i] == "Red":
        red_team.append(students[i])
    elif teams[i] == "Blue":
        blue_team.append(students[i])
    else:
        green_team.append(students[i])

print("  RED TEAM  :", red_team)
print("  BLUE TEAM :", blue_team)
print("  GREEN TEAM:", green_team)
print()

# ════════════════════════════════════════════════════════
#  STRUCTURED THINKING RULES
# ════════════════════════════════════════════════════════

print("  STRUCTURED DATA RULES:")
print("  ─" * 27)
rules = [
    "1. One list = one type of data",
    "2. Name your list to match what it holds",
    "3. Use parallel lists to connect related data",
    "4. Group related items when needed",
    "5. Never mix different data types in one list",
]

for rule in rules:
    print(f"  {rule}")

print()
print("=" * 55)

# ════════════════════════════════════════════════════════
#  YOUR TURN
# ════════════════════════════════════════════════════════
#
#  TASK 1: Spot the structure problem
#  -----------------------------------
#  bad_list = ["Maths", 95, "Science", 88, "English", 72]
#
#  How would you reorganise this into proper lists?
#  Write your answer as comments below:
#
#  subjects = [...]
#  marks    = [...]
#
#  TASK 2: Add a new student
#  -----------------------------------
#  Add "Dev" to the Blue team.
#  Which TWO lists do you need to update?
#
#  TASK 3: Count team sizes
#  -----------------------------------
#  Without grouping into separate team lists,
#  count how many students are in "Red" using .count()
#
#  CHALLENGE:
#  Sort the students alphabetically and keep their
#  team assignments correct. (Hint: this is tricky —
#  think about what happens to the teams list!)
# ════════════════════════════════════════════════════════
