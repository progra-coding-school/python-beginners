# Program Code: LIST-CT-01
# Title: Spot the Bug — Find What's Wrong in the List Code!
# Cognitive Skill: Critical Thinking (Bug identification)
# Topic: Lists in Python
#
# Problem Statement:
#   Sometimes code LOOKS right but has a hidden mistake — a bug.
#   A great programmer does not just write code; they READ code
#   carefully and spot what will go wrong BEFORE running it.
#   In this activity, you will see buggy code, understand the error,
#   and then see the FIXED version run successfully.
#
# Solution:
#   Work through 5 buggy code snippets. For each:
#     - Study the code
#     - Think: what is wrong?
#     - Press ENTER to see the bug explanation
#     - See the fixed code run live
#   A final summary table recaps all 5 bugs.
#
# Reflection:
#   1. Which bug type was hardest to spot just by reading the code?
#   2. What habit can you build to avoid IndexError in your own programs?
#   3. What is the difference between remove() and pop()? When would you use each?
#   4. Why is it important to understand error messages instead of ignoring them?

import time

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line(char="─", length=60):
    print(char * length)

def slow_print(text, delay=0.04):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def show_header():
    print_line("═")
    slow_print("  LIST-CT-01 | Spot the Bug")
    slow_print("  Find What's Wrong in the List Code!")
    print_line("═")
    print()
    slow_print("  Every snippet below has a BUG hiding in it.")
    slow_print("  Read carefully, think about what will go wrong,")
    slow_print("  then press ENTER to see the bug revealed!")
    slow_print("  After each bug, you will see the FIXED code run live.")
    print()

def show_buggy_code(lines):
    print_line()
    print("  BUGGY CODE:")
    print_line()
    for line in lines:
        print(f"    {line}")
    print_line()
    print()

def show_bug_explanation(error_type, explanation_lines):
    slow_print(f"  ❌  BUG FOUND — {error_type}")
    print()
    for line in explanation_lines:
        slow_print(f"     {line}")
    print()

def show_fixed_code(lines):
    print_line()
    slow_print("  ✅  FIXED CODE:")
    print_line()
    for line in lines:
        print(f"    {line}")
    print_line()

def run_fixed(title, func):
    print()
    slow_print(f"  Running fixed code for '{title}'...")
    time.sleep(0.4)
    print_line("·")
    func()
    print_line("·")
    print()

def pause(msg="  Press ENTER to reveal the bug..."):
    input(f"\n{msg}\n")

# ─────────────────────────────────────────────
#  BUG TRACKER — collects summary
# ─────────────────────────────────────────────

bug_summary = []   # list of (bug_num, error_type, one_line_fix)

# ─────────────────────────────────────────────
#  BUG 1 — IndexError
# ─────────────────────────────────────────────

def bug_1():
    print_line("═")
    slow_print("  BUG 1 — Aarav Tries to Access a Student Who Does Not Exist")
    print_line("═")
    print()

    buggy = [
        'students = ["Aarav", "Diya", "Kabir", "Riya", "Arjun"]',
        'print(students[5])   # trying to get the 6th student',
    ]
    show_buggy_code(buggy)
    slow_print("  Aarav has 5 students in his list. He wants the 6th.")
    slow_print("  Can you spot what will go wrong?")
    pause()

    show_bug_explanation(
        "IndexError — Accessing an index that does not exist",
        [
            "The list has 5 items, so valid indices are 0, 1, 2, 3, 4.",
            "students[5] asks for the 6th item — but there is no 6th item!",
            "Python will crash with: IndexError: list index out of range",
            "RULE: For a list of n items, the last valid index is n-1.",
            "Here n=5, so the last valid index is 4.",
        ]
    )

    fixed = [
        'students = ["Aarav", "Diya", "Kabir", "Riya", "Arjun"]',
        'print(students[4])   # FIX: last valid index is 4 (len - 1)',
    ]
    show_fixed_code(fixed)
    run_fixed("Bug 1", lambda: print(["Aarav", "Diya", "Kabir", "Riya", "Arjun"][4]))
    bug_summary.append((1, "IndexError", "Use index 4 (last valid), not 5"))

# ─────────────────────────────────────────────
#  BUG 2 — ValueError: remove() item not in list
# ─────────────────────────────────────────────

def bug_2():
    print_line("═")
    slow_print("  BUG 2 — Diya Tries to Remove Something That Is Not There")
    print_line("═")
    print()

    buggy = [
        'fruits = ["mango", "banana", "apple"]',
        'fruits.remove("guava")   # guava is not in the list!',
        'print(fruits)',
    ]
    show_buggy_code(buggy)
    slow_print("  Diya wants to remove 'guava' from her fruit list.")
    slow_print("  But is 'guava' actually in the list?")
    pause()

    show_bug_explanation(
        "ValueError — remove() called on an item not in the list",
        [
            "remove() searches the list for the item and deletes it.",
            "'guava' is NOT in ['mango', 'banana', 'apple'].",
            "Python will crash with: ValueError: list.remove(x): x not in list",
            "FIX 1: Check with 'in' before removing.",
            "FIX 2: Remove something that actually exists in the list.",
        ]
    )

    fixed = [
        'fruits = ["mango", "banana", "apple"]',
        'if "guava" in fruits:',
        '    fruits.remove("guava")',
        'else:',
        '    print("guava is not in the list — nothing removed")',
        'print(fruits)',
    ]
    show_fixed_code(fixed)

    def run_fixed_2():
        fruits = ["mango", "banana", "apple"]
        if "guava" in fruits:
            fruits.remove("guava")
        else:
            print("guava is not in the list — nothing removed")
        print(fruits)

    run_fixed("Bug 2", run_fixed_2)
    bug_summary.append((2, "ValueError", "Check 'in' list before calling remove()"))

# ─────────────────────────────────────────────
#  BUG 3 — append([list]) creates a nested list
# ─────────────────────────────────────────────

def bug_3():
    print_line("═")
    slow_print("  BUG 3 — Kabir Accidentally Creates a List Inside a List")
    print_line("═")
    print()

    buggy = [
        'team = ["Aarav", "Diya"]',
        'new_players = ["Kabir", "Riya"]',
        'team.append(new_players)    # trying to add all new players',
        'print(team)',
    ]
    show_buggy_code(buggy)
    slow_print("  Kabir wants to add Kabir and Riya to the team.")
    slow_print("  He uses append(). Will team have 4 names after this?")
    pause()

    show_bug_explanation(
        "Logic Bug — append() wraps the whole list as ONE item (nested list)",
        [
            "append() adds its argument as a SINGLE item.",
            "append(['Kabir', 'Riya']) adds the WHOLE list as one element.",
            "Result: ['Aarav', 'Diya', ['Kabir', 'Riya']]  ← nested!",
            "To add multiple items individually, use extend() instead.",
            "extend() unpacks the second list and adds each item one by one.",
        ]
    )

    fixed = [
        'team = ["Aarav", "Diya"]',
        'new_players = ["Kabir", "Riya"]',
        'team.extend(new_players)    # FIX: extend adds each item separately',
        'print(team)',
    ]
    show_fixed_code(fixed)

    def run_fixed_3():
        team = ["Aarav", "Diya"]
        new_players = ["Kabir", "Riya"]
        team.extend(new_players)
        print(team)

    run_fixed("Bug 3", run_fixed_3)
    bug_summary.append((3, "Logic Bug (nested list)", "Use extend() instead of append() for lists"))

# ─────────────────────────────────────────────
#  BUG 4 — Off-by-one: range(len(list)+1)
# ─────────────────────────────────────────────

def bug_4():
    print_line("═")
    slow_print("  BUG 4 — Riya's Loop Goes One Step Too Far")
    print_line("═")
    print()

    buggy = [
        'marks = [85, 90, 78, 92, 88]',
        'for i in range(len(marks) + 1):   # off-by-one!',
        '    print(marks[i])',
    ]
    show_buggy_code(buggy)
    slow_print("  Riya wants to print all marks using their index.")
    slow_print("  Can you see what will go wrong with range(len(marks) + 1)?")
    pause()

    show_bug_explanation(
        "IndexError — Off-by-one error in loop range",
        [
            "len(marks) = 5, so range(len(marks)+1) = range(6) → 0,1,2,3,4,5",
            "Valid indices for 5 items: 0, 1, 2, 3, 4",
            "When i=5, marks[5] does not exist → IndexError!",
            "FIX: Use range(len(marks)) which gives 0,1,2,3,4 — exactly right.",
            "Better yet: use 'for mark in marks:' to avoid index altogether.",
        ]
    )

    fixed = [
        'marks = [85, 90, 78, 92, 88]',
        'for i in range(len(marks)):   # FIX: no +1',
        '    print(marks[i])',
    ]
    show_fixed_code(fixed)

    def run_fixed_4():
        marks = [85, 90, 78, 92, 88]
        for i in range(len(marks)):
            print(marks[i])

    run_fixed("Bug 4", run_fixed_4)
    bug_summary.append((4, "IndexError (off-by-one)", "Use range(len(list)), NOT range(len(list)+1)"))

# ─────────────────────────────────────────────
#  BUG 5 — Verbose == search instead of 'in'
# ─────────────────────────────────────────────

def bug_5():
    print_line("═")
    slow_print("  BUG 5 — Arjun Writes 50 Lines When 1 Would Do  [BOSS BUG]")
    print_line("═")
    print()

    buggy = [
        'cities = ["Chennai", "Mumbai", "Delhi", "Kolkata"]',
        'search = "Delhi"',
        'found = False',
        'for city in cities:',
        '    if city == search:',
        '        found = True',
        'if found:',
        '    print("City found!")',
        'else:',
        '    print("City not found.")',
    ]
    show_buggy_code(buggy)
    slow_print("  Arjun wants to check if 'Delhi' is in his list of cities.")
    slow_print("  His code works... but is there a MUCH simpler way?")
    slow_print("  (This is a bad approach bug — not a crash, but poor style)")
    pause()

    show_bug_explanation(
        "Poor Approach — Using a manual loop when 'in' keyword does it in 1 line",
        [
            "Python's 'in' keyword searches a list automatically.",
            "'Delhi' in cities returns True or False instantly.",
            "Writing a loop with a flag variable is unnecessary and harder to read.",
            "The 'in' approach is cleaner, shorter, and less likely to have bugs.",
            "Rule: When Python has a built-in tool for the job — USE IT.",
        ]
    )

    fixed = [
        'cities = ["Chennai", "Mumbai", "Delhi", "Kolkata"]',
        'search = "Delhi"',
        'if search in cities:          # FIX: use the "in" keyword',
        '    print("City found!")',
        'else:',
        '    print("City not found.")',
    ]
    show_fixed_code(fixed)

    def run_fixed_5():
        cities = ["Chennai", "Mumbai", "Delhi", "Kolkata"]
        search = "Delhi"
        if search in cities:
            print("City found!")
        else:
            print("City not found.")

    run_fixed("Bug 5", run_fixed_5)
    bug_summary.append((5, "Poor Approach (verbose search)", "Use 'item in list' instead of a manual loop"))

# ─────────────────────────────────────────────
#  SUMMARY TABLE
# ─────────────────────────────────────────────

def show_summary():
    print_line("═")
    slow_print("  SUMMARY — All 5 Bugs at a Glance")
    print_line("═")
    print()
    print(f"  {'Bug':<5} {'Error Type':<35} {'Fix'}")
    print_line()
    for num, err, fix in bug_summary:
        print(f"  {num:<5} {err:<35} {fix}")
    print_line()
    print()
    slow_print("  Great work debugging! Remember:")
    slow_print("  → Always check your index range before accessing a list.")
    slow_print("  → Check if an item exists before removing it.")
    slow_print("  → Use extend() to add multiple items, not append().")
    slow_print("  → range(len(list)) — never +1.")
    slow_print("  → Use Python's built-in 'in' for searching.")
    print()

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print_line("═")
    slow_print("  REFLECTION — Think About It")
    print_line("═")
    print()
    slow_print("  1. Which bug type was hardest to spot just by reading the code?")
    print()
    slow_print("  2. What habit can you build to AVOID IndexError in your own programs?")
    print()
    slow_print("  3. What is the difference between remove() and pop()?")
    slow_print("     When would you use each?")
    print()
    slow_print("  4. Why is it important to UNDERSTAND error messages instead")
    slow_print("     of just ignoring them or deleting lines randomly?")
    print()
    print_line("═")

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    show_header()
    input("  Press ENTER to see Bug 1...\n")

    bug_1()
    input("  Press ENTER for Bug 2...\n")

    bug_2()
    input("  Press ENTER for Bug 3...\n")

    bug_3()
    input("  Press ENTER for Bug 4...\n")

    bug_4()
    input("  Press ENTER for Bug 5 (Boss Bug)...\n")

    bug_5()

    show_summary()
    show_reflection()

main()
