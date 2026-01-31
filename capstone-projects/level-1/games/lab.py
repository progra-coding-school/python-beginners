import random
def greet_user():
    ''' Greet the user'''
    print("Hello! Welcome to the game!")

def get_user_choice():
    '''Prompt the user until a valid choice is entered '''
    valid_choices={"rock","paper","scissors"}
    while True:
        choice=input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")


def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def decide_result(user_choice, computer_choice):
    """Determine the result of a round."""
    # Check tie first
    if user_choice == computer_choice:
        return "tie"

    # Define all winning combinations
    winning_cases = {
        ("rock", "scissors"),  # rock crushes scissors
        ("scissors", "paper"), # scissors cut paper
        ("paper", "rock"),     # paper covers rock
    }

    # Check if user won
    if (user_choice, computer_choice) in winning_cases:
        return "win"

    # Otherwise user lost
    return "lose"

user_choice = get_user_choice()
computer_choice = get_computer_choice()
print(f"\nComputer chose: {computer_choice}")
print(f"You chose: {user_choice}")
result=decide_result(user_choice, computer_choice)
print(f"Result: {result.upper()}")









