# What is a List?
# A list is a single variable that holds MANY items together.
# Think of it like a tiffin box — one box, many compartments inside.
# In Python, a list is written with square brackets [ ] and items separated by commas.
# Example: team = ["Aarav", "Kabir", "Rohan"]

# OLD WAY – One variable per player (gets messy fast!)
# Imagine doing this for 50 players — 50 variables!
player1 = "Aarav"
player2 = "Kabir"
player3 = "Rohan"
player4 = "Meera"
player5 = "Diya"

print("Player 1:", player1)
print("Player 2:", player2)
print("Player 3:", player3)
print("Player 4:", player4)
print("Player 5:", player5)

# NEW WAY – All 5 players in ONE variable using a List
# cricket_team is a list of strings (names)
cricket_team = ["Aarav", "Kabir", "Rohan", "Meera", "Diya"]
print("Cricket Team:", cricket_team)

# Lists can hold strings, numbers, or even be empty
# student_names → list of strings
# exam_marks    → list of numbers (integers)
# shopping_list → empty list — we can add items to it later
student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
exam_marks = [88, 95, 72, 100, 65]
shopping_list = []

print("Student Names:", student_names)
print("Exam Marks:", exam_marks)
print("Shopping List:", shopping_list)

# Accessing items by INDEX
# Every item has a position number called an index.
# Index always starts at 0, not 1!
# cricket_team[0] → "Aarav"  (1st item, index 0)
# cricket_team[1] → "Kabir"  (2nd item, index 1)
# cricket_team[-1] → "Diya"  (last item — negative index counts from the right)
print("First player:", cricket_team[0])
print("Second player:", cricket_team[1])
print("Last player:", cricket_team[-1])

# Length of list — len() counts how many items are in the list
team_size = len(cricket_team)
print("Team size:", team_size)

# Last index is always len(list) - 1
# A list with 5 items has indices 0, 1, 2, 3, 4 → last index = 4 = 5 - 1
last_index = len(cricket_team) - 1
print("Last index:", last_index)
print("Last player using last index:", cricket_team[last_index])
