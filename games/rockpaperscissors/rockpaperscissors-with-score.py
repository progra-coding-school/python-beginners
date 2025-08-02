import random

#Initialize the dictionary to store scores
scores={}
validation_error=False

def get_computer_choice():
   options = ["rock", "scissors", "paper"]
   return random.choice(options)

def get_user_choice():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input(f"Enter your choice (rock, paper, scissors): ").strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")


def find_who_wins(computer_choice,user_choice):
   if(user_choice==computer_choice):
       print("Its a Tie")
       return 'tie'
   elif(user_choice=='rock' and computer_choice=='scissors') or \
       (user_choice=='scissors' and computer_choice=='paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
       print("You win !!!")
       return 'win'
   else:
       print("You lose")
       return 'lose'

#Function to update the score
def update_score(name,result):
    """
    Update the score for a player based on the result of the game.
    :param name:Name of the player (string)
    :param result:'win' ,'lose' or 'tie' (string)
    """
    if name not in scores:
        scores[name]=0   #Initialize the score for the new player
    if result=='win':
        scores[name]=scores[name]+1

#Function to toteach the scores
def print_score():
    for name,score in scores.items():
        print(f"{name} : {score}")

#Function to toteach the individual players scores
def print_score_player(player_name):
    for name,score in scores.items():
        if(name==player_name):
            print(f"{name} : {score}")


# Function to find and show the winner
def find_winner():
    if not scores:
        print("\nNo players yet, so no winner!")
        return
    max_score = max(scores.values())
    print(f"Max score is {max_score}")
    winners = [name for name, score in scores.items() if score == max_score]
    if len(winners) > 1:
        print(f"\nIt's a tie between: {', '.join(winners)} with {max_score} points!")
    else:
        print(f"\n{winners[0]} is the winner with {max_score} points!")


def play():
   print("Welcome to rock,paper, scissors game !!!")
   name=input("Please enter your name : ")
   print(f"Welcome {name} !!!")
   do_quit='no'
   while do_quit=='no':
       user_choice = get_user_choice()
       computer_choice = get_computer_choice()
       print('computer choice : ' + computer_choice)
       print('your choice : ' + user_choice)
       score = find_who_wins(computer_choice, user_choice)
       #toteach(f"score is {score}")
       update_score(name,score)
       print_score_player(name)
       continue_play=input("Do you want to continue the game ? : yes or no : ")
       print('continue play : ' + continue_play)
       if (continue_play != 'yes'):
           print("Thanks for playing ! Hope you enjoyed the game ")
           do_quit=input("Do you want to quit the game ? : yes or no :")
           if(do_quit=='yes'):
               break
           else:
               play()
   print("The game is over. Thanks for playing. Please find the scores ")
   print_score()

play()
