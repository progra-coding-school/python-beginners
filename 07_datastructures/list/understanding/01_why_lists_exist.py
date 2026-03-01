# Why Lists Exist

# --- Without a list: separate variables ---
print("Without a list:")
player1 = "Aarav"
player2 = "Diya"
player3 = "Kabir"
player4 = "Meera"
player5 = "Rohan"

print(player1, player2, player3, player4, player5)

# Adding a 6th player needs a new variable — messy!
player6 = "Kumar"
print(player1, player2, player3, player4, player5, player6)

print()

# --- With a list: one variable, unlimited players ---
print("With a list:")
team = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
print(team)

# Adding a player is just one line
team.append("Kumar")
print("After adding Kumar:", team)

# Loop through all players easily
print()
print("All players:")
for player in team:
    print("  -", player)

# Find how many players
print("Total players:", len(team))

print()

# --- When lists really shine: large data ---
marks = [85, 92, 78, 65, 88, 70, 95, 55, 80, 74]
print("Class marks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))

# With separate variables, this would need 10 variables!
# Lists make it possible to handle any amount of data.
