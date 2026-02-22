# Program Code: FN-HOT-03
# Title: Function Mini App — Student Quiz Game
# Cognitive Skill: Higher Order Thinking (Creative Synthesis)
# Topic: Functions in Python

# Build a complete quiz game using functions.
# Every feature is a separate function — clean and reusable.

import random

# --- Question bank ---
QUESTIONS = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options":  ["A. function", "B. def", "C. define", "D. func"],
        "answer":   "B"
    },
    {
        "question": "What does 'return' do in a function?",
        "options":  ["A. Prints a value", "B. Stops the program", "C. Sends a value back", "D. Creates a loop"],
        "answer":   "C"
    },
    {
        "question": "What is a 'parameter'?",
        "options":  ["A. A value passed when calling", "B. A placeholder in the definition", "C. A type of loop", "D. A variable outside the function"],
        "answer":   "B"
    },
    {
        "question": "What does this return? def f(x): return x * x  →  f(5)",
        "options":  ["A. 10", "B. 55", "C. 25", "D. 5"],
        "answer":   "C"
    },
    {
        "question": "What is printed? def show(): print('Hi')  result = show()  print(result)",
        "options":  ["A. Hi", "B. None", "C. Hi\\nNone", "D. Error"],
        "answer":   "C"
    },
]

# --- FUNCTIONS ---
def get_player_name():
    return input("Enter your name: ")

def show_welcome(name):
    print(f"\nWelcome, {name}! Let's test your Python Functions knowledge.")
    print(f"You'll get {len(QUESTIONS)} questions. Answer A, B, C, or D.\n")

def ask_question(q_num, question_data):
    print(f"Q{q_num}: {question_data['question']}")
    for option in question_data["options"]:
        print(f"  {option}")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    return answer

def check_answer(player_answer, correct_answer):
    return player_answer == correct_answer

def calculate_percentage(score, total):
    return (score / total) * 100

def get_performance_label(percentage):
    if percentage == 100:
        return "PERFECT! You're a Functions Master!"
    elif percentage >= 80:
        return "Excellent! Strong understanding of functions."
    elif percentage >= 60:
        return "Good effort! Review the tricky parts."
    else:
        return "Keep practising! Functions get easier with time."

def show_final_result(name, score, total):
    percentage = calculate_percentage(score, total)
    label = get_performance_label(percentage)
    print("\n" + "=" * 40)
    print(f"  Quiz Complete — {name}")
    print(f"  Score: {score} / {total}")
    print(f"  Percentage: {percentage:.0f}%")
    print(f"  {label}")
    print("=" * 40)

def run_quiz():
    name = get_player_name()
    show_welcome(name)

    score = 0
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        player_ans = ask_question(i, q)
        if check_answer(player_ans, q["answer"]):
            print("  Correct!\n")
            score += 1
        else:
            print(f"  Wrong! Correct answer: {q['answer']}\n")

    show_final_result(name, score, len(questions))

# --- Run the app ---
run_quiz()
