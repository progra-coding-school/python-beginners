
'''
Smart ATM Withdrawal.
Problem An ATM allows withdrawal only if:
1.The account balance is at least the withdrawal amount.
2.The withdrawal amount is a multiple of ₹100.
3.The minimum account balance after withdrawal must be ₹1000.

Display one of the following:
1.Transaction Successful
2.Insufficient Balance
3.Enter Amount in Multiples of ₹100
4.Minimum Balance Must Be Maintained
'''


account_balance = int(input("Enter your account balance: "))
withdraw_amount = int(input("Enter the withdrawal amount: "))

if withdraw_amount > account_balance:
    print("Insufficient Balance")
elif withdraw_amount % 100100 != 0:
    print("Enter Amount in Multiples of Rs 100")
elif account_balance - withdraw_amount < 1000:
    print("Minimum Balance Must Be Maintained")
else:
    print("Transaction Successful")
