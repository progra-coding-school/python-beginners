# What is a List? – Simple Version

# OLD WAY – Many variables
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

# NEW WAY – Using a List
cricket_team = ["Aarav", "Kabir", "Rohan", "Meera", "Diya"]
print("Cricket Team:", cricket_team)

# Different Lists
student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
exam_marks = [88, 95, 72, 100, 65]
shopping_list = []

print("Student Names:", student_names)
print("Exam Marks:", exam_marks)
print("Shopping List:", shopping_list)

# Accessing items
print("First player:", cricket_team[0])
print("Second player:", cricket_team[1])
print("Last player:", cricket_team[-1])

# Length of list
team_size = len(cricket_team)
print("Team size:", team_size)

# Last index
last_index = len(cricket_team) - 1
print("Last index:", last_index)
print("Last player using last index:", cricket_team[last_index])
