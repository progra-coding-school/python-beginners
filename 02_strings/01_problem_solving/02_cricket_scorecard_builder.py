# Program Code: STR-PS-02
# Title: Cricket Scorecard Builder — Format the Match Report!
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav's school cricket match just ended.
# The scorer has all the data as raw text:
#   Player names in mixed case, scores as numbers.
# He needs to build a neat, formatted scorecard using strings!
# ============================================================
# DECOMPOSE THE PROBLEM:
# Step 1: Collect team and player data
# Step 2: Format each player's name properly
# Step 3: Build the scorecard display using string operations
# Step 4: Show total and result
# ============================================================

print("=" * 50)
print("    PROGRA KIDS CRICKET — MATCH SCORECARD")
print("=" * 50)

# STEP 1: Match Details
team_name   = "progra pythons"
opponent    = "chennai coders"
match_venue = "MG Ground, Chennai"
match_date  = "21-02-2026"

# STEP 2: Format team names
team_display     = team_name.title()
opponent_display = opponent.title()

print("\n  Match : " + team_display + "  vs  " + opponent_display)
print("  Venue : " + match_venue)
print("  Date  : " + match_date)
print()

# STEP 3: Player batting scorecard
# Format: (raw_name, runs, balls, fours, sixes)
players = [
    ("aarav sharma",   45, 32, 5, 2),
    ("mani kumar",     30, 25, 4, 0),
    ("ravi krishnan",  20, 18, 2, 1),
    ("diya nair",      15, 12, 1, 0),
    ("priya venkat",   10,  8, 1, 0),
]

print("-" * 60)
print("  " + "BATSMAN".ljust(22) + "RUNS".rjust(5) + "BALLS".rjust(6) + "4s".rjust(4) + "6s".rjust(4))
print("-" * 60)

total_runs = 0

for raw_name, runs, balls, fours, sixes in players:
    name = raw_name.title()                  # Proper case
    print("  " + name.ljust(22) + str(runs).rjust(5) + str(balls).rjust(6) + str(fours).rjust(4) + str(sixes).rjust(4))
    total_runs += runs

print("-" * 60)
print("  " + "TOTAL".ljust(22) + str(total_runs).rjust(5))
print("-" * 60)

# STEP 4: Result
opponent_score = 108

print()
if total_runs > opponent_score:
    margin = total_runs - opponent_score
    result = team_display + " WON by " + str(margin) + " runs! 🏆"
elif total_runs < opponent_score:
    margin = opponent_score - total_runs
    result = opponent_display + " won by " + str(margin) + " runs."
else:
    result = "MATCH TIED!"

print("  Opponent Score :", opponent_score)
print("  Our Score      :", total_runs)
print("\n  RESULT :", result)
print("\n" + "=" * 50)

# ============================================================
# REFLECTION:
# 1. What does .title() do to "aarav sharma"?
# 2. How would you add the player's position (Captain, WK)?
# 3. Can you modify this to take player names as input?
# ============================================================
