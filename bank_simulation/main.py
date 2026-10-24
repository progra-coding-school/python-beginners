from transactions import transactions
from money_reciver import recive_money
print("==================================")
print(" BANKING SYSTEM.")
print("==================================")
print("==================================")
print("TRANSACTION CENTRE.")
print("==================================")
print("WELCOME.")
#settings
bank_balance=999999
def account_signing_in_creating():
    username = "HanielZerubbabel"
    password="Haniel12345678910!@#$%^&*()"
    #account creation
    account_y_n_question=input("do you have a account if no write n if yes write y.:")
    if account_y_n_question=="n":
        print("Then create your account here.")
        name=input("Enter your full name:")
        age=int(input("Enter your age remember you write as a number:"))
        username=input("Enter yor user name:")
        password=input("Enter your password make sure it is long (over 5 characters) :")
        details_entered_fully_y_n_question=input("Have entered all your details ?:")
        if details_entered_fully_y_n_question=="y":
            array_details=[name,age,username,password]
            print(f"""
            FINAL DETAILS FOR ACCOUNT CREATION.
            Fullname={name},
            Age={age},
            Username={username},
            Bank password={password}    
            """)
            create_account_input_y_n_question=input("Do you want to  create the account enter y for yes and n for no ...:")
            if create_account_input_y_n_question=="y":
                account=[]
                account.append(array_details)
                print("ACCOUNT CREATED SUCESSFULLY.")
    elif account_y_n_question=="y":
        username_reciver=input("Enter your username : ")
        password_reciver=input("Enter your password:")
        if username_reciver==username and password_reciver==password :
            print("Welcome back to your account")
        else:
            print("Invalid credationals")
account_signing_in_creating()
def transactions_withdraw_account_details_balance(bank_balance):
    print(f"Your bank balance is {bank_balance}")
    transactions_needed_y_n_question=input("do you want to send money to someone enter y for yes n for no:")
    if transactions_needed_y_n_question=="y":
        transactions(bank_balance)
    else:
        pass
    money_recived_needed_to_see_y_n_question = input("Do you want to see whether did you receive any money enter y for yes and n for no: ")
    if money_recived_needed_to_see_y_n_question=="y":
        recive_money(bank_balance)
    else:
        pass



transactions_withdraw_account_details_balance(bank_balance)


