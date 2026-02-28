# Program Code: SE-FC-02
# Title: Mental Math with Sets
# Cognitive Skill: Focus and Concentration
# Topic: Sets in Python

# Work through each problem IN YOUR HEAD first.
# Only run to check your answer.

print("=== Mental Math with Sets ===")
print("Answer each question before running!\n")

# --- Q1: Size after deduplication ---
raw = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print(f"Q1: len(set({raw})) = {len(set(raw))}")
# Think: unique values are 1,2,3,4,5,6 → count?

print()

# --- Q2: Intersection size ---
a = {10, 20, 30, 40, 50}
b = {30, 40, 50, 60, 70}
print(f"Q2: len(a & b) = {len(a & b)}")
# Think: which values appear in both a and b?

print()

# --- Q3: Union size ---
x = {"cat", "dog", "fish"}
y = {"dog", "bird", "fish", "hamster"}
print(f"Q3: len(x | y) = {len(x | y)}")
# Think: cat + dog + fish + bird + hamster = ? unique items

print()

# --- Q4: Difference ---
students_a = {"Aarav", "Diya", "Karthik", "Riya"}
students_b = {"Diya", "Riya", "Ananya"}
diff = students_a - students_b
print(f"Q4: students_a - students_b = {sorted(diff)}")
# Think: who is in a but NOT in b?

print()

# --- Q5: Is it a subset? ---
p = {1, 2}
q = {1, 2, 3, 4}
print(f"Q5: p.issubset(q) = {p.issubset(q)}")
print(f"    q.issubset(p) = {q.issubset(p)}")
# Think: can all of p fit inside q?  Can all of q fit inside p?

print()

# --- Q6: Symmetric difference ---
m = {1, 2, 3, 4}
n = {3, 4, 5, 6}
print(f"Q6: m ^ n = {m ^ n}")
# Think: items in m or n but NOT in both → which numbers?

print()

# --- Q7: Chained operations ---
team1 = {"Aarav", "Diya", "Karthik"}
team2 = {"Diya", "Riya"}
team3 = {"Karthik", "Vivek"}
all_players = team1 | team2 | team3
print(f"Q7: Total unique players across 3 teams = {len(all_players)}")
# Think: list all unique names first, then count.

# Think:
# 1. In Q3, why isn't the answer 3 + 4 = 7?
# 2. In Q6, which operator gives BOTH sides minus the overlap?
