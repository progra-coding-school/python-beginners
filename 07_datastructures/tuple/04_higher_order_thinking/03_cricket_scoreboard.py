# Program Code: TU-HOT-03
# Title: Cricket Scoreboard with Tuples
# Cognitive Skill: Higher Order Thinking
# Topic: Tuples in Python

# Design challenge:
# Use tuples to model a cricket match.
# Each ball is a record: (over, ball, batsman, runs, event)
# Events: 'dot', 'run', 'four', 'six', 'wicket', 'wide'

# --- Ball-by-ball data ---
# Format: (over, ball, batsman, runs, event)
balls = (
    (1, 1, "Aarav",   0, "dot"),
    (1, 2, "Aarav",   4, "four"),
    (1, 3, "Aarav",   1, "run"),
    (1, 4, "Diya",    6, "six"),
    (1, 5, "Diya",    0, "dot"),
    (1, 6, "Diya",    0, "wicket"),
    (2, 1, "Karthik", 2, "run"),
    (2, 2, "Karthik", 0, "wide"),
    (2, 3, "Karthik", 4, "four"),
    (2, 4, "Karthik", 6, "six"),
    (2, 5, "Karthik", 1, "run"),
    (2, 6, "Riya",    0, "dot"),
)

print("=== Ball-by-Ball Scorecard ===")
print(f"  {'Over':>4} {'Ball':>4} {'Batsman':<12} {'Runs':>5} {'Event':<10}")
print(f"  {'─'*4} {'─'*4} {'─'*12} {'─'*5} {'─'*10}")
for over, ball, batsman, runs, event in balls:
    print(f"  {over:>4}.{ball:<4} {batsman:<12} {runs:>5} {event:<10}")

print()

# --- Total team score ---
total_runs = sum(b[3] for b in balls if b[4] != "wide") + \
             sum(1 for b in balls if b[4] == "wide")   # wides add 1 extra run
wickets    = sum(1 for b in balls if b[4] == "wicket")
print(f"Total: {total_runs}/{wickets}")

print()

# --- Per-batsman stats ---
print("=== Batsman Scores ===")
batsmen = set(b[2] for b in balls)
for name in sorted(batsmen):
    player_balls = [b for b in balls if b[2] == name]
    player_runs  = sum(b[3] for b in player_balls)
    fours        = sum(1 for b in player_balls if b[4] == "four")
    sixes        = sum(1 for b in player_balls if b[4] == "six")
    out          = any(b[4] == "wicket" for b in player_balls)
    status       = "out" if out else "not out"
    print(f"  {name:<12} {player_runs:>3} runs ({fours} fours, {sixes} sixes) — {status}")

print()

# --- Highlight: biggest shots ---
print("=== Sixes Hit ===")
for over, ball, batsman, runs, event in balls:
    if event == "six":
        print(f"  Over {over}.{ball}: {batsman} hits a SIX!")

# Think:
# 1. Why did we use a tuple of tuples rather than a list of lists for `balls`?
# 2. How would you calculate the run rate (runs per over)?
