# Organise Data with Lists
# Structured data means: each list holds ONE type of information.
# When data is organised properly, every operation becomes simple and clear.
# KEY RULE: one list = one kind of data. Never mix different things in one list.

# Problem: mixing data types in one list is confusing
# bad_list = ["Riya", "Red", "Arun", "Blue", "Sam", "Red"]
# Which names are students? Which are team colours? You cannot tell.

# Fix: use SEPARATE, clearly named parallel lists
# students[i] and teams[i] always belong to the same person

students = ["Riya", "Arun", "Sam", "Priya", "Kiran", "Meena"]
teams    = ["Red",  "Blue", "Red", "Green", "Blue",  "Green"]

# students[i] and teams[i] are always linked (parallel lists)
# students[0]="Riya" → teams[0]="Red" → Riya is in Red team

print("Student        Team")
print("-" * 25)
for i in range(len(students)):
    print("  " + students[i].ljust(14) + teams[i])
print()

# Group students by team using three collector lists
# Loop through once — check each student's team and append to the right group
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

print("RED TEAM  :", red_team)
print("BLUE TEAM :", blue_team)
print("GREEN TEAM:", green_team)
print()

# Five rules every programmer should follow when organising list data
rules = [
    "1. One list = one type of data",
    "2. Name your list to match what it holds",
    "3. Use parallel lists to connect related data",
    "4. Group related items when needed",
    "5. Never mix different data types in one list",
]
print("Structured Data Rules:")
for rule in rules:
    print("  " + rule)

# YOUR TURN (offline tasks):
#   Task 1: bad_list = ["Maths", 95, "Science", 88, "English", 72]
#           Reorganise into proper lists:
#           subjects = [...]
#           marks    = [...]
#
#   Task 2: Add "Dev" to the Blue team.
#           Which TWO lists do you need to update?
#
#   Task 3: Count how many students are in "Red" using teams.count("Red")
#
#   Challenge: Sort students alphabetically and keep their team assignments correct.
#              (Hint: think about what happens to the teams list when you sort only students!)
