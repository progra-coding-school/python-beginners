# Program Code: OUT-FC-02
# Title: Mental Output Challenge
# Cognitive Skill: Focus and Concentration (Mental Tracking)
# Topic: Output in Python

# Predict what each print() shows — in your head, without running it!

score = 0
total = 10

print("=== Mental Output Challenge ===")
print("Predict the EXACT output. Focus on every character!")
print()

questions = [
    ('print("Progra" * 2)',                    "PrograProgra"),
    ('print(3 + 4 * 2)',                       "11"),
    ('print("3" + "4" * 2)',                   "344"),
    ('print(10 / 5)',                          "2.0"),
    ('print(10 // 3, 10 % 3)',                 "3 1"),
    ('print("A", "B", sep="")',                "AB"),
    ('print("Hi", end="! ")\nprint("Bye")',    "Hi! Bye"),
    ('print(2 ** 10)',                          "1024"),
    ('print("=" * 3 + " OK " + "=" * 3)',      "=== OK ==="),
    ('print(len("Aarav"))',                    "5"),
]

for i, (code, answer) in enumerate(questions, 1):
    print("Q" + str(i) + ": " + code)
    user_ans = input("Answer: ").strip()
    if user_ans == str(answer):
        print("  Correct! →", answer)
        score += 1
    else:
        print("  Answer:", answer)
    print()

print("Mental Output Score:", score, "/", total)
if score == total:
    print("Perfect eye for output! You see every detail.")
elif score >= 7:
    print("Strong focus! Review the tricky ones.")
elif score >= 5:
    print("Good effort! Pay extra attention to types and operators.")
else:
    print("Keep practising! Trace each print() step by step.")
