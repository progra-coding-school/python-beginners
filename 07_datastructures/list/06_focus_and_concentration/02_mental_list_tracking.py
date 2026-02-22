# Program Code: LIST-FC-02
# Title: Mental List Tracking — Follow the List in Your Head!
# Cognitive Skill: Focus & Concentration (Mental tracking)
# Topic: Lists in Python
#
# Problem Statement:
#   Every time a list operation runs, the list changes.
#   Can you hold the current state of the list in your head
#   after EACH operation — without running the code?
#   This trains the same mental skill that expert programmers
#   use when they debug code by reading it.
#
# Solution:
#   Work through 5 challenges. Each challenge starts with a list
#   and runs 2-3 operations one at a time. After EACH operation,
#   predict what the list looks like NOW. Then see if you were right
#   before moving to the next step.
#
# Reflection:
#   1. Which operation was hardest to track mentally — sort(),
#      pop(), insert(), or reverse()? Why?
#   2. When you got a step wrong, did you recover and get the
#      next step right? What does that tell you about focus?
#   3. How is tracking a list in your head like keeping score
#      of a cricket match without looking at the scoreboard?
#   4. What strategy did you use to remember the list state
#      between steps — visualising, writing, or counting?

import time

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line(char="─", length=55):
    print(char * length)

def slow_print(text, delay=0.04):
    """Print text character by character for a typewriter effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def show_header():
    print("=" * 55)
    slow_print("  LIST-FC-02 | Mental List Tracking")
    slow_print("  Follow the List in Your Head!")
    print("=" * 55)
    print()
    slow_print("  Welcome, young programmer!")
    slow_print("  You will see a list, then a series of operations.")
    slow_print("  After EACH operation, predict what the list looks like.")
    slow_print("  No running code. Just your brain! 🧠")
    print()

def show_starting_list(label, lst):
    """Display the starting list clearly."""
    print_line()
    slow_print(f"  Starting list:")
    print(f"    {label} = {lst}")
    print_line()
    print()

def show_operation(op_str):
    """Display the next operation about to happen."""
    time.sleep(0.3)
    print()
    slow_print(f"  OPERATION:  {op_str}")

def ask_prediction():
    """Ask student what the list looks like now."""
    print("  What does the list look like NOW?")
    return input("  Your prediction (e.g. [1, 2, 3]): ").strip()

def check_step(user_input, actual_list, op_explanation):
    """Check a single step prediction. Returns 1 if correct, 0 if not."""
    correct = False

    # Try eval comparison first
    try:
        parsed = eval(user_input)
        if parsed == actual_list:
            correct = True
    except Exception:
        pass

    # Fallback: loose string comparison
    if not correct:
        user_clean = user_input.replace(" ", "").lower()
        actual_clean = str(actual_list).replace(" ", "").lower()
        if user_clean == actual_clean:
            correct = True

    input("\n  Press ENTER to see the result...\n")

    if correct:
        slow_print("  ✅ Correct! Great mental tracking!")
    else:
        slow_print(f"  ❌ Not quite — here's what happened:")
        slow_print(f"     {op_explanation}")
        slow_print(f"     List is now: {actual_list}")
    print()
    time.sleep(0.4)
    return 1 if correct else 0

def show_achievement(score, total):
    print("=" * 55)
    pct = (score / total) * 100 if total > 0 else 0
    print(f"  Your Score: {score} / {total} steps correct")
    print()
    if pct == 100:
        slow_print("  🏆 Sharp eyes! You are a List Detective!")
    elif pct >= 60:
        slow_print("  ✅ Good focus! Keep training your attention.")
    else:
        slow_print("  💪 Keep practising — focus takes training!")
    print("=" * 55)

# ─────────────────────────────────────────────
#  CHALLENGES
# ─────────────────────────────────────────────

def challenge_1():
    """Simple: append then pop. 2 steps."""
    print("=" * 55)
    slow_print("  CHALLENGE 1 — Aarav's Number Box  [EASY]")
    print("=" * 55)
    print()
    slow_print("  Aarav has a simple list of numbers.")
    slow_print("  Watch it change — one step at a time!")
    print()

    lst = [1, 2, 3]
    show_starting_list("numbers", lst)

    steps_correct = 0

    # Step 1: append(4)
    show_operation("numbers.append(4)")
    slow_print("  append(4) adds the number 4 at the END of the list.")
    user = ask_prediction()
    lst.append(4)
    steps_correct += check_step(
        user, lst,
        "append(4) adds 4 at the end → [1, 2, 3, 4]"
    )

    # Step 2: pop()
    show_operation("numbers.pop()")
    slow_print("  pop() removes and returns the LAST item.")
    user = ask_prediction()
    lst.pop()
    steps_correct += check_step(
        user, lst,
        "pop() removes the last item (4) → [1, 2, 3]"
    )

    slow_print(f"  Challenge 1 complete! You got {steps_correct}/2 steps right.")
    print()
    return steps_correct

def challenge_2():
    """Medium: insert then remove. 2 steps."""
    print("=" * 55)
    slow_print("  CHALLENGE 2 — Diya's Alphabet Box  [MEDIUM]")
    print("=" * 55)
    print()
    slow_print("  Diya has a list of letters. Watch as she inserts")
    slow_print("  a new letter and then removes one. Track it!")
    print()

    lst = ["a", "b", "c"]
    show_starting_list("letters", lst)

    steps_correct = 0

    # Step 1: insert(1, "x")
    show_operation('letters.insert(1, "x")')
    slow_print('  insert(1, "x") puts "x" at INDEX 1.')
    slow_print("  Everything from index 1 onwards shifts right.")
    user = ask_prediction()
    lst.insert(1, "x")
    steps_correct += check_step(
        user, lst,
        'insert(1, "x") slides "x" into position 1 → ["a", "x", "b", "c"]'
    )

    # Step 2: remove("b")
    show_operation('letters.remove("b")')
    slow_print('  remove("b") finds the FIRST "b" and deletes it.')
    user = ask_prediction()
    lst.remove("b")
    steps_correct += check_step(
        user, lst,
        'remove("b") deletes "b" → ["a", "x", "c"]'
    )

    slow_print(f"  Challenge 2 complete! You got {steps_correct}/2 steps right.")
    print()
    return steps_correct

def challenge_3():
    """Medium: sort then pop(0). 2 steps."""
    print("=" * 55)
    slow_print("  CHALLENGE 3 — Kabir's Jumbled Scores  [MEDIUM]")
    print("=" * 55)
    print()
    slow_print("  Kabir's cricket scores are all jumbled up.")
    slow_print("  He sorts them and removes the lowest. Track it!")
    print()

    lst = [5, 3, 8, 1]
    show_starting_list("scores", lst)

    steps_correct = 0

    # Step 1: sort()
    show_operation("scores.sort()")
    slow_print("  sort() rearranges the list from SMALLEST to LARGEST.")
    user = ask_prediction()
    lst.sort()
    steps_correct += check_step(
        user, lst,
        "sort() orders smallest to largest → [1, 3, 5, 8]"
    )

    # Step 2: pop(0)
    show_operation("scores.pop(0)")
    slow_print("  pop(0) removes the item at INDEX 0 — the FIRST item.")
    slow_print("  (This is different from pop() which removes the LAST!)")
    user = ask_prediction()
    lst.pop(0)
    steps_correct += check_step(
        user, lst,
        "pop(0) removes item at index 0 (the first item) → [3, 5, 8]"
    )

    slow_print(f"  Challenge 3 complete! You got {steps_correct}/2 steps right.")
    print()
    return steps_correct

def challenge_4():
    """Hard: append, sort, pop(-1). 3 steps."""
    print("=" * 55)
    slow_print("  CHALLENGE 4 — Riya's Team List  [HARD]")
    print("=" * 55)
    print()
    slow_print("  Riya has a team list of names. She adds a member,")
    slow_print("  sorts the list alphabetically, then removes the")
    slow_print("  last name. Can you track all 3 steps?")
    print()

    lst = ["Aarav", "Diya", "Kabir"]
    show_starting_list("team", lst)

    steps_correct = 0

    # Step 1: append("Meera")
    show_operation('team.append("Meera")')
    slow_print('  append("Meera") adds "Meera" at the END.')
    user = ask_prediction()
    lst.append("Meera")
    steps_correct += check_step(
        user, lst,
        'append("Meera") adds at end → ["Aarav", "Diya", "Kabir", "Meera"]'
    )

    # Step 2: sort()
    show_operation("team.sort()")
    slow_print("  sort() on strings arranges them ALPHABETICALLY (A to Z).")
    slow_print("  Think: which name comes first in the alphabet?")
    user = ask_prediction()
    lst.sort()
    steps_correct += check_step(
        user, lst,
        f"sort() alphabetical order → {lst}"
    )

    # Step 3: pop(-1)
    show_operation("team.pop(-1)")
    slow_print("  pop(-1) removes the item at index -1.")
    slow_print("  Index -1 always means the LAST item in the list.")
    user = ask_prediction()
    lst.pop(-1)
    steps_correct += check_step(
        user, lst,
        f"pop(-1) removes last item → {lst}"
    )

    slow_print(f"  Challenge 4 complete! You got {steps_correct}/3 steps right.")
    print()
    return steps_correct

def challenge_5():
    """Hard: extend, pop(2), reverse. 3 steps."""
    print("=" * 55)
    slow_print("  CHALLENGE 5 — Aarav's Score Extender  [BOSS CHALLENGE]")
    print("=" * 55)
    print()
    slow_print("  This is the hardest challenge!")
    slow_print("  Aarav extends his score list, removes one item")
    slow_print("  from the middle, then reverses everything.")
    slow_print("  Stay focused and track every change!")
    print()

    lst = [10, 20, 30, 40, 50]
    show_starting_list("scores", lst)

    steps_correct = 0

    # Step 1: extend([60, 70])
    show_operation("scores.extend([60, 70])")
    slow_print("  extend([60, 70]) adds MULTIPLE items to the end.")
    slow_print("  It is like calling append() twice in a row.")
    user = ask_prediction()
    lst.extend([60, 70])
    steps_correct += check_step(
        user, lst,
        "extend([60, 70]) adds 60 and 70 at the end → [10, 20, 30, 40, 50, 60, 70]"
    )

    # Step 2: pop(2)
    show_operation("scores.pop(2)")
    slow_print("  pop(2) removes the item at INDEX 2.")
    slow_print("  Count from the left: index 0, 1, 2...")
    user = ask_prediction()
    lst.pop(2)
    steps_correct += check_step(
        user, lst,
        f"pop(2) removes item at index 2 → {lst}"
    )

    # Step 3: reverse()
    show_operation("scores.reverse()")
    slow_print("  reverse() flips the ENTIRE list — last becomes first,")
    slow_print("  first becomes last. Reverse the list you have NOW.")
    user = ask_prediction()
    lst.reverse()
    steps_correct += check_step(
        user, lst,
        f"reverse() flips the list → {lst}"
    )

    slow_print(f"  Challenge 5 complete! You got {steps_correct}/3 steps right.")
    print()
    return steps_correct

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print("=" * 55)
    slow_print("  REFLECTION — Think About It")
    print("=" * 55)
    print()
    slow_print("  1. Which operation was hardest to track mentally —")
    slow_print("     sort(), pop(), insert(), or reverse()? Why?")
    print()
    slow_print("  2. When you got a step wrong, did you recover and")
    slow_print("     get the next step right? What does that tell")
    slow_print("     you about how focus works?")
    print()
    slow_print("  3. How is tracking a list step by step like keeping")
    slow_print("     score of a cricket match in your head, ball by ball?")
    print()
    slow_print("  4. What strategy helped you most — visualising the")
    slow_print("     list, writing it down, or counting positions?")
    print()
    print("=" * 55)

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    show_header()
    input("  Press ENTER to start Challenge 1...\n")

    total_steps = 0
    correct_steps = 0

    # Challenge 1: 2 steps
    correct_steps += challenge_1()
    total_steps += 2
    input("  Press ENTER for Challenge 2...\n")

    # Challenge 2: 2 steps
    correct_steps += challenge_2()
    total_steps += 2
    input("  Press ENTER for Challenge 3...\n")

    # Challenge 3: 2 steps
    correct_steps += challenge_3()
    total_steps += 2
    input("  Press ENTER for Challenge 4...\n")

    # Challenge 4: 3 steps
    correct_steps += challenge_4()
    total_steps += 3
    input("  Press ENTER for Challenge 5 (Boss Challenge)...\n")

    # Challenge 5: 3 steps
    correct_steps += challenge_5()
    total_steps += 3

    # Final score across all 12 steps
    show_achievement(correct_steps, total_steps)
    show_reflection()

main()
