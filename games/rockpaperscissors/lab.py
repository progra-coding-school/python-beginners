import random

def get_computer_choice():
   options = ["rock", "scissors", "paper"]
   return random.choice(options)

computer_choice=get_computer_choice()
print(computer_choice)