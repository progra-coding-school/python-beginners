


def validate_input(user_choice):
    choices=["rock","paper","scissors"]
    print(user_choice in  choices)
    if not user_choice in  choices:
        print("Enter a valid choice")
        return False
    else:
        return True


while(True):
    user_choice = input("Please enter your choice as rock, paper or scissors:")
    is_valid = validate_input(user_choice)
    print("is_valid--while loop", is_valid)
    if is_valid:
        break


