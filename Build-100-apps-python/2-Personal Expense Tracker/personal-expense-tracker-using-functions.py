def get_user_details():
    name = input("Enter your name: ")
    budget = float(input("Enter your budget: ₹"))
    return name, budget


def get_expense(expense_number):
    category = input("Enter expense " + str(expense_number) + " category: ")
    amount = float(input("Enter expense " + str(expense_number) + " amount: ₹"))
    return category, amount


def calculate_total(amount1, amount2, amount3):
    total = amount1 + amount2 + amount3
    return total


def display_report(name, budget, category1, amount1,
                   category2, amount2, category3, amount3, total):
    remaining_budget = budget - total

    print("\n--- Expense Report ---")
    print("Name:", name)
    print("Expense 1:", category1, "- ₹", amount1)
    print("Expense 2:", category2, "- ₹", amount2)
    print("Expense 3:", category3, "- ₹", amount3)
    print("Total Expenses: ₹", total)
    print("Remaining Budget: ₹", remaining_budget)

    if total > budget:
        print("Status: Budget Exceeded")
    else:
        print("Status: Within Budget")


# Main program
name, budget = get_user_details()

category1, amount1 = get_expense(1)
category2, amount2 = get_expense(2)
category3, amount3 = get_expense(3)

total = calculate_total(amount1, amount2, amount3)

display_report(name, budget, category1, amount1,
               category2, amount2, category3, amount3, total)