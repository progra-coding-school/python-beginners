import random

#1.Score variables created
user_score = 0
computer_score = 0

#2.greet_user method created
def greet_user():
    print("Welcome to the Rock, Paper, Scissors Game")

#3.get_user_choice method created
def get_user_choice():
    user_choice=input("Please enter your choice as rock, paper or scissors:")
    return user_choice

#4.get_computer_choice method created
def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

#5.check_winner method created
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

#6.update_score method created
def update_score(winner, user_score, computer_score):
    if winner == "user":
        user_score = user_score + 1
    elif winner=="computer" :
        computer_score = computer_score + 1
    else:
        print("Its a tie")
    return user_score, computer_score

#7.decide_final_winner method created
def decide_final_winner(user_score, computer_score):
    print("User:", user_score)
    print("Computer:", computer_score)
    if user_score > computer_score:
        print("Final Winner is USER")
    elif computer_score > user_score:
        print("Final Winner is COMPUTER")
    else:
        print("The game is a TIE")

#8.thank_you method created
def thank_you():
    print("Thanks for playing and  hope you enjoyed")

#9.validate_input method created
def validate_input(user_choice):
    choices=["rock","paper","scissors"]
    if not user_choice in choices:
        print("Enter a valid choice")
        return False
    else:
        return True


#10.main method to run the game
def play_game(user_score, computer_score):
    greet_user()
    while True:
        game_continue = input("Do you want to continue: yes or no:")
        if game_continue == "no":
            decide_final_winner(user_score, computer_score)
            break

        while (True):
            user_choice = get_user_choice()
            is_valid = validate_input(user_choice)
            if is_valid:
                break

        print("User choice :", user_choice)
        computer_choice = get_computer_choice()
        print("Computer choice :", computer_choice)
        winner = check_winner(computer_choice, user_choice)
        user_score, computer_score = update_score(winner, user_score, computer_score)
        print("User score :", user_score)
        print("Computer score :", computer_score)
        thank_you()

#11.call the play_game method
play_game(user_score, computer_score)






