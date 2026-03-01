# Looping Through Lists

team = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

# --- Style 1: for item in list ---
print("Style 1: for item in list")
for player in team:
    print("  -", player)

print()

# --- Style 2: for i in range(len(list)) ---
print("Style 2: for i in range(len(list))")
for i in range(len(team)):
    print("  index " + str(i) + " : " + team[i])

print()

# --- Style 3: enumerate() — index + item together ---
print("Style 3: enumerate()")
for i, player in enumerate(team):
    print("  " + str(i) + ". " + player)

print()

# --- When to use which style ---
print("Use Style 1 when: you only need the items")
print("Use Style 2 when: you need the index to modify items")
print("Use Style 3 when: you need BOTH index and item")
print()

# --- Example: modify items using index ---
marks = [80, 92, 75, 88, 95]
print("Original marks:", marks)

for i in range(len(marks)):
    if marks[i] < 80:
        marks[i] = 80       # set minimum mark to 80
print("After minimum = 80:", marks)

print()

# --- Example: numbered list using enumerate ---
shopping = ["milk", "eggs", "bread", "butter"]
print("Shopping list:")
for i, item in enumerate(shopping, start=1):   # start numbering at 1
    print("  " + str(i) + ". " + item)
