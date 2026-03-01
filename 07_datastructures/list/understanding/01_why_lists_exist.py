# Why Lists Exist
# Before lists, we stored multiple values in separate variables.
# This breaks down quickly — imagine 50 players, 50 variables!
# Lists solve this by holding many values in ONE variable,
# making it easy to add, loop, and calculate across all items at once.

# --- Without a list: separate variables ---
# Every new player needs a new variable. Adding a 6th means editing the code!
print("Without a list:")
player1 = "Aarav"
player2 = "Diya"
player3 = "Kabir"
player4 = "Meera"
player5 = "Rohan"

print(player1, player2, player3, player4, player5)

# Adding a 6th player needs a brand new variable — messy and hard to scale!
player6 = "Kumar"
print(player1, player2, player3, player4, player5, player6)

print()

# --- With a list: one variable, unlimited players ---
# One variable holds all players. Adding more is just one line.
print("With a list:")
team = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
print(team)

# Adding a player is always just one line — no new variables needed
team.append("Kumar")
print("After adding Kumar:", team)

# Loop through ALL players with a single for loop
# With variables, you would need to write print(player1), print(player2)... manually
print()
print("All players:")
for player in team:
    print("  -", player)

# len() tells us how many items are in the list — works for any size
print("Total players:", len(team))

print()

# --- When lists really shine: working with large data ---
# With 10 separate variables, max/min/sum would be impossible to calculate cleanly.
# With a list, Python built-in functions do all the work!
marks = [85, 92, 78, 65, 88, 70, 95, 55, 80, 74]
print("Class marks:", marks)
print("Highest:", max(marks))           # finds the maximum in one step
print("Lowest:", min(marks))            # finds the minimum in one step
print("Average:", sum(marks) / len(marks))  # sum() adds all, len() counts all
