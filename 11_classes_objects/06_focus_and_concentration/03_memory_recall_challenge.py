# Program Code: CL-FC-03
# Title: Memory Recall Challenge
# Cognitive Skill: Focus and Concentration
# Topic: Classes and Objects in Python

# Study the class below for 45 seconds.
# Then scroll down and answer the questions FROM MEMORY.
# Run to verify!

# ─── Memorise this class ─────────────────────────────────────────
class Player:
    team = "Progra XI"      # class attribute

    def __init__(self, name, role, jersey):
        self.name    = name
        self.role    = role
        self.jersey  = jersey
        self.runs    = 0
        self.wickets = 0

    def bat(self, runs):
        self.runs += runs

    def bowl(self, wickets):
        self.wickets += wickets

    def stats(self):
        print(f"  {self.jersey:>2}. {self.name:<12} [{self.role:<10}]"
              f"  Runs: {self.runs:>4}  Wkts: {self.wickets}")

    def __str__(self):
        return f"Player({self.name}, #{self.jersey})"

# ─── Objects created ─────────────────────────────────────────────
p1 = Player("Aarav",   "Batsman",  7)
p2 = Player("Karthik", "Bowler",  11)
p3 = Player("Diya",    "All-rounder", 3)

p1.bat(45)
p1.bat(62)
p2.bowl(3)
p3.bat(38)
p3.bowl(2)
p2.bat(5)

print("=== Player Objects (study for 45 seconds) ===")
for p in [p1, p2, p3]:
    p.stats()
print(f"Team: {Player.team}")

print()
print("─" * 55)
print("Answer from memory — then verify below!")
print("─" * 55)
print()

# --- Q1: What is the class attribute shared by all players? ---
print(f"Q1: Class attribute 'team' = '{Player.team}'")

# --- Q2: What is Aarav's jersey number? ---
print(f"Q2: Aarav's jersey = {p1.jersey}")

# --- Q3: How many total runs did p1 score? ---
print(f"Q3: p1 total runs = {p1.runs}")

# --- Q4: What is Karthik's role? ---
print(f"Q4: Karthik's role = '{p2.role}'")

# --- Q5: How many wickets did Diya take? ---
print(f"Q5: Diya's wickets = {p3.wickets}")

# --- Q6: What does str(p2) return? ---
print(f"Q6: str(p2) = '{str(p2)}'")

# --- Q7: After p2.bat(5), what is p2.runs? ---
print(f"Q7: p2.runs = {p2.runs}")

print()
print("─" * 55)
print("Score yourself:")
print("  7/7 → Exceptional focus and memory!")
print("  5-6 → Great — review missed details.")
print("  3-4 → Good — study method by method.")
print("  0-2 → Re-read the class once per method, then test again.")

# Think:
# 1. Which part was hardest to remember — attributes, method logic, or class attributes?
# 2. If you added a fourth player, what three lines would you write?
