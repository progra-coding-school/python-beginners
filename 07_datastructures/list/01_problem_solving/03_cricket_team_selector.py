# Program Code: LIST-PS-03
# Title: Cricket Team Selector — Pick the Playing 11!
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Lists in Python

# ======================================================
# WHAT PROBLEM ARE WE SOLVING?
# ======================================================
# Coach Rahul has 15 players for the school cricket match.
# Only 11 can play — these are the "Playing 11".
# The remaining 4 sit on the bench as substitutes.
#
# Coach needs to:
#   - Rank all 15 players by their performance score
#   - Pick the TOP 11 as the playing squad
#   - Show who is on the bench
#   - (BONUS) Allow swapping a bench player with a playing player
#
# WHY USE LISTS?
# We have player names AND scores together — we need to
# SORT them as a unit. Lists of pairs let us keep
# a player's name and score linked during sorting.
# ======================================================

# ======================================================
# DECOMPOSE THE PROBLEM
# ======================================================
# Break the big problem into small, clear steps:
#
# Step 1: Store 15 player names and their performance scores
# Step 2: Combine each player's name + score into a pair [score, name]
# Step 3: Sort the pairs by score in descending order (highest first)
# Step 4: The top 11 pairs → Playing 11
# Step 5: The remaining 4 pairs → Bench players
# Step 6: Print the Playing 11 with rank numbers and scores
# Step 7: Print the bench players
#
# BONUS: Let Coach swap one bench player in for a playing 11 player
# ======================================================


print("=" * 55)
print("   Cricket Team Selector — Pick the Playing 11!")
print("=" * 55)
print("\nCoach Rahul's School Cricket Tournament Selection")


# --------------------------------------------------
# STEP 1: Store 15 player names and their scores
# --------------------------------------------------
# Performance score is out of 100
# These are school players inspired by Indian cricket legends!

players = [
    "Rohit", "Virat",  "Dhoni",  "Bumrah", "Jadeja",
    "Ashwin", "Rahul",  "Pant",   "Shami",  "Siraj",
    "Hardik", "Ishan",  "Axar",   "Shardul", "Gill"
]

scores = [
    91,  95,  88,  85,  79,
    83,  76,  90,  72,  68,
    87,  80,  74,  70,  93
]

print("\nStep 1: All 15 players and their performance scores")
print("-" * 40)
print(f"{'Player':<12} {'Score':>6}")
print("-" * 20)

for i in range(len(players)):
    print(f"{players[i]:<12} {scores[i]:>6}")

print("-" * 20)
print(f"Total players registered: {len(players)}")


# --------------------------------------------------
# STEP 2: Combine players + scores into pairs
# --------------------------------------------------
# We create a list where each item is [score, player_name]
# Putting score FIRST lets Python sort by score automatically

player_pairs = []

for i in range(len(players)):
    pair = [scores[i], players[i]]   # [score, name]
    player_pairs.append(pair)

print("\nStep 2: Combined into score-name pairs")
print("-" * 40)
print("Format: [score, name]")
print(player_pairs)


# --------------------------------------------------
# STEP 3: Sort by score — highest first
# --------------------------------------------------
# sort() rearranges the list IN PLACE
# By default it sorts the first element in each pair (the score)
# reverse=True → highest score comes first (Rank 1)

player_pairs.sort(reverse=True)

print("\nStep 3: Sorted by score (highest → lowest)")
print("-" * 40)
print("After sorting:")
for pair in player_pairs:
    print(f"  Score: {pair[0]}  |  Player: {pair[1]}")


# --------------------------------------------------
# STEP 4: Pick the top 11 — the Playing 11
# --------------------------------------------------
# List slicing: player_pairs[0:11] gives us items at index 0 to 10
# That is the first 11 items = the top 11 scorers

playing_11 = player_pairs[0:11]   # indices 0, 1, 2, ... 10


# --------------------------------------------------
# STEP 5: Remaining 4 are the bench players
# --------------------------------------------------
# List slicing: player_pairs[11:] gives us items from index 11 onward

bench = player_pairs[11:]         # indices 11, 12, 13, 14


# --------------------------------------------------
# STEP 6: Print the Playing 11
# --------------------------------------------------

print()
print("=" * 55)
print("        COACH RAHUL'S PLAYING 11 — SELECTED!")
print("=" * 55)
print(f"{'Rank':<6} {'Player':<14} {'Score':>6}  {'Role'}")
print("-" * 45)

for rank, pair in enumerate(playing_11, start=1):
    score  = pair[0]
    player = pair[1]

    # Add captain label to Rank 1 (the highest scorer leads!)
    if rank == 1:
        role = "Captain"
    elif rank == 2:
        role = "Vice Captain"
    else:
        role = "Player"

    print(f"{rank:<6} {player:<14} {score:>6}  {role}")

print("=" * 55)


# --------------------------------------------------
# STEP 7: Print the bench players
# --------------------------------------------------

print()
print("=" * 55)
print("        BENCH PLAYERS (Substitutes)")
print("=" * 55)
print(f"{'Bench #':<10} {'Player':<14} {'Score':>6}")
print("-" * 35)

for bench_num, pair in enumerate(bench, start=1):
    score  = pair[0]
    player = pair[1]
    print(f"{bench_num:<10} {player:<14} {score:>6}")

print("=" * 55)
print("\nBest of luck to the team! Go school cricket! \U0001f3cf")


# --------------------------------------------------
# BONUS: Let Coach swap a bench player in
# --------------------------------------------------
# The coach can pick one bench player and one playing 11 player
# and swap their positions — just like real team management!

print()
print("=" * 55)
print("   BONUS: Coach's Player Swap Tool")
print("=" * 55)

# Show bench options for the coach to choose from
print("\nBench players available for swap:")
for i, pair in enumerate(bench, start=1):
    print(f"  {i}. {pair[1]} (Score: {pair[0]})")

# Show playing 11 options the coach can replace
print("\nPlaying 11 — who do you want to replace?")
for i, pair in enumerate(playing_11, start=1):
    print(f"  {i}. {pair[1]} (Score: {pair[0]})")

print()

# Coach makes their choices (hardcoded for demo — try changing these!)
# Coach wants to bring in bench player 1 and replace playing 11 player 9
bench_choice   = 1   # bench player number (1-4)
playing_choice = 9   # playing 11 player number (1-11)

# Convert to 0-based index for list access
bench_index   = bench_choice - 1
playing_index = playing_choice - 1

# Save the names for the announcement
incoming_player = bench[bench_index][1]
outgoing_player = playing_11[playing_index][1]

# Perform the swap
bench[bench_index], playing_11[playing_index] = (
    playing_11[playing_index], bench[bench_index]
)

print(f"SWAP MADE:")
print(f"  OUT: {outgoing_player} (moves to bench)")
print(f"  IN : {incoming_player} (joins Playing 11)")

# Show the updated Playing 11 after the swap
print()
print("=" * 55)
print("   UPDATED PLAYING 11 (After Swap)")
print("=" * 55)
print(f"{'Rank':<6} {'Player':<14} {'Score':>6}")
print("-" * 30)

for rank, pair in enumerate(playing_11, start=1):
    # Highlight the newly added player
    tag = "  <-- NEW" if pair[1] == incoming_player else ""
    print(f"{rank:<6} {pair[1]:<14} {pair[0]:>6}{tag}")

print("=" * 55)
print("\nFinal squad locked in. Match day is here — let's go!")


# ======================================================
# REFLECTION — Think and Answer
# ======================================================
# 1. Why do we put score FIRST in each pair [score, name]
#    instead of [name, score]? What would happen if we
#    put the name first and tried to sort?
#
# 2. What does player_pairs[0:11] mean? What is list slicing?
#    Try changing the numbers — what does player_pairs[2:5] give?
#
# 3. In the BONUS swap, we used a simultaneous swap:
#    a, b = b, a
#    Why is this safer than using a temporary variable?
#    Try writing the swap the long way using a temp variable.
#
# 4. Right now the captain is just the top scorer.
#    Can you think of a better real-life way to pick a captain?
#    How would you change the code to support that?
# ======================================================
