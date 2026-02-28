# Program Code: CL-UN-04
# Title: Encapsulation — Bundling Data and Behaviour
# Cognitive Skill: Understanding
# Topic: Classes and Objects in Python

# ENCAPSULATION: keeping data and the methods that work on it
# inside ONE class — so the object manages itself.

# --- Without encapsulation: data is exposed and fragile ---
print("=== WITHOUT encapsulation ===")

# Bare dictionary — anyone can change anything, even nonsensically
account = {"owner": "Aarav", "balance": 500}

# Nothing stops this accidental corruption:
account["balance"] = -99999     # silent disaster!
print("Corrupted balance:", account["balance"])

print()

# --- With encapsulation: the class controls access ---
print("=== WITH encapsulation ===")

class BankAccount:
    def __init__(self, owner, opening_balance=0):
        self.owner   = owner
        self._balance = opening_balance     # _ means "don't touch directly"

    def deposit(self, amount):
        if amount <= 0:
            print("  Deposit must be positive.")
            return
        self._balance += amount
        print(f"  Deposited Rs.{amount}. Balance: Rs.{self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("  Withdrawal must be positive.")
            return
        if amount > self._balance:
            print(f"  Insufficient funds. Balance: Rs.{self._balance}")
            return
        self._balance -= amount
        print(f"  Withdrew Rs.{amount}. Balance: Rs.{self._balance}")

    def get_balance(self):
        return self._balance    # read-only access to balance

acc = BankAccount("Aarav", 500)
acc.deposit(200)
acc.withdraw(100)
acc.withdraw(1000)     # rejected by the class
print(f"  Final balance: Rs.{acc.get_balance()}")

print()

# --- What encapsulation protects ---
print("=== What encapsulation gives you ===")
print("  1. VALIDATION — the class checks data before accepting it")
print("  2. CONSISTENCY — balance can only change through deposit/withdraw")
print("  3. CLARITY — each method has one clear purpose")
print("  4. SAFETY — internal data can't be corrupted from outside")

print()

# --- Real-life analogy ---
print("=== Real-life analogy ===")
print("An ATM machine ENCAPSULATES your bank account.")
print("  You can only: deposit, withdraw, check balance.")
print("  You CANNOT: directly open the machine and change the number.")
print("  The machine's rules protect the data inside.")

# Think:
# 1. What would happen if a student could directly set their own marks in the database?
# 2. What is the purpose of the _ prefix on _balance?
