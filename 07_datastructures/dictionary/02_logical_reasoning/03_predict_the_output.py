# Program Code: DC-LR-03
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning
# Topic: Dictionaries in Python

# For each block, write your prediction on paper FIRST.
# Then uncomment the print statements and verify.

# --- Challenge 1 ---
print("=== Challenge 1 ===")
d = {"x": 10, "y": 20, "z": 30}
print(len(d))               # Predict: ?
print("y" in d)             # Predict: ?
print(d.get("w", -1))       # Predict: ?
# Answers: 3 | True | -1

print()

# --- Challenge 2 ---
print("=== Challenge 2 ===")
bag = {"apples": 5, "bananas": 3}
bag["apples"]  += 2         # add 2 more apples
bag["oranges"]  = 4         # new fruit
bag.pop("bananas")          # remove bananas
print(bag)
# Predict: ?
# Answer : {'apples': 7, 'oranges': 4}

print()

# --- Challenge 3 ---
print("=== Challenge 3 ===")
team = {"Aarav": 45, "Diya": 62, "Karthik": 38}
top  = max(team, key=team.get)
print(top)
# Predict: ?
# Answer : Diya  (62 is the highest)

print()

# --- Challenge 4 ---
print("=== Challenge 4 ===")
nested = {"school": {"name": "Progra", "city": "Chennai"}}
print(nested["school"]["city"])
print(nested.get("school", {}).get("pin", "No PIN"))
# Predict line 1: ?      line 2: ?
# Answer        : Chennai | No PIN

print()

# --- Challenge 5 — Tricky! ---
print("=== Challenge 5 ===")
count = {}
words = ["go", "stop", "go", "go", "stop"]
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print(sorted(count.items()))    # items sorted alphabetically
# Predict: ?
# Answer : [('go', 3), ('stop', 2)]

# Think:
# 1. In Challenge 3, what would happen if TWO students had the same highest score?
# 2. In Challenge 5, why does sorted() produce alphabetical order here?
