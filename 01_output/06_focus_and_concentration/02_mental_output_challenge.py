# Mental Output Challenge
# Predict what each print() shows — in your head, without running it!
# Mental calculation builds the habit of tracing code before executing it.

score = 0
total = 10

print("Mental Output Challenge")
print("Predict the EXACT output. Focus on every character!")
print()

# Each question is (code_as_text, exact_expected_answer)
# Think through each one carefully — operator type and data type both matter
questions = [
    ('print("Progra" * 2)',                    "PrograProgra"),
    ('print(3 + 4 * 2)',                       "11"),          # * before + (BODMAS!)
    ('print("3" + "4" * 2)',                   "344"),         # "4"*2="44", then "3"+"44"
    ('print(10 / 5)',                          "2.0"),          # / always gives float
    ('print(10 // 3, 10 % 3)',                 "3 1"),          # quotient and remainder
    ('print("A", "B", sep="")',                "AB"),           # sep="" removes space
    ('print("Hi", end="! ")\nprint("Bye")',    "Hi! Bye"),      # end keeps on same line
    ('print(2 ** 10)',                          "1024"),         # 2 to the power of 10
    ('print("=" * 3 + " OK " + "=" * 3)',      "=== OK ==="),   # repetition + joining
    ('print(len("Aarav"))',                    "5"),             # len counts characters
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
