# Program Code: LP-ST-03
# Title: Organise the Loop — Accumulator Pattern
# Cognitive Skill: Structured Thinking (Data Organisation)
# Topic: Loops in Python

# Complex programs have many things to track inside a loop.
# Organise them into clear groups: setup → loop → output.

# PROBLEM: Analyse a cricket team's batting scorecard

innings = [
    ("Aarav",   72,  85),   # name, runs, balls
    ("Karthik", 45,  60),
    ("Diya",   103,  98),
    ("Riya",    28,  40),
    ("Aman",    15,  20),
    ("Rohan",    0,   3),
]

# --- GROUP 1: Setup (before the loop) ---
total_runs     = 0
total_balls    = 0
highest_score  = 0
top_scorer     = ""
half_centuries = 0
centuries      = 0
ducks          = 0    # scored 0

# --- GROUP 2: The Loop (process each batsman) ---
print("=== Batting Scorecard ===")
print(f"  {'Batsman':12} {'Runs':6} {'Balls':6} {'SR':8} {'Status'}")
print("  " + "-" * 50)

for name, runs, balls in innings:
    # Calculate strike rate
    strike_rate = (runs / balls) * 100 if balls > 0 else 0

    # Determine achievement
    if runs == 0:
        achievement = "Duck"
        ducks += 1
    elif runs >= 100:
        achievement = "Century!"
        centuries += 1
    elif runs >= 50:
        achievement = "50+"
        half_centuries += 1
    else:
        achievement = "-"

    # Accumulate team totals
    total_runs  += runs
    total_balls += balls

    # Track highest
    if runs > highest_score:
        highest_score = runs
        top_scorer    = name

    print(f"  {name:12} {runs:6} {balls:6} {strike_rate:7.1f}  {achievement}")

# --- GROUP 3: Output (after the loop) ---
team_strike_rate = (total_runs / total_balls) * 100 if total_balls > 0 else 0

print("  " + "-" * 50)
print(f"\n=== Team Summary ===")
print(f"  Total runs      : {total_runs}")
print(f"  Total balls     : {total_balls}")
print(f"  Team strike rate: {team_strike_rate:.1f}")
print(f"  Top scorer      : {top_scorer} ({highest_score} runs)")
print(f"  Centuries       : {centuries}")
print(f"  Half-centuries  : {half_centuries}")
print(f"  Ducks           : {ducks}")

# Think:
# 1. Where would you add code to find the LOWEST scorer?
# 2. How would you reorganise this to also show overs (balls/6)?
