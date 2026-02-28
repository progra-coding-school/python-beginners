# Program Code: CL-PS-02
# Title: Bank Account Class
# Cognitive Skill: Problem Solving
# Topic: Classes and Objects in Python

# Problem:
# Build a BankAccount class that supports:
# deposit, withdraw, transfer, statement, and interest.

class BankAccount:
    INTEREST_RATE = 0.04    # 4% annual interest — class attribute

    def __init__(self, owner, account_no, opening_balance=0):
        self.owner      = owner
        self.account_no = account_no
        self._balance   = opening_balance
        self._history   = []
        self._log(f"Account opened with Rs.{opening_balance}")

    def _log(self, message):
        """Internal method — record a transaction."""
        self._history.append(message)

    def deposit(self, amount):
        if amount <= 0:
            print(f"  [{self.owner}] Deposit must be positive.")
            return False
        self._balance += amount
        self._log(f"Deposited   +Rs.{amount:>7}  | Balance: Rs.{self._balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print(f"  [{self.owner}] Amount must be positive.")
            return False
        if amount > self._balance:
            print(f"  [{self.owner}] Insufficient funds (Rs.{self._balance} available).")
            return False
        self._balance -= amount
        self._log(f"Withdrew    -Rs.{amount:>7}  | Balance: Rs.{self._balance}")
        return True

    def transfer(self, amount, target_account):
        print(f"  Transferring Rs.{amount} from {self.owner} → {target_account.owner}")
        if self.withdraw(amount):
            target_account.deposit(amount)
            self._log(f"Transferred to {target_account.owner}")
            target_account._log(f"Received from {self.owner}")

    def add_interest(self):
        interest = round(self._balance * self.INTEREST_RATE, 2)
        self._balance += interest
        self._log(f"Interest    +Rs.{interest:>7}  | Balance: Rs.{self._balance}")
        print(f"  [{self.owner}] Interest added: Rs.{interest}")

    @property
    def balance(self):
        return self._balance

    def statement(self):
        print(f"\n  === Account Statement: {self.owner} (A/C {self.account_no}) ===")
        for entry in self._history:
            print(f"    {entry}")
        print(f"  Current Balance: Rs.{self._balance}\n")

# --- Demo ---
aarav_acc = BankAccount("Aarav",   "ACC001", 1000)
diya_acc  = BankAccount("Diya",    "ACC002",  500)

aarav_acc.deposit(500)
aarav_acc.withdraw(200)
aarav_acc.withdraw(2000)        # should fail
aarav_acc.transfer(300, diya_acc)
aarav_acc.add_interest()

diya_acc.deposit(1000)
diya_acc.add_interest()

aarav_acc.statement()
diya_acc.statement()

# Think:
# 1. Why does the `_log` method start with an underscore?
# 2. How would you add a minimum balance requirement of Rs.100?
