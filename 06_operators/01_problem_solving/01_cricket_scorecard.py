# Program Code: OP-PS-01
# Title: Cricket Scorecard Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Operators in Python

# Big question: How do we calculate a batsman's full scorecard?
# Break it into smaller calculations — one operator at a time.

print("=== Cricket Scorecard Calculator ===")
print()

# Step 1: Get inputs
player_name = input("Enter batsman name: ")
fours = int(input("How many 4s did they hit? "))
sixes = int(input("How many 6s did they hit? "))
singles = int(input("How many singles? "))
balls_faced = int(input("How many balls faced? "))

# Step 2: Calculate runs from boundaries
runs_from_fours = fours * 4
runs_from_sixes = sixes * 6
runs_from_singles = singles * 1

# Step 3: Calculate total runs
total_runs = runs_from_fours + runs_from_sixes + runs_from_singles

# Step 4: Calculate strike rate (runs per 100 balls)
if balls_faced > 0:
    strike_rate = (total_runs / balls_faced) * 100
else:
    strike_rate = 0

# Step 5: Check if it's a half-century or century
is_half_century = total_runs >= 50 and total_runs < 100
is_century = total_runs >= 100

# Step 6: Display scorecard
print(f"\n--- Scorecard: {player_name} ---")
print(f"Fours: {fours}  →  Runs: {runs_from_fours}")
print(f"Sixes: {sixes}  →  Runs: {runs_from_sixes}")
print(f"Singles: {singles}")
print(f"Total Runs: {total_runs}")
print(f"Balls Faced: {balls_faced}")
print(f"Strike Rate: {round(strike_rate, 2)}")

if is_century:
    print("Achievement: CENTURY! Outstanding!")
elif is_half_century:
    print("Achievement: HALF CENTURY! Well played!")
else:
    print("Keep batting!")

# Think:
# 1. What new variable would you add to track dot balls (balls with 0 runs)?
# 2. How would you calculate the number of scoring shots vs dot balls?
