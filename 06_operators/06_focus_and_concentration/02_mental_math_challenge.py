# Program Code: OP-FC-02
# Title: Mental Math Challenge — Operators
# Cognitive Skill: Focus and Concentration (Mental Tracking)
# Topic: Operators in Python

# Calculate each expression in your HEAD before running it.
# No pen, no paper — just focus!

score = 0
total = 10

print("=== Mental Math Challenge ===")
print("Solve each expression in your head. Apply BODMAS!")
print()

questions = [
    ("5 + 3 * 2",          5 + 3 * 2),
    ("(5 + 3) * 2",        (5 + 3) * 2),
    ("20 - 10 // 3",       20 - 10 // 3),
    ("15 % 4",             15 % 4),
    ("2 ** 4 - 6",         2 ** 4 - 6),
    ("100 // 7",           100 // 7),
    ("100 % 7",            100 % 7),
    ("3 * 4 + 2 ** 2",     3 * 4 + 2 ** 2),
    ("(10 - 4) * (3 + 2)", (10 - 4) * (3 + 2)),
    ("50 // 6 + 50 % 6",   50 // 6 + 50 % 6),
]

for i, (expr, answer) in enumerate(questions, 1):
    user_ans = input(f"Q{i}: {expr} = ")
    try:
        if float(user_ans.strip()) == answer:
            print(f"  Correct! {expr} = {answer}")
            score += 1
        else:
            print(f"  Wrong! {expr} = {answer}")
    except:
        print(f"  Invalid input. {expr} = {answer}")
    print()

# Final score
print(f"Mental Math Score: {score} / {total}")
if score == total:
    print("Perfect! Your mental operator skills are sharp!")
elif score >= 7:
    print("Great focus! A few more practice rounds and you'll be perfect.")
elif score >= 5:
    print("Good effort! Keep practising BODMAS — it gets faster with practice.")
else:
    print("Keep going! Try again after reviewing operator precedence.")
