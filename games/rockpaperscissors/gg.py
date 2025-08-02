# Initialize the dictionary to store scores
scores = {}

# Function to update score
def update_score(name, result):
    """
    Update the score for a person based on the result of the game.
    :param name: Name of the person (string)
    :param result: 'win' or 'lose' (string)
    """
    if name not in scores:
        scores[name] = 0  # Initialize score for the new player

    if result == "win":
        scores[name] += 1
    elif result == "lose":
        scores[name] -= 1
    else:
        print("Invalid result. Please use 'win' or 'lose'.")

# Simulate a few iterations
update_score("Alice", "win")
update_score("Bob", "lose")
update_score("Alice", "lose")
update_score("Charlie", "win")

update_score("Alice", "win")
update_score("Alice", "win")
# Print final scores
print("Final Scores:", scores)
