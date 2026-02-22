# Program Code: FN-PS-03
# Title: Cricket Stats Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Functions in Python

# Big question: How do we calculate a complete cricket stats sheet?
# Break each stat into its own function.

def calculate_runs(fours, sixes, singles):
    return (fours * 4) + (sixes * 6) + singles

def calculate_strike_rate(runs, balls_faced):
    if balls_faced == 0:
        return 0
    return round((runs / balls_faced) * 100, 2)

def get_batting_label(runs):
    if runs >= 100:
        return "CENTURY!"
    elif runs >= 50:
        return "HALF CENTURY!"
    elif runs >= 30:
        return "Good knock"
    else:
        return "Short innings"

def calculate_bowling_economy(runs_given, overs_bowled):
    if overs_bowled == 0:
        return 0
    return round(runs_given / overs_bowled, 2)

def get_bowling_rating(economy):
    if economy <= 4:
        return "Excellent"
    elif economy <= 6:
        return "Good"
    elif economy <= 8:
        return "Average"
    else:
        return "Expensive"

def print_batting_card(name, fours, sixes, singles, balls_faced):
    runs = calculate_runs(fours, sixes, singles)
    strike_rate = calculate_strike_rate(runs, balls_faced)
    label = get_batting_label(runs)

    print(f"\n--- Batting: {name} ---")
    print(f"  4s: {fours}  6s: {sixes}  Singles: {singles}")
    print(f"  Total Runs:   {runs}")
    print(f"  Balls Faced:  {balls_faced}")
    print(f"  Strike Rate:  {strike_rate}")
    print(f"  Achievement:  {label}")

def print_bowling_card(name, wickets, runs_given, overs_bowled):
    economy = calculate_bowling_economy(runs_given, overs_bowled)
    rating = get_bowling_rating(economy)

    print(f"\n--- Bowling: {name} ---")
    print(f"  Wickets: {wickets}  Runs Given: {runs_given}  Overs: {overs_bowled}")
    print(f"  Economy:  {economy}")
    print(f"  Rating:   {rating}")

# --- Input and display ---
print("=== Cricket Stats Calculator ===")
print()

print("BATTING STATS")
bat_name    = input("Batsman name: ")
fours       = int(input("Number of 4s: "))
sixes       = int(input("Number of 6s: "))
singles     = int(input("Number of singles: "))
balls_faced = int(input("Balls faced: "))
print_batting_card(bat_name, fours, sixes, singles, balls_faced)

print()
print("BOWLING STATS")
bowl_name     = input("Bowler name: ")
wickets       = int(input("Wickets taken: "))
runs_given    = int(input("Runs given: "))
overs_bowled  = float(input("Overs bowled: "))
print_bowling_card(bowl_name, wickets, runs_given, overs_bowled)

# Think:
# 1. What function would you add to calculate the team's total runs?
# 2. How would you modify print_batting_card to also show the dot-ball count?
