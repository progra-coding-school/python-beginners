# Program Code: CL-KN-04
# Title: The Constructor — __init__ in Depth
# Cognitive Skill: Knowledge
# Topic: Classes and Objects in Python

# __init__ is Python's constructor method.
# It is called AUTOMATICALLY when you create an object.
# Its job: set up all the starting data for the object.

# --- Anatomy of __init__ ---
print("=== Anatomy of __init__ ===")

class BankAccount:
    def __init__(self, owner, balance=0):
        # self     — the new object being created
        # owner    — passed in when creating the object
        # balance  — optional, defaults to 0
        self.owner   = owner
        self.balance = balance
        self.transactions = []     # always starts empty
        print(f"  Account created for {self.owner} with Rs.{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +Rs.{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  Insufficient balance! (Have Rs.{self.balance})")
            return
        self.balance -= amount
        self.transactions.append(f"Withdraw: -Rs.{amount}")

    def statement(self):
        print(f"\n  === {self.owner}'s Account ===")
        for t in self.transactions:
            print(f"    {t}")
        print(f"  Balance: Rs.{self.balance}")

# --- Creating accounts ---
print()
acc1 = BankAccount("Aarav", 500)
acc2 = BankAccount("Diya")          # uses default balance = 0

print()

# --- Using methods ---
acc1.deposit(200)
acc1.withdraw(100)
acc1.withdraw(1000)     # should fail
acc1.statement()

print()
acc2.deposit(1000)
acc2.withdraw(300)
acc2.statement()

print()

# --- __init__ runs for EVERY new object ---
print("=== Every object gets its own __init__ run ===")
class Counter:
    def __init__(self, start=0):
        self.count = start
        print(f"  Counter started at {self.count}")

    def increment(self):
        self.count += 1

c1 = Counter()
c2 = Counter(10)
c1.increment()
c1.increment()
print(f"  c1 count: {c1.count}")
print(f"  c2 count: {c2.count}")   # independent

# Think:
# 1. Why does each account have its own separate `transactions` list?
# 2. What would happen if `transactions` was a CLASS attribute instead of an instance attribute?
