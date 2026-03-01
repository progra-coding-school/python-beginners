# Looping Through Lists
# There are 3 ways to loop through a list. Each has a different use:
#   Style 1: for item in list           → when you only need the items
#   Style 2: for i in range(len(list))  → when you need the index to modify items
#   Style 3: enumerate(list)            → when you need BOTH the index AND the item

team = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

# --- Style 1: for item in list ---
# Simplest and most readable — gives you each item directly
# Use this when you just want to read or print each item
print("Style 1: for item in list")
for player in team:
    print("  -", player)

print()

# --- Style 2: for i in range(len(list)) ---
# Gives you index numbers 0, 1, 2 ... which lets you access list[i]
# Use this when you need to CHANGE items in the list (you need the index for assignment)
print("Style 2: for i in range(len(list))")
for i in range(len(team)):
    print("  index " + str(i) + " : " + team[i])

print()

# --- Style 3: enumerate() — index + item together ---
# enumerate() gives you both the index AND the item at the same time
# More readable than Style 2 when you need both
print("Style 3: enumerate()")
for i, player in enumerate(team):
    print("  " + str(i) + ". " + player)

print()

# Quick guide on which style to use
print("Use Style 1 when: you only need the items")
print("Use Style 2 when: you need the index to modify items")
print("Use Style 3 when: you need BOTH index and item")
print()

# --- Example: modify items using index (Style 2 in action) ---
# We cannot use Style 1 here — "for mark in marks" gives a copy, not the actual slot
marks = [80, 92, 75, 88, 95]
print("Original marks:", marks)

for i in range(len(marks)):
    if marks[i] < 80:
        marks[i] = 80       # raise any mark below 80 up to 80 (minimum mark rule)
print("After minimum = 80:", marks)

print()

# --- Example: numbered list using enumerate (Style 3 in action) ---
# start=1 makes the numbering begin at 1 instead of 0 (more natural for users)
shopping = ["milk", "eggs", "bread", "butter"]
print("Shopping list:")
for i, item in enumerate(shopping, start=1):
    print("  " + str(i) + ". " + item)
