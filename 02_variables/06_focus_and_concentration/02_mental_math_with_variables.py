# Program Code: VAR-FC-02
# Title: Mental Math with Variables
# Cognitive Skill: Focus and Concentration (Mental tracking)
# Topic: Variables in Python

import time

score = 0

# Round 1 — 3 operations
print("--- Round 1 ---")
print("runs = 0")
time.sleep(2)
print("runs = runs + 6")
time.sleep(2)
print("runs = runs + 4")
time.sleep(2)
print("runs = runs + 3")

runs = 0
runs = runs + 6
runs = runs + 4
runs = runs + 3

guess = int(input("What is runs? "))
print("Answer:", runs)
if guess == runs:
    print("Correct!")
    score = score + 1
else:
    print("Trace: 0 -> 6 -> 10 ->", runs)

# Round 2 — 5 operations
print("--- Round 2 ---")
print("savings = 50")
time.sleep(2)
print("savings = savings + 20")
time.sleep(2)
print("savings = savings - 15")
time.sleep(2)
print("savings = savings + 20")
time.sleep(2)
print("savings = savings + 10")
time.sleep(2)
print("savings = savings - 25")

savings = 50
savings = savings + 20
savings = savings - 15
savings = savings + 20
savings = savings + 10
savings = savings - 25

guess = int(input("What is savings? "))
print("Answer:", savings)
if guess == savings:
    print("Correct!")
    score = score + 1
else:
    print("Trace: 50 -> 70 -> 55 -> 75 -> 85 ->", savings)

# Round 3 — 7 operations
print("--- Round 3 ---")
print("money = 100")
time.sleep(2)
print("money = money + 50")
time.sleep(2)
print("money = money + 50")
time.sleep(2)
print("money = money - 80")
time.sleep(2)
print("money = money + 30")
time.sleep(2)
print("money = money + 40")
time.sleep(2)
print("money = money - 60")
time.sleep(2)
print("money = money + 20")

money = 100
money = money + 50
money = money + 50
money = money - 80
money = money + 30
money = money + 40
money = money - 60
money = money + 20

guess = int(input("What is money? "))
print("Answer:", money)
if guess == money:
    print("Correct!")
    score = score + 1
else:
    print("Trace: 100->150->200->120->150->190->130->", money)

print("Score:", score, "/ 3")
