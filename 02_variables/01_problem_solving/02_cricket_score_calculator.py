# Program Code: CS-PS-02
# Title: Aarav's Cricket Score Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav played a cricket match yesterday.
# His coach asks: "What was your total score?"
# But a cricket score is not just ONE number!
# It is made up of MANY parts: fours, sixes, singles, doubles...
# Let's break down the score into its parts!
# ============================================================

# ------------------------------------------------------------
# DECOMPOSITION PLAN:
# Big Question: "What is Aarav's total score?"
#
# Smaller Questions:
#   1. How many FOURS did he hit? (each four = 4 runs)
#   2. How many SIXES did he hit? (each six = 6 runs)
#   3. How many SINGLES did he run? (each single = 1 run)
#   4. How many DOUBLES did he run? (each double = 2 runs)
#   5. How many BALLS did he face? (for strike rate)
# ------------------------------------------------------------

print("=== Aarav's Cricket Score Calculator ===")
print()

# STEP 1: Break the score into parts
fours = int(input("How many FOURS did Aarav hit? : "))
sixes = int(input("How many SIXES did Aarav hit? : "))
singles = int(input("How many SINGLES did he run? : "))
doubles = int(input("How many DOUBLES did he run? : "))
balls_faced = int(input("How many BALLS did he face? : "))

# STEP 2: Calculate each part separately
runs_from_fours = fours * 4
runs_from_sixes = sixes * 6
runs_from_singles = singles * 1
runs_from_doubles = doubles * 2

# STEP 3: Combine all parts
total_runs = runs_from_fours + runs_from_sixes + runs_from_singles + runs_from_doubles

# STEP 4: Calculate strike rate
# Strike Rate = (Total Runs / Balls Faced) * 100
strike_rate = (total_runs / balls_faced) * 100

# Display the complete scorecard
print()
print("=" * 40)
print("AARAV'S SCORECARD")
print("=" * 40)
print(f"Fours:   {fours} x 4 = {runs_from_fours} runs")
print(f"Sixes:   {sixes} x 6 = {runs_from_sixes} runs")
print(f"Singles: {singles} x 1 = {runs_from_singles} runs")
print(f"Doubles: {doubles} x 2 = {runs_from_doubles} runs")
print("-" * 40)
print(f"TOTAL RUNS:   {total_runs}")
print(f"Balls Faced:  {balls_faced}")
print(f"Strike Rate:  {strike_rate}")
print("=" * 40)

# ============================================================
# REFLECTION PROMPTS:
# 1. We broke "total score" into 4 types of runs.
#    What would you add if there were EXTRAS (wides, no-balls)?
# 2. Each type of run became its OWN variable.
#    Why is that better than calculating everything in one line?
# 3. Try this: Add a variable for "threes" (3 runs).
#    How does the code change?
# ============================================================
