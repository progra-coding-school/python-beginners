# Memory Recall Challenge
# Read the dictionary of cricket player stats carefully.
# Then cover the screen and answer the questions from memory.
# This builds concentration AND tests your understanding of how to query a nested dict.

# Study this for 30 seconds — runs, wickets, catches for each player
player_stats = {
    "Aarav":   {"runs": 45,  "wickets": 2, "catches": 1},
    "Diya":    {"runs": 62,  "wickets": 0, "catches": 3},
    "Karthik": {"runs": 18,  "wickets": 4, "catches": 2},
    "Riya":    {"runs": 33,  "wickets": 1, "catches": 0},
    "Ananya":  {"runs":  0,  "wickets": 3, "catches": 2},
}

print("Player Stats (study for 30 seconds):")
for name, stats in player_stats.items():
    print("  " + name.ljust(10) +
          " Runs: " + str(stats["runs"]).rjust(3) +
          "  Wickets: " + str(stats["wickets"]) +
          "  Catches: " + str(stats["catches"]))

print()
print("-" * 50)
print("Now answer the questions below WITHOUT looking up")
print("-" * 50)
print()

# Q1: number of players — len() counts the top-level keys
answer_q1 = len(player_stats)
print("Q1: Total players =", answer_q1)

# Q2: highest wickets — max with a lambda to compare the nested "wickets" value
# lambda n: player_stats[n]["wickets"] → for each player name n, return their wickets
top_bowler = max(player_stats, key=lambda n: player_stats[n]["wickets"])
print("Q2: Most wickets  =", top_bowler, "(" + str(player_stats[top_bowler]["wickets"]) + " wickets)")

# Q3: direct nested access — player_stats["Riya"]["runs"]
print("Q3: Riya's runs   =", player_stats["Riya"]["runs"])

# Q4: sum a value from every nested dict using a generator expression
# p["runs"] for p in player_stats.values() → give me "runs" from each player's inner dict
total_runs = sum(p["runs"] for p in player_stats.values())
print("Q4: Total runs    =", total_runs)

# Q5: list comprehension to collect players where catches == 0
# [name for name, s in ...] is the standard "filter items to a list" pattern
zero_catches = [name for name, s in player_stats.items() if s["catches"] == 0]
print("Q5: Zero catches  =", zero_catches)

# Q6: average — total divided by number of players
avg_runs = total_runs / len(player_stats)
print("Q6: Average runs  =", str(round(avg_runs, 1)))

print()
print("-" * 50)
print("How many did you get right without looking?")
print("  5-6 correct → Excellent focus!")
print("  3-4 correct → Good — try again with a timer.")
print("  0-2 correct → Slow down and re-read carefully.")
