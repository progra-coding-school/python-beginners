# Trace the Dictionary
# Read each code block carefully. PREDICT the output before looking at the answer.
# Tracing code step by step builds the mental model that makes debugging easy.
# Work through each trace on paper — then run to confirm.

# Trace 1: update + add + delete
# Step by step: b updated from 2→20, d=4 added (new key), a deleted entirely
print("Trace 1:")
d = {"a": 1, "b": 2, "c": 3}
d["b"] = 20      # key "b" already exists → value changes from 2 to 20
d["d"] = 4       # key "d" is new → gets added at the end
del d["a"]       # key "a" is deleted — gone completely
print(d)
# Predicted output? → {'b': 20, 'c': 3, 'd': 4}

print()

# Trace 2: .update() merges and overwrites
# Diya's score changes 90→95 (existing key updated); Karthik is new (key added)
print("Trace 2:")
scores = {"Aarav": 85, "Diya": 90}
scores.update({"Diya": 95, "Karthik": 78})   # Diya overwritten, Karthik added
print(scores)
# Predicted? → {'Aarav': 85, 'Diya': 95, 'Karthik': 78}

print()

# Trace 3: .pop() removes AND returns the value
# val gets the removed value (12); the key "age" disappears from the dict
print("Trace 3:")
info = {"name": "Riya", "age": 12}
val  = info.pop("age")      # removes "age", stores 12 in val
print("Popped:", val)
print("Dict now:", info)
# Predicted popped: 12    Dict: {'name': 'Riya'}

print()

# Trace 4: loop with condition — only add prices UNDER Rs.100
# mango (120) is above 100 → skipped. banana (40) + apple (80) = 120
print("Trace 4:")
prices = {"mango": 120, "banana": 40, "apple": 80}
total  = 0
for item, cost in prices.items():
    if cost < 100:
        total += cost
print("Total of items under Rs.100:", total)
# Predicted? → 120  (banana 40 + apple 80)

print()

# Trace 5: building a frequency dict using .get()
# .get(item, 0) returns current count or 0 if first time seeing the item
# pen appears 3 times, book 2 times, eraser 1 time
print("Trace 5:")
bag   = {}
items = ["pen", "book", "pen", "eraser", "book", "pen"]
for item in items:
    bag[item] = bag.get(item, 0) + 1   # get current count (0 if new), add 1
print(bag)
# Predicted? → {'pen': 3, 'book': 2, 'eraser': 1}
