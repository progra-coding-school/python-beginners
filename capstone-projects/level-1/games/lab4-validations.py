user_choice="rock"
print( user_choice !="rock")
print(user_choice !="rock" and user_choice !="paper" and user_choice !="scissors")

def user_input(user_choice):
    print("user_choice",user_choice)
    if user_choice !="rock" or user_choice !="paper" or user_choice !="scissors":
        print("t")
        return "invalid choice"
    else:
        return "valid choice"


print(user_input("rock"))