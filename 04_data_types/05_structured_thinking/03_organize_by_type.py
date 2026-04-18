# Program Code: DT-ST-03
# Title: Organize Data by Type
# Cognitive Skill: Structured Thinking (Data organization)
# Topic: Data Types in Python

# Good programs organize variables by type and purpose.
# This makes the code readable and reduces type errors.

print("--- Cricket Match Summary ---\n")

# --- Player Info (str) ---
player_name = "Virat"
team = "India"
opponent = "Australia"

# --- Stats (int) ---
balls_faced = 65
fours = 8
sixes = 3
runs = 92

# --- Calculated (float) ---
strike_rate = round((runs / balls_faced) * 100, 2)
runs_from_boundaries = (fours * 4) + (sixes * 6)
other_runs = runs - runs_from_boundaries

# --- Status (bool) ---
is_century = runs >= 100
is_half_century = runs >= 50
is_man_of_match = runs > 75 and strike_rate > 130

print("Player: " + player_name + " (" + team + " vs " + opponent + ")")
print("Runs:", runs, "off", balls_faced, "balls")
print("Boundaries:", fours, "fours,", sixes, "sixes (" + str(runs_from_boundaries) + " runs from boundaries)")
print("Other runs:", other_runs)
print("Strike rate:", strike_rate)
print("Half century:", is_half_century, " |  Century:", is_century)
print("Man of the Match:", is_man_of_match)

# Think:
# 1. Which variables are float? Why?
# 2. Why is 'is_man_of_match' a bool and not a str like "yes"?
# 3. What other variables would you add for a full cricket scorecard?
