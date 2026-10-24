from bank_simulation.transaction_ui import ui
def transactions(bank_balance):
    transaction_amount_question=int(input("Enter the amount to sent to someone in integers that are  whole numbers:"))
    amount_transaction=transaction_amount_question
    if bank_balance<transaction_amount_question:
        print("you don't have enough money to send to someone...")
    elif transaction_amount_question==str:
        print("you should write the amount in numbers...")
    elif transaction_amount_question==bool:
        print("you should write the amount in whole numbers...")
    else:
        print("perfect.your required amount of money will be sent to the person who you need to send..")
        bank_balance=bank_balance-transaction_amount_question
        print(f"your updated bank balance ={bank_balance}")
        print(ui)
transactions(bank_balance=int)

