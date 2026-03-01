# Program Code: LIST-LR-01
# Title: Trace the List
# Cognitive Skill: Logical Reasoning (Tracing step-by-step)
# Topic: Lists in Python

score = 0
total = 5

print("=== Trace the List ===")
print("After each series of operations, type what the list looks like.")
print()

def check(user_input, actual):
    try:
        parsed = eval(user_input)
        return parsed == actual
    except Exception:
        user_clean = user_input.replace(" ", "").lower()
        actual_clean = str(actual).replace(" ", "").lower()
        return user_clean == actual_clean

# --- Round 1 ---
print("Round 1:")
print("  snacks = ['chips', 'mango', 'biscuit']")
print("  snacks.append('chocolate')")
print("  snacks.remove('mango')")
ans = input("  Final list? ").strip()
snacks = ["chips", "mango", "biscuit"]
snacks.append("chocolate")
snacks.remove("mango")
if check(ans, snacks):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", snacks)
print()

# --- Round 2 ---
print("Round 2:")
print("  team = ['Aarav', 'Kabir', 'Diya']")
print("  team.insert(1, 'Riya')")
print("  team.pop()")
ans = input("  Final list? ").strip()
team = ["Aarav", "Kabir", "Diya"]
team.insert(1, "Riya")
team.pop()
if check(ans, team):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", team)
print()

# --- Round 3 ---
print("Round 3:")
print("  marks = [78, 45, 92, 60]")
print("  marks.sort()")
print("  marks.append(55)")
ans = input("  Final list? ").strip()
marks = [78, 45, 92, 60]
marks.sort()
marks.append(55)
if check(ans, marks):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", marks)
print()

# --- Round 4 ---
print("Round 4:")
print("  cart = ['rice', 'dal', 'oil']")
print("  cart.append('sugar')")
print("  cart.insert(0, 'salt')")
print("  cart.remove('oil')")
print("  cart.append('ghee')")
ans = input("  Final list? ").strip()
cart = ["rice", "dal", "oil"]
cart.append("sugar")
cart.insert(0, "salt")
cart.remove("oil")
cart.append("ghee")
if check(ans, cart):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", cart)
print()

# --- Round 5 (Boss) ---
print("Round 5 (Boss Round):")
print("  scores = [34, 12, 56]")
print("  scores.extend([20, 45])")
print("  scores.reverse()")
print("  scores.pop(2)")
ans = input("  Final list? ").strip()
scores = [34, 12, 56]
scores.extend([20, 45])
scores.reverse()
scores.pop(2)
if check(ans, scores):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", scores)
print()

print("Score:", score, "/", total)
