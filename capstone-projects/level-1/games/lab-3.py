user_score = 0
computer_score = 0
winner="user"

def update_score(winner,user_score,computer_score):
    if winner == "user":
        user_score = user_score + 1
    else:
        computer_score = computer_score + 1
    return user_score,computer_score

user_score,computer_score=update_score(winner,user_score,computer_score)
print("user_score :", user_score)
print("computer_score :", computer_score)