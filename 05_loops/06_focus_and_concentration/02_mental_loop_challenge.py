# Program Code: LP-FC-02
# Title: Mental Loop Challenge
# Cognitive Skill: Focus and Concentration (Mental Tracking)
# Topic: Loops in Python

# Trace each loop in your HEAD — no pen, no paper.
# Track the variable at every step!

score = 0
total = 8

print("=== Mental Loop Challenge ===")
print("Solve each one in your head. Track every iteration!")
print()

questions = [
    (
        "total = 0\nfor n in range(1, 5):\n    total += n\nprint(total)",
        10,
        "1+2+3+4 = 10"
    ),
    (
        "x = 1\nwhile x < 50:\n    x *= 2\nprint(x)",
        64,
        "1→2→4→8→16→32→64 (64 >= 50, loop stops)"
    ),
    (
        "count = 0\nfor i in range(10):\n    if i % 3 == 0:\n        count += 1\nprint(count)",
        4,
        "i=0,3,6,9 are divisible by 3 → count=4"
    ),
    (
        "result = 1\nfor i in range(1, 5):\n    result *= i\nprint(result)",
        24,
        "1×1=1, ×2=2, ×3=6, ×4=24 (4 factorial)"
    ),
    (
        "total = 0\nfor i in range(1, 11, 2):\n    total += i\nprint(total)",
        25,
        "1+3+5+7+9 = 25 (odd numbers 1–9)"
    ),
    (
        "s = ''\nfor ch in 'hello':\n    s = ch + s\nprint(s)",
        "olleh",
        "Prepend each char: h→hh→lh→... builds 'olleh' (reversed!)"
    ),
    (
        "n = 100\ncount = 0\nwhile n > 1:\n    n //= 2\n    count += 1\nprint(count)",
        6,
        "100→50→25→12→6→3→1 → 6 steps"
    ),
    (
        "total = 0\nfor i in range(1, 6):\n    total += i * i\nprint(total)",
        55,
        "1+4+9+16+25 = 55 (sum of squares 1–5)"
    ),
]

for i, (code, answer, explanation) in enumerate(questions, 1):
    print(f"Q{i}:")
    for line in code.split('\n'):
        print(f"  {line}")
    user_ans = input("Answer: ").strip()
    try:
        correct = str(user_ans) == str(answer)
    except:
        correct = False
    if correct:
        print(f"  Correct! {explanation}")
        score += 1
    else:
        print(f"  Answer: {answer} — {explanation}")
    print()

print(f"Mental Loop Score: {score} / {total}")
if score == total:
    print("Perfect! You can trace loops in your sleep!")
elif score >= 6:
    print("Excellent focus! A couple more runs and you'll be perfect.")
elif score >= 4:
    print("Good effort! Slow down and trace each variable step by step.")
else:
    print("Keep practising! Write out variables on paper as you trace.")
