# Program Code: 07-realworld-04
# Title: Cricket Team Selector

# Problem:
# A coach has 15 players. He needs to pick 11 for the match.
# Select the top 11 players based on their scores.

players = ["Rohit", "Virat", "Dhoni", "Bumrah", "Jadeja",
           "Ashwin", "Rahul", "Pant", "Shami", "Siraj",
           "Hardik", "Ishan", "Axar", "Shardul", "Gill"]

scores = [88, 95, 82, 78, 70,
          65, 90, 85, 60, 72,
          80, 55, 68, 50, 91]

# Combine players with their scores and sort by score
# Create a list of [score, player] pairs
player_scores = []
for i in range(len(players)):
    player_scores.append([scores[i], players[i]])

# Sort by score (descending - highest first)
player_scores.sort(reverse=True)

# Pick top 11
team = player_scores[:11]

print("--- Selected Playing 11 ---")
for i in range(len(team)):
    print(i + 1, ".", team[i][1], "- Score:", team[i][0])

# Who missed out?
bench = player_scores[11:]
print("\n--- On the Bench ---")
for player in bench:
    print(" -", player[1], "- Score:", player[0])
