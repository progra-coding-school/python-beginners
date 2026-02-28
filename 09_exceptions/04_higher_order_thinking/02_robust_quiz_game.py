# Program Code: EX-HOT-02
# Title: Robust Quiz Game with Full Error Handling
# Cognitive Skill: Higher Order Thinking
# Topic: Exceptions in Python

# Design challenge:
# Build a quiz game that handles ALL invalid inputs gracefully.
# The game must NEVER crash, no matter what the user types.

# --- Questions bank ---
questions = [
    {
        "question": "What is 7 x 8?",
        "options"  : ["54", "56", "63", "48"],
        "answer"   : 2,     # index of correct option (1-based: option 2 = "56")
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options"  : ["Venus", "Earth", "Mercury", "Mars"],
        "answer"   : 3,     # Mercury
    },
    {
        "question": "How many sides does a hexagon have?",
        "options"  : ["5", "6", "7", "8"],
        "answer"   : 2,
    },
]

# --- Safe input reader (simulated for non-interactive demo) ---
def get_answer(prompt, num_options, simulated_input=None):
    """Return a valid 1-based option number."""
    if simulated_input is not None:
        raw = simulated_input
        print(f"{prompt}{raw}")
    else:
        raw = input(prompt)

    try:
        choice = int(raw)
        if not (1 <= choice <= num_options):
            raise ValueError(f"Must be between 1 and {num_options}")
        return choice
    except ValueError as e:
        return None, str(e)     # signal invalid input

# --- Quiz engine ---
def run_quiz(simulated_answers=None):
    score  = 0
    total  = len(questions)
    sim_iter = iter(simulated_answers) if simulated_answers else None

    print("=== Progra Quiz Game ===\n")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for j, opt in enumerate(q["options"], 1):
            print(f"     {j}. {opt}")

        # Keep asking until a valid answer is given
        attempts = 0
        while True:
            sim = next(sim_iter, None) if sim_iter else None
            result = get_answer("Your answer (1-4): ", len(q["options"]), sim)

            if isinstance(result, tuple):
                _, err = result
                print(f"  Invalid input: {err}. Try again.")
                attempts += 1
                if attempts >= 3:
                    print("  Too many invalid attempts. Skipping question.")
                    break
            else:
                if result == q["answer"]:
                    print("  Correct!\n")
                    score += 1
                else:
                    correct_opt = q["options"][q["answer"] - 1]
                    print(f"  Wrong. Correct answer: {q['answer']}. {correct_opt}\n")
                break

    print("=== Results ===")
    print(f"Score: {score}/{total}")
    if score == total:
        print("Perfect score! Outstanding!")
    elif score >= total // 2:
        print("Good effort! Keep practising.")
    else:
        print("Keep going — practice makes perfect!")

# --- Demo with simulated inputs (includes some invalid ones) ---
simulated = ["abc", "0", "2",   # Q1: two invalid, then correct
             "3",                # Q2: Mercury
             "99", "3", ]        # Q3: one invalid, then correct
run_quiz(simulated_answers=simulated)

# Think:
# 1. Why does the game limit invalid attempts to 3 before skipping?
# 2. How would you save the score to a file at the end using try/except?
