import random

def greet_user():
    print("Welcome to the Rock, Paper, Scissors Game")

def start_game():
    game_start=input("Do you want to start/continue the game ?:yes or no : ")
    return game_start

def get_user_choice():
    user_choice=input("Please enter your choice as rock, paper or scissors:")
    return user_choice

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def check_winner(computer_choice, user_choice):

    if computer_choice == user_choice:
        return "Tie"

    elif computer_choice == "rock" and user_choice == "paper":
        return "user"

    elif computer_choice == "rock" and user_choice == "scissors":
        return "computer"

    elif computer_choice == "paper" and user_choice == "rock":
        return "computer"

    elif computer_choice == "paper" and user_choice == "scissors":
        return "user"

    elif computer_choice == "scissors" and user_choice == "rock":
        return "user"

    elif computer_choice == "scissors" and user_choice == "paper":
        return "computer"

    else:
        return "Invalid input"

def play_game():
    greet_user()
    while True:
        continue_game = start_game()
        print("continue_game:", continue_game)
        if continue_game == "no":
            break
        print("user wants to continue the game")
        user_choice = get_user_choice()
        print("user choice is :", user_choice)
        computer_choice = get_computer_choice()
        print("computer choice is :", computer_choice)
        winner = check_winner(computer_choice, user_choice)
        print("The winner is :", winner)



play_game()










