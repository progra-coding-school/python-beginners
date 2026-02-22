# Program Code: LIST-CT-03
# Title: Assumption Breaker — True or False About Lists?
# Cognitive Skill: Critical Thinking (Challenge assumptions)
# Topic: Lists in Python
#
# ════════════════════════════════════════════════════════
#  THE CHALLENGE
# ════════════════════════════════════════════════════════
#
#  Many beginners make WRONG ASSUMPTIONS about lists.
#  They believe things that seem logical — but are false!
#
#  Your job: Read each statement. Decide: True or False?
#  Then RUN the code to verify your thinking.
#
#  A critical thinker does not guess — they TEST.
#
# ════════════════════════════════════════════════════════

print("=" * 55)
print("  ASSUMPTION BREAKER — TRUE OR FALSE?")
print("=" * 55)
print()

score = 0

def ask(statement, correct_answer, explanation):
    global score
    print(f"  Statement: {statement}")
    answer = input("  True or False? ").strip().lower()
    if answer in ["true", "t", "false", "f"]:
        is_true = answer in ["true", "t"]
        if is_true == correct_answer:
            print("  ✅ Correct!")
            score += 1
        else:
            print(f"  ❌ Wrong! The answer is: {'True' if correct_answer else 'False'}")
        print(f"  💡 {explanation}")
    else:
        print("  ⚠️  Please type True or False.")
    print()

# ── Statement 1 ──────────────────────────────────────────
ask(
    statement   = 'fruits = ["Mango", "Apple", "Banana"]\n  fruits[3] gives "Banana"',
    correct_answer = False,
    explanation = "fruits[3] causes IndexError! The last index is 2, not 3.\n"
                  "  Rule: A list of 3 items has indexes 0, 1, 2."
)

# ── Statement 2 ──────────────────────────────────────────
ask(
    statement   = "A list can hold both numbers and strings at the same time.",
    correct_answer = True,
    explanation = 'mixed = [1, "hello", 3.14, True]  → This is valid Python!\n'
                  "  Lists can hold any type — they are flexible containers."
)

# ── Statement 3 ──────────────────────────────────────────
ask(
    statement   = 'numbers = [5, 3, 8, 1]\n  numbers[-1] causes an error.',
    correct_answer = False,
    explanation = "numbers[-1] gives 1 — the LAST item.\n"
                  "  Negative indexing counts from the end: -1 = last, -2 = second last."
)

# ── Statement 4 ──────────────────────────────────────────
ask(
    statement   = 'a = [1, 2, 3]\n  b = a\n  b.append(4) does NOT change a.',
    correct_answer = False,
    explanation = "b = a does NOT copy the list. Both a and b point to the SAME list.\n"
                  "  Changing b ALSO changes a. Use b = a.copy() to make a real copy."
)

# ── Statement 5 ──────────────────────────────────────────
ask(
    statement   = 'numbers = [4, 2, 7, 1]\n  numbers.sort() returns a sorted list.',
    correct_answer = False,
    explanation = "numbers.sort() sorts the list IN PLACE and returns None.\n"
                  "  Use sorted(numbers) if you want a sorted copy returned."
)

# ── Statement 6 ──────────────────────────────────────────
ask(
    statement   = 'items = []\n  len(items) == 0 is True.',
    correct_answer = True,
    explanation = "An empty list has length 0. len([]) == 0 → True.\n"
                  "  You can check if a list is empty with: if not items:"
)

# ── Statement 7 ──────────────────────────────────────────
ask(
    statement   = 'colors = ["Red", "Blue", "Red", "Green"]\n'
                  '  "Red" in colors gives True.',
    correct_answer = True,
    explanation = '"in" checks whether the VALUE exists anywhere in the list.\n'
                  '  It returns True as soon as it finds one match — does not count all.'
)

# ── Results ──────────────────────────────────────────────
print("=" * 55)
print(f"  Your Score: {score} / 7")

if score == 7:
    print("  🏆 Perfect! You think like a Python expert!")
elif score >= 5:
    print("  🌟 Very strong! A few assumptions to revisit.")
elif score >= 3:
    print("  👍 Good start! Review the explanations above.")
else:
    print("  💪 Keep questioning — that's what critical thinkers do!")

print("=" * 55)
print()

# ════════════════════════════════════════════════════════
#  VERIFY IN CODE — Run these yourself!
# ════════════════════════════════════════════════════════
#
#  fruits = ["Mango", "Apple", "Banana"]
#  # print(fruits[3])          → IndexError
#  print(fruits[-1])            → "Banana"
#
#  a = [1, 2, 3]
#  b = a
#  b.append(4)
#  print(a)                     → [1, 2, 3, 4]  ← a changed too!
#
#  numbers = [4, 2, 7, 1]
#  result = numbers.sort()
#  print(result)                → None
#  print(numbers)               → [1, 2, 4, 7]  ← sorted in place
#
#  A critical thinker ALWAYS tests before believing!
# ════════════════════════════════════════════════════════
