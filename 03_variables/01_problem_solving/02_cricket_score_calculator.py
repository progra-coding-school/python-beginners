# Program Code: VAR-PS-02
# Title: Aarav's Cricket Score Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Variables in Python

# Big question: What is Aarav's total score?
# Break it into parts — one variable each.

fours = int(input("How many fours? "))
sixes = int(input("How many sixes? "))
singles = int(input("How many singles? "))
doubles = int(input("How many doubles? "))
balls_faced = int(input("How many balls faced? "))

runs_from_fours = fours * 4
runs_from_sixes = sixes * 6
runs_from_singles = singles * 1
runs_from_doubles = doubles * 2

total_runs = runs_from_fours + runs_from_sixes + runs_from_singles + runs_from_doubles
strike_rate = (total_runs / balls_faced) * 100

print("Fours:", fours, "x 4 =", runs_from_fours)
print("Sixes:", sixes, "x 6 =", runs_from_sixes)
print("Singles:", singles)
print("Doubles:", doubles, "x 2 =", runs_from_doubles)
print("Total runs:", total_runs)
print("Strike rate:", strike_rate)

# Think:
# 1. What variable would you add for extras (wides, no-balls)?
# 2. Why is it better to use separate variables for each type of run?
