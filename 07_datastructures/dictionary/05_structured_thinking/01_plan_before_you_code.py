# Program Code: DC-ST-01
# Title: Plan Before You Code
# Cognitive Skill: Structured Thinking
# Topic: Dictionaries in Python

# Task: Build a Cricket Score Tracker for a match.
# Before writing a single line of code, answer the planning questions below.

# ─── PLANNING TEMPLATE ───────────────────────────────────────────
# Problem  : Track runs scored by each batsman in a cricket match.
# Inputs   : Player name, runs scored per ball/over
# Outputs  : Individual scores, total team score, highest scorer
# Structure: dictionary — player name (key) → runs (value)
# Steps    :
#   1. Define the score dictionary
#   2. Add/update scores as the match progresses
#   3. Calculate team total
#   4. Find highest scorer
#   5. Display the scorecard
# Edge cases: What if a player is out for 0? What if name is wrong?
# ─────────────────────────────────────────────────────────────────

print("=== Cricket Score Tracker ===")

# --- Step 1: Define scores (after planning, NOW write code) ---
scores = {
    "Aarav":   45,
    "Karthik": 62,
    "Riya":    18,
    "Diya":     0,   # out for a duck
    "Ananya":  33,
}

# --- Step 2: Update a score (e.g., a correction) ---
scores["Riya"] += 5     # 5 extra runs were miscounted
print("After correction:", scores["Riya"], "runs for Riya")
print()

# --- Step 3: Team total ---
total = sum(scores.values())
print(f"Team Total: {total} runs")
print()

# --- Step 4: Highest scorer ---
top_player = max(scores, key=scores.get)
print(f"Highest Scorer: {top_player} with {scores[top_player]} runs")
print()

# --- Step 5: Scorecard display ---
print("=== Scorecard ===")
print(f"  {'Player':<12} {'Runs':>5}")
print(f"  {'─'*12} {'─'*5}")
for player, runs in scores.items():
    status = " (not out)" if runs == max(scores.values()) else ""
    print(f"  {player:<12} {runs:>5}{status}")
print(f"  {'─'*12} {'─'*5}")
print(f"  {'Total':<12} {total:>5}")

# Think:
# 1. What new key would you add if you also wanted to track wickets taken?
# 2. Write out the 5-step plan for a "vote counter" before coding it.
