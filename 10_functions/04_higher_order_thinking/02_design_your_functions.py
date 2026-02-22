# Program Code: FN-HOT-02
# Title: Design Your Functions — ATM Machine
# Cognitive Skill: Higher Order Thinking (Design from Scratch)
# Topic: Functions in Python

# Design challenge: Build a mini ATM using functions.
# Each operation is its own function — just like a real ATM.

# --- Account data ---
account = {
    "name": "Aarav",
    "pin": "1234",
    "balance": 5000
}

# --- FUNCTION 1: Verify PIN ---
def verify_pin(stored_pin, entered_pin):
    return stored_pin == entered_pin

# --- FUNCTION 2: Check balance ---
def check_balance(balance):
    return balance

# --- FUNCTION 3: Deposit money ---
def deposit(balance, amount):
    if amount <= 0:
        return balance, "Invalid amount. Enter a positive value."
    new_balance = balance + amount
    return new_balance, f"Rs.{amount} deposited successfully."

# --- FUNCTION 4: Withdraw money ---
def withdraw(balance, amount):
    if amount <= 0:
        return balance, "Invalid amount."
    if amount > balance:
        return balance, "Insufficient balance."
    if amount % 100 != 0:
        return balance, "Amount must be a multiple of Rs.100."
    new_balance = balance - amount
    return new_balance, f"Rs.{amount} withdrawn successfully."

# --- FUNCTION 5: Display menu ---
def show_menu():
    print("\n=== Progra ATM ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# --- FUNCTION 6: Print receipt ---
def print_receipt(name, action, amount, balance):
    print(f"\n--- Receipt ---")
    print(f"Account: {name}")
    print(f"Action:  {action}")
    if amount > 0:
        print(f"Amount:  Rs.{amount}")
    print(f"Balance: Rs.{balance}")
    print("---------------")

# --- MAIN ATM PROGRAM ---
print(f"Welcome to Progra ATM")
name = account["name"]
entered = input("Enter your 4-digit PIN: ")

if not verify_pin(account["pin"], entered):
    print("Wrong PIN. Access denied.")
else:
    print(f"Welcome, {name}!")
    while True:
        show_menu()
        choice = input("Choose (1-4): ")

        if choice == "1":
            bal = check_balance(account["balance"])
            print(f"Your balance: Rs.{bal}")
            print_receipt(name, "Balance Check", 0, bal)

        elif choice == "2":
            amt = int(input("Enter deposit amount: Rs."))
            account["balance"], msg = deposit(account["balance"], amt)
            print(msg)
            print_receipt(name, "Deposit", amt, account["balance"])

        elif choice == "3":
            amt = int(input("Enter withdrawal amount: Rs."))
            account["balance"], msg = withdraw(account["balance"], amt)
            print(msg)
            print_receipt(name, "Withdrawal", amt, account["balance"])

        elif choice == "4":
            print(f"Thank you, {name}. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Think:
# 1. What new function would you add for 'Transfer to another account'?
# 2. How would you add a 3-tries limit for the wrong PIN?
