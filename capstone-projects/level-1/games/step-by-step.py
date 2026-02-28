import random

def get_user_choice():
    user_choice=input("Please enter your choice as rock, paper or scissors:")
    return user_choice

user_choice=get_user_choice()
print("user choice is :",user_choice)


def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

computer_choice=get_computer_choice()
print("computer choice is :",computer_choice)


def check_winner(computer_choice, user_choice):

    if computer_choice == user_choice:
        return "Tie"

    elif computer_choice == "rock" and user_choice == "paper":
        return "User wins"

    elif computer_choice == "rock" and user_choice == "scissors":
        return "Computer wins"

    elif computer_choice == "paper" and user_choice == "rock":
        return "Computer wins"

    elif computer_choice == "paper" and user_choice == "scissors":
        return "User wins"

    elif computer_choice == "scissors" and user_choice == "rock":
        return "User wins"

    elif computer_choice == "scissors" and user_choice == "paper":
        return "Computer wins"

    else:
        return "Invalid input"

print("The winner is :",check_winner(computer_choice,user_choice))









