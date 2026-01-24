import random

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

print(get_computer_choice())
#get_user_choice()