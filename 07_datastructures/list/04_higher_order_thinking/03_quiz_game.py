# Quiz Game – Powered by Lists
# Two parallel lists: questions[i] pairs with answers[i]
# This is the classic "data-driven" pattern:
#   → store questions and answers in lists
#   → one loop handles ALL questions automatically
#   → adding a new question = just add one line to each list (no code changes!)
# KEY CONCEPT: parallel lists — questions[0] matches answers[0], and so on.

questions = [
    "What is the index of the first item in a list?",
    "Which method adds an item to the END of a list?",
    "Which method removes the LAST item from a list?",
    "What keyword checks if an item EXISTS in a list?",
    "Which method sorts a list in ascending order?",
]

answers = [
    "0",
    "append",
    "pop",
    "in",
    "sort",
]

score = 0
total = len(questions)   # total adjusts automatically if you add more questions

print("You will be asked", total, "questions.")
print()

# One loop handles every question — no need to repeat code for each question
# range(total) gives 0, 1, 2, 3, 4 — the same index for both lists
for i in range(total):
    print("Q" + str(i + 1) + " of " + str(total) + ": " + questions[i])
    player_answer = input("Your answer: ").strip().lower()
    if player_answer == answers[i].lower():   # compare case-insensitively
        print("Correct!")
        score += 1
    else:
        print("Answer:", answers[i])
    print()

print("Score:", score, "/", total)
if score == total:
    print("Perfect score! Python List Master!")
elif score >= 3:
    print("Great effort! Almost there!")
else:
    print("Keep practising — you will get it!")
