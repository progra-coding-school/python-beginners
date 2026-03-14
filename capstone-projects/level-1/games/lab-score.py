user_score = 0
computer_score = 0

# user_score=user_score+1
# print(user_score)
# computer_score = computer_score+1
# print(computer_score)

def update_score(winner, user_score, computer_score):
    if winner == "user":
        user_score = user_score + 1

    elif winner == "computer":
        computer_score = computer_score + 1

    print("Current Score -> User:", user_score, "| Computer:", computer_score)

    return user_score, computer_score

winner="computer"
user_score, computer_score=update_score(winner,user_score,computer_score)
winner="user"
user_score, computer_score=update_score(winner,user_score,computer_score)
winner="computer"
user_score, computer_score=update_score(winner,user_score,computer_score)
winner="user"
user_score, computer_score=update_score(winner,user_score,computer_score)
print(user_score)
print(computer_score)