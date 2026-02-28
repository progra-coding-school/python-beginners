# Program Code: DC-FC-01
# Title: Spot the Difference
# Cognitive Skill: Focus and Concentration
# Topic: Dictionaries in Python

# Two versions of similar code are shown side by side (as separate blocks).
# Find every difference — some are bugs, some are just style choices.

# ─── Pair 1 ─────────────────────────────────────────────────────
print("=== Pair 1 ===")

# Version A
a = {"name": "Aarav", "age": 13}
print(a.get("name"))        # Aarav

# Version B
b = {"Name": "Aarav", "age": 13}
print(b.get("name"))        # None  ← different!
# Difference: key is "Name" (capital N) in B. .get("name") returns None.

print()

# ─── Pair 2 ─────────────────────────────────────────────────────
print("=== Pair 2 ===")

# Version A
scores_a = {"Aarav": 85, "Diya": 90}
scores_a["Karthik"] = 78
print(len(scores_a))        # 3

# Version B
scores_b = {"Aarav": 85, "Diya": 90}
scores_b.update({"Diya": 78})
print(len(scores_b))        # 2  ← different!
# Difference: A adds a new key (Karthik), B updates an existing key (Diya). Length differs.

print()

# ─── Pair 3 ─────────────────────────────────────────────────────
print("=== Pair 3 ===")

# Version A — safe loop
data_a = {"x": 1, "y": 2, "z": 3}
for k in list(data_a.keys()):
    if data_a[k] < 2:
        del data_a[k]
print("A:", data_a)    # {'y': 2, 'z': 3}

# Version B — may raise RuntimeError
data_b = {"x": 1, "y": 2, "z": 3}
try:
    for k in data_b.keys():   # looping directly — dangerous
        if data_b[k] < 2:
            del data_b[k]
    print("B:", data_b)
except RuntimeError as e:
    print("B: RuntimeError —", e)
# Difference: A wraps keys in list() (safe snapshot); B loops directly (risky).

print()

# ─── Pair 4 ─────────────────────────────────────────────────────
print("=== Pair 4 ===")

menu_a = {"idli": 15, "dosa": 30}
print(menu_a["chai"] if "chai" in menu_a else "Not available")   # Not available

menu_b = {"idli": 15, "dosa": 30}
print(menu_b.get("chai", "Not available"))                        # Not available
# Difference: Different syntax, same result. B is shorter and more Pythonic.

# Think:
# 1. In Pair 1, how would you fix Version B so it behaves like Version A?
# 2. In Pair 3, which version would you always use? Why?
