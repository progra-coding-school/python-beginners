import random

# -----------------------------
# Global Score Storage
# -----------------------------
scores = {}


# -----------------------------
# Utility Functions
# -----------------------------
def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])


def get_user_choice():
    """Prompt the user until a valid choice is entered."""
    valid_choices = {"rock", "paper", "scissors"}

    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")


# -----------------------------
# Game Logic
# -----------------------------
def decide_result(user_choice, computer_choice):
    """Determine the result of a round."""
    if user_choice == computer_choice:
        return "tie"

    winning_cases = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }

    if (user_choice, computer_choice) in winning_cases:
        return "win"

    return "lose"


# -----------------------------
# Score Management
# -----------------------------
def update_score(player_name, result):
    """Update player score based on game result."""
    scores.setdefault(player_name, 0)

    if result == "win":
        scores[player_name] += 1


def print_player_score(player_name):
    """Print score of a single player."""
    print(f"{player_name}'s Score: {scores.get(player_name, 0)}")


def print_all_scores():
    """Print all player scores."""
    print("\nFinal Scores:")
    for name, score in scores.items():
        print(f"{name}: {score}")


# -----------------------------
# Winner Determination
# -----------------------------
def announce_winner():
    """Find and announce the overall winner."""
    if not scores:
        print("No games played.")
        return

    max_score = max(scores.values())
    winners = [name for name, score in scores.items() if score == max_score]

    if len(winners) > 1:
        print(f"\nIt's a tie between {', '.join(winners)} with {max_score} points!")
    else:
        print(f"\n🏆 {winners[0]} wins with {max_score} points!")


# -----------------------------
# Main Game Loop
# -----------------------------
def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")

    player_name = input("Enter your name: ").strip()
    print(f"Hello {player_name}! Let's start.\n")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nComputer chose: {computer_choice}")
        print(f"You chose: {user_choice}")

        result = decide_result(user_choice, computer_choice)
        print(f"Result: {result.upper()}")

        update_score(player_name, result)
        print_player_score(player_name)

        if input("\nPlay again? (yes/no): ").strip().lower() != "yes":
            break

    print_all_scores()
    announce_winner()
    print("\nThanks for playing! 👋")


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    play_game()
