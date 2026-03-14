import random

user_score = 0
computer_score = 0

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
        return "tie"

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

def update_score(winner, user_score, computer_score):
    if winner == "user":
        user_score = user_score + 1

    elif winner == "computer":
        computer_score = computer_score + 1

    print("Current Score -> User:", user_score, "| Computer:", computer_score)

    return user_score, computer_score


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
        user_score, computer_score = update_score(winner, user_score, computer_score)
        print("The winner is :", winner)

def decide_final_winner(user_score, computer_score):

    print("\nFinal Score")
    print("User:", user_score)
    print("Computer:", computer_score)

    if user_score > computer_score:
        print("Final Winner is USER")

    elif computer_score > user_score:
        print("Final Winner is COMPUTER")

    else:
        print("The game is a TIE")


def thank_you():
    print("Thanks for playing and  hope you enjoyed")

greet_user()
while True:
    game_continue=input("Do you want to continue: yes or no:")
    if game_continue=="no":
        decide_final_winner(user_score, computer_score)
        break
    user_choice=get_user_choice()
    print("User choice :",user_choice)
    computer_choice=get_computer_choice()
    print("Computer choice :", computer_choice)
    winner=check_winner(computer_choice,user_choice)
    if(winner=='tie'):
        print("Its a tie")
    else:
        print(winner,"own this round :)")
    user_score, computer_score = update_score(winner, user_score, computer_score)

thank_you()






