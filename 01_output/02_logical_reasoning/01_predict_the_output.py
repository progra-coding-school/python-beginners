# Program Code: OUT-LR-01
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning (Tracing)
# Topic: Output in Python

# Read each print() statement. Predict what it shows BEFORE running.

score = 0

print("=== Predict the Output ===")
print("Type exactly what you think will be printed.")
print()

questions = [
    ('print("Hello" + " " + "World")',          "Hello World"),
    ('print(5 + 3)',                             "8"),
    ('print("5" + "3")',                         "53"),
    ('print("Ha" * 3)',                          "HaHaHa"),
    ('print(10 / 2)',                            "5.0"),
    ('print(10 // 3)',                           "3"),
    ('print("*" * 5)',                           "*****"),
    ('print("Age:", 13)',                        "Age: 13"),
    ('print(2 ** 3)',                            "8"),
    ('print("A", "B", "C", sep="-")',            "A-B-C"),
]

for i, (code, answer) in enumerate(questions, 1):
    print("Q" + str(i) + ": " + code)
    user_ans = input("Your answer: ").strip()
    if user_ans == answer:
        print("  Correct! Output:", answer)
        score += 1
    else:
        print("  Answer:", answer)
    print()

print("Score:", score, "/", len(questions))
