# Program Code: CS-HO-01
# Title: Reverse Engineer - Decode the Output!
# Cognitive Skill: Higher Order Thinking (Analysis - working backwards)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Usually we READ code and PREDICT the output.
# But real engineers sometimes work BACKWARDS!
# They see the RESULT and figure out what code created it.
# This is called REVERSE ENGINEERING.
# Can you look at the output and figure out the variables?
# ============================================================

# ------------------------------------------------------------
# HOW TO PLAY:
# 1. You will see an OUTPUT (what the program printed)
# 2. Your job: Figure out what VARIABLES were used
# 3. Enter the variable values
# 4. Check if you decoded it correctly!
# ------------------------------------------------------------

score = 0

print("=== Reverse Engineer: Decode the Output! ===")
print("Look at the output. Figure out the variables!")
print()

# ----- ROUND 1 (Easy) -----
print("--- Round 1 ---")
print("This is the OUTPUT that was printed:")
print()
print('  ┌────────────────────────────────┐')
print('  │ Hello, my name is Diya         │')
print('  │ I am 10 years old              │')
print('  └────────────────────────────────┘')
print()
print("What variables produced this?")
name_guess = input("  What is the value of 'name'? : ")
age_guess = input("  What is the value of 'age'?  : ")
print()

# The actual code that produced it
name = "Diya"
age = 10
print(f"The code was:")
print(f'  name = "{name}"')
print(f'  age = {age}')
print(f'  print(f"Hello, my name is {{name}}")')
print(f'  print(f"I am {{age}} years old")')

if name_guess == "Diya" and age_guess == "10":
    print("Perfect decode!")
    score = score + 1
else:
    print(f"The answer was: name = 'Diya', age = 10")

input("\nPress Enter for Round 2...")
print()

# ----- ROUND 2 (Medium) -----
print("--- Round 2 ---")
print("This is the OUTPUT that was printed:")
print()
print('  ┌────────────────────────────────┐')
print('  │ Item: Samosa                    │')
print('  │ Price: Rs.15                    │')
print('  │ Quantity: 4                     │')
print('  │ Total: Rs.60                    │')
print('  └────────────────────────────────┘')
print()
print("What variables produced this?")
item_guess = input("  Value of 'item'?     : ")
price_guess = input("  Value of 'price'?    : ")
qty_guess = input("  Value of 'quantity'? : ")
total_guess = input("  Value of 'total'?    : ")
print()

item = "Samosa"
price = 15
quantity = 4
total = price * quantity

print("The code was:")
print(f'  item = "{item}"')
print(f'  price = {price}')
print(f'  quantity = {quantity}')
print(f'  total = price * quantity  # {price} * {quantity} = {total}')

if item_guess == "Samosa" and price_guess == "15" and qty_guess == "4" and total_guess == "60":
    print("Perfect decode!")
    score = score + 1
else:
    print("Check the values above. Did you figure out that total = price * quantity?")

input("\nPress Enter for Round 3...")
print()

# ----- ROUND 3 (Hard) -----
print("--- Round 3 (Challenge!) ---")
print("This is the OUTPUT that was printed:")
print()
print('  ┌─────────────────────────────────────┐')
print('  │         CRICKET SCORECARD            │')
print('  │ Player: Aarav                        │')
print('  │ Fours: 5 (20 runs)                   │')
print('  │ Sixes: 2 (12 runs)                   │')
print('  │ Total: 32 runs                       │')
print('  │ Balls: 18                            │')
print('  │ Strike Rate: 177.78                  │')
print('  └─────────────────────────────────────┘')
print()
print("What variables produced this?")
print("(Hint: Total = runs from fours + runs from sixes)")
print("(Hint: Strike Rate = total / balls * 100)")
fours_guess = input("  How many fours?        : ")
sixes_guess = input("  How many sixes?        : ")
balls_guess = input("  How many balls faced?  : ")
print()

player = "Aarav"
fours = 5
sixes = 2
runs_from_fours = fours * 4
runs_from_sixes = sixes * 6
total_runs = runs_from_fours + runs_from_sixes
balls = 18
strike_rate = round((total_runs / balls) * 100, 2)

print("The code was:")
print(f'  player = "{player}"')
print(f'  fours = {fours}')
print(f'  sixes = {sixes}')
print(f'  runs_from_fours = fours * 4     # {runs_from_fours}')
print(f'  runs_from_sixes = sixes * 6     # {runs_from_sixes}')
print(f'  total_runs = {runs_from_fours} + {runs_from_sixes}  # {total_runs}')
print(f'  balls = {balls}')
print(f'  strike_rate = ({total_runs} / {balls}) * 100  # {strike_rate}')

if fours_guess == "5" and sixes_guess == "2" and balls_guess == "18":
    print("Excellent reverse engineering!")
    score = score + 1
else:
    print("This was tricky! You had to work backwards from the output.")
    print("20 runs from fours means 5 fours (20/4=5)")
    print("12 runs from sixes means 2 sixes (12/6=2)")

print()
print("=" * 40)
print(f"YOUR SCORE: {score} / 3")
print("=" * 40)

# ============================================================
# REFLECTION PROMPTS:
# 1. Working BACKWARDS is harder than working forwards.
#    Why? What is different about the thinking?
# 2. In Round 3, how did you figure out the number of fours
#    from "20 runs"? What math did you do in your head?
# 3. Engineers reverse engineer products all the time.
#    Why would someone want to understand how something
#    was built by looking at the final product?
# ============================================================
