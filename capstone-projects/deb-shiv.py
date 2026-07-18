user_score=0
computer_score=0

def greet_user():
    print("welcome to the rock-paper-sissors game")

def get_user_choice():
  user_choice = input("please enter your choice as rock, paper or scissors")
  return user_choice

def get_computer_choice():
  """return a random choice for the computer"""
  return random.choice["rock","paper","scissors"]

def check_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "tie"

    elif(user_choice == "rock" and computer_choice == "paper"):
        return "computer"

    elif user_choice == "rock" and computer_choice == "scissors":
        return "user"

    elif user_choice == "paper" and computer_choice == "rock":
        return "user"

    elif user_choice == "paper" and computer_choice == "scissors":
        return "computer"

    elif user_choice == "scissors" and computer_choice == "rock":
        return "computer"

    elif user_choice == "scissors" and computer_choice == "paper":
        return "user"

    else:
        return "invalid input"

def update_score(winner, user_score, computer_score):

    if winner == "user":
        user_score = user_score + 1
    elif winner == "computer":
        computer_score = computer_score + 1
    else:
        print("Its a tie")
    return user_score, computer_score

def decide_final_winner(user_score, computer_score):
  print("user:", user_score)
  print("computer:", computer_score)
  if user_score>computer_score:
    print("final winner is user")
  elif user_score<computer_score:
    print("final winner is computer")
  else:
    ("the game is a tie")

def thank_you():
  print("thanks for laying and hope you enjoyed")

def validate_input(user_choice):
  choices = ["rock", "paper", "scissors"]
  if not user_choice in choices:
    print("enter a valid choice")
    return false
  else:
    return true

def play_game(user_score, computer_score):
  greet_user()
  while true:
    game continue = input("do you want to continue: Yes or No:")
    if game continue == no:
      decide_final_winner(user_score, computer_score)
      break

    while (true):
      user_choice = get_user_choice()
      is valid = validate_input(user_choice)
      if is_valid:
        break

      print("user_choice :", user_choice)
      computer_choice = get_computer_choice()
      print("computer_choice :", computer_choice)
      winner = check_winner(computer_choice, user_choice)
      user_choice, computer_choice = update_score(winner, user_score, computer_score)
      print("User score :", user_score)
      print("Computer score :", computer_score)

      thank_you
















