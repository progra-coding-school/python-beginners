# Mental Math with Sets
# Work through each problem IN YOUR HEAD first. Only run to check your answer.
# Mental set calculations train both focus AND understanding of set operations.

print("Mental Math with Sets")
print("Answer each question before running!")
print()

# --- Q1: Size after deduplication ---
# Think: list each unique value first, then count
raw = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print("Q1: len(set(raw)) =", len(set(raw)))
# Unique values are 1,2,3,4,5,6 → count?

print()

# --- Q2: Intersection size ---
# Think: which values appear in BOTH a and b?
a = {10, 20, 30, 40, 50}
b = {30, 40, 50, 60, 70}
print("Q2: len(a & b) =", len(a & b))

print()

# --- Q3: Union size ---
# Think: list all unique items from x AND y (each only once)
x = {"cat", "dog", "fish"}
y = {"dog", "bird", "fish", "hamster"}
print("Q3: len(x | y) =", len(x | y))
# Hint: cat + dog + fish + bird + hamster = ? unique items

print()

# --- Q4: Difference ---
# Think: who is in students_a but NOT in students_b?
students_a = {"Aarav", "Diya", "Karthik", "Riya"}
students_b = {"Diya", "Riya", "Ananya"}
diff = students_a - students_b
print("Q4: students_a - students_b =", sorted(diff))

print()

# --- Q5: Is it a subset? ---
# Think: can ALL of p fit inside q? Can ALL of q fit inside p?
p = {1, 2}
q = {1, 2, 3, 4}
print("Q5: p.issubset(q) =", p.issubset(q))
print("    q.issubset(p) =", q.issubset(p))

print()

# --- Q6: Symmetric difference ---
# Think: items in m OR n but NOT in both → which numbers are excluded from the middle?
m = {1, 2, 3, 4}
n = {3, 4, 5, 6}
print("Q6: m ^ n =", m ^ n)

print()

# --- Q7: Chained operations ---
# Think: list all unique names from all three teams first, then count
team1 = {"Aarav", "Diya", "Karthik"}
team2 = {"Diya", "Riya"}
team3 = {"Karthik", "Vivek"}
all_players = team1 | team2 | team3
print("Q7: Total unique players across 3 teams =", len(all_players))

# Think:
# 1. In Q3, why isn't the answer 3 + 4 = 7?
# 2. In Q6, which operator gives BOTH sides minus the overlap?
