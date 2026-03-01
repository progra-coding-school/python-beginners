# Trace the List
# A list changes every time an operation runs.
# This exercise trains you to TRACE — follow each step in your head
# and predict exactly what the list looks like after each operation.
# Type your answer as a Python list, e.g. ['a', 'b'] or [1, 2, 3]

score = 0
total = 5

# check() compares the student's answer to the actual list result
# It uses eval() to parse typed text like "[1, 2, 3]" into a real Python list
def check(user_input, actual):
    try:
        parsed = eval(user_input)
        return parsed == actual
    except Exception:
        # fallback: compare as strings with spaces removed
        user_clean = user_input.replace(" ", "").lower()
        actual_clean = str(actual).replace(" ", "").lower()
        return user_clean == actual_clean

# --- Round 1: append + remove ---
# append adds to the end; remove deletes the first matching value
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

# --- Round 2: insert + pop ---
# insert(1, x) pushes everything from index 1 rightward; pop() removes the last item
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

# --- Round 3: sort + append ---
# sort() rearranges in place first, THEN append adds to the end of the sorted list
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

# --- Round 4: append + insert + remove + append (four steps!) ---
# Trace each step carefully — the list changes after every line
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

# --- Round 5 (Boss): extend + reverse + pop(2) ---
# extend adds multiple items; reverse flips the whole list; pop(2) removes index 2
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
