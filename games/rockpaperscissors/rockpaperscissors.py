import random

def get_computer_choice():
   options = ["rock", "scissors", "paper"]
   return random.choice(options)

def get_user_choice():
  user_choice= input("Enter your choice:[rock , paper, scissors] : ")
  return user_choice

def find_who_wins(computer_choice,user_choice):
   if(user_choice==computer_choice):
       print("Its a Tie")
       return 0
   elif(user_choice=='rock' and computer_choice=='scissors'):
       print("You win !!!")
       return 1
   else:
       print("You lose")
       return 0


def play():
   print("Welcome to rock,paper, scissors game !!!")
   name=input("Please enter your name : ")
   print(f"Welcome {name} !!!")
   while True:
       user_choice = get_user_choice()
       computer_choice = get_computer_choice()
       print('computer choice : ' + computer_choice)
       print('your choice : ' + user_choice)
       score = find_who_wins(computer_choice, user_choice)
       print(f"score is {score}")
       continue_play=input("Do you want to continue the game ? : yes or no : ")
       print('continue play : ' + continue_play)
       if (continue_play != 'yes'):
           print("Thanks for playing ! Hope you enjoyed the game ")
           do_quit=input("Do you want to quit the game ? : yes or no :")
           if(do_quit=='yes'):
               break
           else:
               play()


play()