name = input("Enter your name: ")
budget = float(input("Enter your budget: ₹"))

# Get the first expense
category1 = input("Enter first expense category: ")
amount1 = float(input("Enter first expense amount: ₹"))

# Get the second expense
category2 = input("Enter second expense category: ")
amount2 = float(input("Enter second expense amount: ₹"))

# Get the third expense
category3 = input("Enter third expense category: ")
amount3 = float(input("Enter third expense amount: ₹"))

# Calculate total expenses
total_expenses = amount1 + amount2 + amount3

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Display the report
print("\n--- Expense Report ---")
print("Name:", name)
print("Expense 1:", category1, "- ₹", amount1)
print("Expense 2:", category2, "- ₹", amount2)
print("Expense 3:", category3, "- ₹", amount3)
print("Total Expenses: ₹", total_expenses)
print("Remaining Budget: ₹", remaining_budget)

if total_expenses > budget:
    print("Status: Budget Exceeded")
else:
    print("Status: Within Budget")