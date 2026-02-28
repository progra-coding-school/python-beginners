# Program Code: CL-PS-03
# Title: Cricket Player Stats Tracker
# Cognitive Skill: Problem Solving
# Topic: Classes and Objects in Python

# Problem:
# Build a CricketPlayer class that tracks:
# batting runs, bowling wickets, catches — across multiple matches.

class CricketPlayer:
    def __init__(self, name, role):
        self.name     = name
        self.role     = role        # "batsman", "bowler", "all-rounder"
        self.matches  = 0
        self.runs     = []
        self.wickets  = []
        self.catches  = 0

    def play_match(self, runs_scored, wickets_taken=0, catches_taken=0):
        self.matches         += 1
        self.runs.append(runs_scored)
        self.wickets.append(wickets_taken)
        self.catches         += catches_taken
        print(f"  {self.name}: Match {self.matches} — "
              f"{runs_scored} runs, {wickets_taken} wkts, {catches_taken} catches")

    def batting_average(self):
        if not self.runs:
            return 0
        return sum(self.runs) / len(self.runs)

    def bowling_average(self):
        total_wickets = sum(self.wickets)
        if total_wickets == 0:
            return None
        return total_wickets / self.matches

    def highest_score(self):
        return max(self.runs) if self.runs else 0

    def total_wickets(self):
        return sum(self.wickets)

    def report(self):
        print(f"\n  {'─'*35}")
        print(f"  Player  : {self.name}  ({self.role})")
        print(f"  Matches : {self.matches}")
        print(f"  Runs    : {self.runs}  → Total: {sum(self.runs)}")
        print(f"  Bat Avg : {self.batting_average():.1f}")
        print(f"  Hi Score: {self.highest_score()}")
        print(f"  Wickets : {self.wickets}  → Total: {self.total_wickets()}")
        if self.bowling_average():
            print(f"  Wkt/Match: {self.bowling_average():.1f}")
        print(f"  Catches : {self.catches}")
        print(f"  {'─'*35}")

# --- Demo ---
print("=== Cricket Team Stats ===\n")

aarav   = CricketPlayer("Aarav",   "batsman")
karthik = CricketPlayer("Karthik", "bowler")
diya    = CricketPlayer("Diya",    "all-rounder")

# Match 1
aarav.play_match(45, catches_taken=1)
karthik.play_match(5, wickets_taken=3)
diya.play_match(38, wickets_taken=1, catches_taken=2)

# Match 2
aarav.play_match(62)
karthik.play_match(0, wickets_taken=4)
diya.play_match(55, wickets_taken=2)

# Match 3
aarav.play_match(18, catches_taken=2)
karthik.play_match(12, wickets_taken=2)
diya.play_match(70, wickets_taken=0, catches_taken=1)

# Reports
for player in [aarav, karthik, diya]:
    player.report()

# Best batsman
team = [aarav, karthik, diya]
best = max(team, key=lambda p: p.batting_average())
print(f"\nBest batsman: {best.name} (avg {best.batting_average():.1f})")

# Think:
# 1. How would you add a method that returns all matches where the player scored 50+?
# 2. Why store runs and wickets as lists rather than just totals?
