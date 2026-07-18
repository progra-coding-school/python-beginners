import random
#step one

user_score = 0
computer_score = 0

#step two

def greet_user():
    print("Welcome to the Rock, Paper, Scissors Game")

#step three

def get_user_choice():
  user_choice=input("plese enter your option as rock, paper, or scissor:")
  return user_choice

#step four

def get_computer_choice():
   """Return a random choice for the computer."""
   return random.choice [("rock", "paper", "scissor")]

#step five

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

#step six

def update_score(winner, user_score, computer_score):
  if winner== "user":
      user_score= user_score+1
  elif winner == "computer"
      computer_score= computer_score+1
    else:
        print("Its a tie")
    return user_score, computer_score

#step seven

def decide_final_winner(user_score, computer_score):
    print("User:", user_score)
    print("Computer:", computer_score)
    if user_score > computer_score:
        print("Final Winner is USER")
    elif computer_score > user_score:
        print("Final Winner is COMPUTER")
    else:
        print("The game is a TIE")

#step eight

def thank_you():
  print("thank you for playing and hope you enjoyed.")

def validate_input(user_choice):
    choices = ["rock", "paper", "scissors"]
    if not user_choice in choices:
        print("Enter a valid choice")
        return False
    else:
        return True

#step nine

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

#step ten

play_game(user_score, computer_score)
