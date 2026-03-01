# Plan Before You Code — Cricket Score Tracker
# A dictionary is the perfect fit here: player name → runs.
# PLANNING TEMPLATE (answer these BEFORE writing a single line of code):
#   Problem  : Track runs scored by each batsman in a cricket match.
#   Inputs   : Player name, runs scored
#   Outputs  : Individual scores, team total, highest scorer
#   Structure: dictionary — player name (key) → runs (value)
#   Steps    : 1. Define scores  2. Update  3. Total  4. Topper  5. Display
#   Edge cases: Player out for 0? (valid — store 0 as value) Name typo? (check carefully)

print("Cricket Score Tracker")

# Step 1: Define the scores — initial data after the match
scores = {
    "Aarav":   45,
    "Karthik": 62,
    "Riya":    18,
    "Diya":     0,   # out for a duck — value is 0, still a valid entry
    "Ananya":  33,
}

# Step 2: Update a score (correction — 5 extra runs were miscounted for Riya)
scores["Riya"] += 5     # += modifies the existing value in place
print("After correction: Riya has", scores["Riya"], "runs")
print()

# Step 3: Team total — sum all values in one line
# sum(scores.values()) loops through all run values and adds them
total = sum(scores.values())
print("Team Total:", total, "runs")
print()

# Step 4: Highest scorer
# max(scores, key=scores.get) → finds the key (player name) whose value (runs) is maximum
# This is the standard pattern for "find the key of the max value in a dict"
top_player = max(scores, key=scores.get)
print("Highest Scorer:", top_player, "with", scores[top_player], "runs")
print()

# Step 5: Scorecard display
print("Scorecard:")
print("  " + "Player".ljust(12) + "Runs".rjust(5))
print("  " + "-" * 17)
for player, runs in scores.items():
    # Mark the top scorer with a label — show the note only for the max value
    status = " (top scorer)" if runs == max(scores.values()) else ""
    print("  " + player.ljust(12) + str(runs).rjust(5) + status)
print("  " + "-" * 17)
print("  " + "Total".ljust(12) + str(total).rjust(5))
