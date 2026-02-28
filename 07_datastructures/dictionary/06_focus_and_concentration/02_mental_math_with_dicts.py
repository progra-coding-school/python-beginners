# Program Code: DC-FC-02
# Title: Mental Math with Dictionaries
# Cognitive Skill: Focus and Concentration
# Topic: Dictionaries in Python

# Work through each problem IN YOUR HEAD first.
# Only run the code to check your answer.

print("=== Mental Math with Dictionaries ===")
print("Try to answer each question before running!\n")

# --- Question 1 ---
prices = {"mango": 120, "banana": 40, "apple": 80, "grapes": 90}
total  = sum(prices.values())
print(f"Q1: Sum of all prices = {total}")
# Think: 120 + 40 + 80 + 90 = ?

print()

# --- Question 2 ---
marks    = {"Maths": 85, "Science": 92, "English": 78}
average  = sum(marks.values()) / len(marks)
print(f"Q2: Average mark = {average:.1f}")
# Think: (85 + 92 + 78) / 3 = ?

print()

# --- Question 3 ---
stock  = {"pens": 50, "books": 30, "erasers": 80}
stock["pens"]   -= 20
stock["books"]  += 10
stock["rulers"]  = 25
total_items      = sum(stock.values())
print(f"Q3: Total items in stock after changes = {total_items}")
# Think: pens=30, books=40, erasers=80, rulers=25 → total?

print()

# --- Question 4 ---
team = {"Aarav": 45, "Diya": 62, "Karthik": 38, "Riya": 55}
above_50 = sum(1 for runs in team.values() if runs > 50)
print(f"Q4: Players who scored more than 50 = {above_50}")
# Think: Diya (62), Riya (55) → count?

print()

# --- Question 5 ---
bag   = {}
items = ["pen", "pen", "book", "pen", "eraser", "book"]
for item in items:
    bag[item] = bag.get(item, 0) + 1
print(f"Q5: pen count = {bag['pen']},  book count = {bag['book']},  eraser = {bag['eraser']}")
# Think: pen appears 3 times, book 2 times, eraser 1 time

print()

# --- Question 6 (trickiest!) ---
d = {"a": 10, "b": 20, "c": 30}
d.update({"b": 5, "d": 40})
print(f"Q6: Sum of all values = {sum(d.values())}")
# Think: after update → a=10, b=5 (overwritten), c=30, d=40 → total?

# Think:
# 1. In Q3, what is the new "pens" value after subtracting 20?
# 2. In Q6, why is b=5 and not 20? What happened to the old value?
