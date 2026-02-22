# Program Code: VAR-ST-01
# Title: Amma's Chai Stall Calculator
# Cognitive Skill: Structured Thinking (Plan first, then code)
# Topic: Variables in Python

# PLAN BEFORE CODING:
# Category 1 — Prices: chai_price, samosa_price, biscuit_price
# Category 2 — Quantities: chai_qty, samosa_qty, biscuit_qty
# Category 3 — Totals: chai_total, samosa_total, biscuit_total
# Category 4 — Final: bill_total

# Prices
chai_price = 10
samosa_price = 15
biscuit_price = 5

print("Menu — Chai:", chai_price, " Samosa:", samosa_price, " Biscuit:", biscuit_price)

# Quantities
chai_qty = int(input("How many Chai? "))
samosa_qty = int(input("How many Samosa? "))
biscuit_qty = int(input("How many Biscuit? "))

# Totals
chai_total = chai_price * chai_qty
samosa_total = samosa_price * samosa_qty
biscuit_total = biscuit_price * biscuit_qty

# Final bill
bill_total = chai_total + samosa_total + biscuit_total

print("Chai:", chai_total)
print("Samosa:", samosa_total)
print("Biscuit:", biscuit_total)
print("Total:", bill_total)
print("Thank you!")

# Think:
# 1. Did planning the variables first make coding easier?
# 2. Amma wants to add Vada (Rs.12). What new variables do you need?
#    Write the plan first, then add the code.
