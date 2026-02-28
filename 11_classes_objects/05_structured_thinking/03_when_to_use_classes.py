# Program Code: CL-ST-03
# Title: When to Use Classes
# Cognitive Skill: Structured Thinking
# Topic: Classes and Objects in Python

# Not every problem needs a class.
# Rule of thumb: use a class when you need MULTIPLE instances
# of something that has BOTH data AND behaviour.

print("=== Decision Guide: Function vs Dict vs Class ===\n")

# --- Scenario 1: Calculate area of one rectangle ---
print("Scenario 1: Calculate area of ONE rectangle")
print("→ A simple FUNCTION is enough — no need for a class")
def rect_area(w, h):
    return w * h
print(f"  area(4, 6) = {rect_area(4, 6)}\n")

# --- Scenario 2: Store one student's profile (read-only) ---
print("Scenario 2: Store one student's profile, no behaviour needed")
print("→ A DICT is fine — just data, no methods")
student = {"name": "Aarav", "grade": 7, "city": "Chennai"}
print(f"  {student}\n")

# --- Scenario 3: Manage many bank accounts with deposit/withdraw ---
print("Scenario 3: Manage multiple bank accounts with transactions")
print("→ Use a CLASS — multiple instances, each with data + behaviour")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def __str__(self):
        return f"{self.owner}: Rs.{self.balance}"

a1 = BankAccount("Aarav", 1000)
a2 = BankAccount("Diya",   500)
a1.deposit(200)
print(f"  {a1}")
print(f"  {a2}\n")

# --- Scenario 4: Track a cricket scoreboard during a live match ---
print("Scenario 4: Live cricket scoreboard — state changes over time")
print("→ Use a CLASS — state changes, methods update it")
class Scoreboard:
    def __init__(self, team):
        self.team    = team
        self.runs    = 0
        self.wickets = 0

    def add_runs(self, r):
        self.runs += r

    def wicket_fell(self):
        self.wickets += 1

    def __str__(self):
        return f"{self.team}: {self.runs}/{self.wickets}"

board = Scoreboard("India")
board.add_runs(45)
board.add_runs(62)
board.wicket_fell()
board.add_runs(18)
board.wicket_fell()
print(f"  Score: {board}\n")

# --- Quick Reference ---
print("=== Quick Reference ===")
print("  One-off calculation          → FUNCTION")
print("  Store simple data (one item) → DICT or named tuple")
print("  Multiple things with behaviour → CLASS")
print("  State that changes over time → CLASS")
print("  Reusable blueprint           → CLASS")

# Think:
# 1. Would you use a class to validate an email address? Why or why not?
# 2. Would you use a class for a to-do list app? Plan its attributes and methods.
