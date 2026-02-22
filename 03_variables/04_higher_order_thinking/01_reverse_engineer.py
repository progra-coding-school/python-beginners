# Program Code: VAR-HOT-01
# Title: Reverse Engineer — Decode the Output
# Cognitive Skill: Higher Order Thinking (Working backwards)
# Topic: Variables in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("Output was:")
print("  Hello, my name is Diya")
print("  I am 10 years old")
name_guess = input("Value of 'name'? ")
age_guess = input("Value of 'age'? ")
name = "Diya"
age = 10
print("name =", name, "  age =", age)
if name_guess == "Diya" and age_guess == "10":
    print("Correct!")
    score = score + 1
else:
    print("Answer: name = Diya, age = 10")
input("Press Enter for Round 2...")

# Round 2
print("--- Round 2 ---")
print("Output was:")
print("  Item: Samosa")
print("  Price: 15")
print("  Quantity: 4")
print("  Total: 60")
item_guess = input("Value of 'item'? ")
price_guess = input("Value of 'price'? ")
qty_guess = input("Value of 'quantity'? ")
total_guess = input("Value of 'total'? ")
item = "Samosa"
price = 15
quantity = 4
total = price * quantity
print("item =", item, " price =", price, " quantity =", quantity, " total =", total)
if item_guess == "Samosa" and price_guess == "15" and qty_guess == "4" and total_guess == "60":
    print("Correct!")
    score = score + 1
else:
    print("total = price * quantity =", price, "*", quantity, "=", total)
input("Press Enter for Round 3...")

# Round 3
print("--- Round 3 (Challenge) ---")
print("Output was:")
print("  Player: Aarav")
print("  Fours: 5 (20 runs)")
print("  Sixes: 2 (12 runs)")
print("  Total: 32 runs")
print("  Balls: 18   Strike rate: 177.78")
fours_guess = input("How many fours? ")
sixes_guess = input("How many sixes? ")
balls_guess = input("How many balls? ")
fours = 5
sixes = 2
balls = 18
total_runs = fours * 4 + sixes * 6
strike_rate = round((total_runs / balls) * 100, 2)
print("fours =", fours, " sixes =", sixes, " balls =", balls)
print("total =", total_runs, " strike rate =", strike_rate)
if fours_guess == "5" and sixes_guess == "2" and balls_guess == "18":
    print("Correct!")
    score = score + 1
else:
    print("20 runs from fours = 5 fours (20/4). 12 runs from sixes = 2 sixes (12/6).")

print("Score:", score, "/ 3")
