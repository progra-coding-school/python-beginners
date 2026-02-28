# Program Code: DC-FC-03
# Title: Memory Recall Challenge
# Cognitive Skill: Focus and Concentration
# Topic: Dictionaries in Python

# Read each dictionary carefully for 30 seconds.
# Then scroll down and answer the questions FROM MEMORY.
# Then run the code to verify!

# ─── Memorise this dictionary ───────────────────────────────────
player_stats = {
    "Aarav":   {"runs": 45,  "wickets": 2, "catches": 1},
    "Diya":    {"runs": 62,  "wickets": 0, "catches": 3},
    "Karthik": {"runs": 18,  "wickets": 4, "catches": 2},
    "Riya":    {"runs": 33,  "wickets": 1, "catches": 0},
    "Ananya":  {"runs":  0,  "wickets": 3, "catches": 2},
}

print("=== Player Stats (study for 30 seconds) ===")
for name, stats in player_stats.items():
    print(f"  {name:<10}  Runs: {stats['runs']:>3}  Wickets: {stats['wickets']}  Catches: {stats['catches']}")

print()
print("─" * 50)
print("Now answer the questions below WITHOUT looking up ↑")
print("─" * 50)
print()

# --- Q1: How many players are in the dictionary? ---
answer_q1 = len(player_stats)
print(f"Q1: Total players = {answer_q1}")

# --- Q2: Who took the most wickets? ---
top_bowler = max(player_stats, key=lambda n: player_stats[n]["wickets"])
print(f"Q2: Most wickets  = {top_bowler} ({player_stats[top_bowler]['wickets']} wickets)")

# --- Q3: What was Riya's run count? ---
print(f"Q3: Riya's runs   = {player_stats['Riya']['runs']}")

# --- Q4: How many total runs did the team score? ---
total_runs = sum(p["runs"] for p in player_stats.values())
print(f"Q4: Total runs    = {total_runs}")

# --- Q5: Which player made zero catches? ---
zero_catches = [name for name, s in player_stats.items() if s["catches"] == 0]
print(f"Q5: Zero catches  = {zero_catches}")

# --- Q6: What is the average run score? ---
avg_runs = total_runs / len(player_stats)
print(f"Q6: Average runs  = {avg_runs:.1f}")

print()
print("─" * 50)
print("How many did you get right without looking?")
print("  5-6 correct → Excellent focus!")
print("  3-4 correct → Good — try again with a timer.")
print("  0-2 correct → Slow down and re-read carefully.")

# Think:
# 1. Which stat was hardest to remember — runs, wickets, or catches? Why?
# 2. What technique (grouping, patterns, stories) could help you memorise a dictionary faster?
