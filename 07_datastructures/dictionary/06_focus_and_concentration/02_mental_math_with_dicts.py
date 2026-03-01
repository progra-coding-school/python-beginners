# Mental Math with Dictionaries
# Work through each problem IN YOUR HEAD before reading the answer.
# Mental calculation with dicts trains both focus AND understanding of dict operations.
# Then run the code to verify — how many did you get right?

print("Mental Math with Dictionaries")
print()

# Q1: sum of all values
# Trace: 120 + 40 + 80 + 90 = ?
prices = {"mango": 120, "banana": 40, "apple": 80, "grapes": 90}
total  = sum(prices.values())
print("Q1: Sum of all prices =", total)
# Answer: 330

print()

# Q2: average — sum divided by count
# Trace: (85 + 92 + 78) / 3 = 255 / 3 = ?
marks   = {"Maths": 85, "Science": 92, "English": 78}
average = sum(marks.values()) / len(marks)
print("Q2: Average mark =", str(round(average, 1)))
# Answer: 85.0

print()

# Q3: update values, add a new key, then sum everything
# Trace: pens 50-20=30, books 30+10=40, erasers stays 80, rulers added=25
stock  = {"pens": 50, "books": 30, "erasers": 80}
stock["pens"]   -= 20   # 50 - 20 = 30
stock["books"]  += 10   # 30 + 10 = 40
stock["rulers"]  = 25   # new key added
total_items      = sum(stock.values())
print("Q3: Total items in stock after changes =", total_items)
# Answer: pens=30, books=40, erasers=80, rulers=25 → 175

print()

# Q4: count values matching a condition using a generator expression
# Trace: Diya=62 (>50 yes), Riya=55 (>50 yes), Aarav=45 (no), Karthik=38 (no)
team     = {"Aarav": 45, "Diya": 62, "Karthik": 38, "Riya": 55}
above_50 = sum(1 for runs in team.values() if runs > 50)
print("Q4: Players who scored more than 50 =", above_50)
# Answer: 2

print()

# Q5: frequency count — count occurrences of each item
# Trace: pen appears 3 times, book 2 times, eraser 1 time
# bag.get(item, 0) returns 0 on first occurrence so we never crash on a missing key
bag   = {}
items = ["pen", "pen", "book", "pen", "eraser", "book"]
for item in items:
    bag[item] = bag.get(item, 0) + 1
print("Q5: pen =", bag["pen"], " book =", bag["book"], " eraser =", bag["eraser"])
# Answer: pen=3, book=2, eraser=1

print()

# Q6: update overwrites existing keys, adds new ones — then sum
# Before: a=10, b=20, c=30.  After update: b changes 20→5, d=40 added.
# Sum: 10 + 5 + 30 + 40 = ?
d = {"a": 10, "b": 20, "c": 30}
d.update({"b": 5, "d": 40})    # b overwritten from 20 to 5; d is brand new
print("Q6: Sum of all values =", sum(d.values()))
# Answer: 85
