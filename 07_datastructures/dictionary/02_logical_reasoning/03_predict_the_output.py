# Predict the Output
# Before you run any of these blocks, write your prediction on paper.
# Then run the code and check — were you right?
# Being able to predict output without running code shows deep understanding.

# Challenge 1: len, 'in', .get() with default
# len counts pairs; 'in' checks keys; .get() returns default for missing keys
print("Challenge 1:")
d = {"x": 10, "y": 20, "z": 30}
print(len(d))               # Predict: 3    (three key-value pairs)
print("y" in d)             # Predict: True  ("y" is a key)
print(d.get("w", -1))       # Predict: -1   ("w" not in dict → return default -1)

print()

# Challenge 2: modify values, add new key, remove key
# apples: 5 + 2 = 7. oranges = 4 (new key added). bananas removed by pop.
print("Challenge 2:")
bag = {"apples": 5, "bananas": 3}
bag["apples"]  += 2         # 5 + 2 = 7
bag["oranges"]  = 4         # new key added
bag.pop("bananas")          # bananas removed entirely
print(bag)
# Predict: {'apples': 7, 'oranges': 4}

print()

# Challenge 3: max() with key=dict.get
# max(team, key=team.get) → finds the key (player name) whose value (score) is highest
# Aarav=45, Diya=62, Karthik=38 → Diya wins
print("Challenge 3:")
team = {"Aarav": 45, "Diya": 62, "Karthik": 38}
top  = max(team, key=team.get)
print(top)
# Predict: Diya

print()

# Challenge 4: nested dict access + chained .get()
# line 1: nested["school"]["city"] → go two levels deep → "Chennai"
# line 2: .get("school", {}) finds school OK, but .get("pin", "No PIN") → not found
print("Challenge 4:")
nested = {"school": {"name": "Progra", "city": "Chennai"}}
print(nested["school"]["city"])
print(nested.get("school", {}).get("pin", "No PIN"))
# Predict line 1: Chennai    line 2: No PIN

print()

# Challenge 5: frequency count, then sorted .items()
# After counting: go=3, stop=2
# sorted() on a list of tuples → sorts alphabetically by the first element (the key)
print("Challenge 5:")
count = {}
words = ["go", "stop", "go", "go", "stop"]
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print(sorted(count.items()))    # sorted tuples → alphabetical by key name
# Predict: [('go', 3), ('stop', 2)]
