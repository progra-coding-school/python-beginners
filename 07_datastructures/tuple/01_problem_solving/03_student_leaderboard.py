# Program Code: TU-PS-03
# Title: Student Leaderboard Using Tuples
# Cognitive Skill: Problem Solving
# Topic: Tuples in Python

# Problem:
# Build a leaderboard for a class quiz.
# Each entry is a record: (rank, name, score).
# Tasks: sort by score, assign ranks, find top 3, handle ties.

# --- Raw scores ---
quiz_scores = [
    ("Aarav",   85),
    ("Diya",    92),
    ("Karthik", 78),
    ("Riya",    92),     # tie with Diya!
    ("Ananya",  88),
    ("Vivek",   78),     # tie with Karthik!
    ("Priya",   95),
]

print("=== Quiz Leaderboard ===")
print()

# --- Step 1: Sort by score descending, then by name alphabetically (for ties) ---
sorted_scores = sorted(quiz_scores, key=lambda s: (-s[1], s[0]))

# --- Step 2: Assign ranks (ties get same rank) ---
leaderboard = []
rank = 1
for i, (name, score) in enumerate(sorted_scores):
    if i > 0 and score < sorted_scores[i-1][1]:
        rank = i + 1    # new rank only if score is lower than previous
    leaderboard.append((rank, name, score))

# --- Step 3: Display leaderboard ---
print(f"  {'Rank':>4}  {'Name':<12} {'Score':>5}")
print(f"  {'─'*4}  {'─'*12} {'─'*5}")
for rank, name, score in leaderboard:
    medal = " 🥇" if rank == 1 else (" 🥈" if rank == 2 else (" 🥉" if rank == 3 else ""))
    print(f"  #{rank:<3}  {name:<12} {score:>5}{medal}")

print()

# --- Step 4: Top 3 students ---
print("=== Top 3 ===")
top3 = [entry for entry in leaderboard if entry[0] <= 3]
for rank, name, score in top3:
    print(f"  Rank {rank}: {name} — {score} marks")

print()

# --- Step 5: Class statistics ---
all_scores = [s for _, s in quiz_scores]
print("=== Class Statistics ===")
print(f"  Highest : {max(all_scores)}")
print(f"  Lowest  : {min(all_scores)}")
print(f"  Average : {sum(all_scores)/len(all_scores):.1f}")
print(f"  Above avg: {sum(1 for s in all_scores if s > sum(all_scores)/len(all_scores))} students")

# Think:
# 1. Why did we sort by (-score, name) — what does the negative sign do?
# 2. How would you change the leaderboard to show the BOTTOM 3 instead of the top 3?
