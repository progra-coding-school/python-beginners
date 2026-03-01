# Assumption Breaker – True or False About Lists?
# Many beginners hold wrong beliefs about how lists work.
# This exercise challenges those beliefs — think carefully before answering!
# Each statement is designed to test a common misconception.

score = 0


# ask() handles one True/False question and updates the score automatically
def ask(statement, correct, explanation):
    global score
    print("Statement:", statement)
    ans = input("True or False? ").strip().lower()
    given = "True" if ans in ("t", "true") else "False"
    if given == correct:
        print("Correct!", explanation)
        score += 1
    else:
        print("Answer:", correct, "—", explanation)
    print()

# Statement 1: off-by-one trap — beginners often think index 3 gives the 3rd item
# But index 3 gives the FOURTH item. A 3-item list has indices 0, 1, 2 only.
ask(
    'fruits = ["Mango", "Apple", "Banana"]\n  fruits[3] gives "Banana"',
    "False",
    "fruits[3] causes IndexError! Valid indices are 0, 1, 2. 'Banana' is at index 2."
)

# Statement 2: lists can mix types — strings, numbers, booleans all in one list
# Python lists are "heterogeneous" — they do not enforce one type
ask(
    "A list can hold both numbers and strings at the same time.",
    "True",
    'mixed = [1, "hello", 3.14] is valid. Lists hold any type.'
)

# Statement 3: negative index — beginners fear it causes an error, but it is very useful
# -1 = last item, -2 = second from last, -len = first item
ask(
    "numbers = [5, 3, 8, 1]\n  numbers[-1] causes an error.",
    "False",
    "numbers[-1] gives 1 — the LAST item. Negative index -1 always means last."
)

# Statement 4: shared reference trap — the most dangerous list assumption!
# b = a does NOT copy the list. Both variables point to the SAME list in memory.
# Use b = a.copy() or b = a[:] to create a true independent copy.
ask(
    "a = [1, 2, 3]\n  b = a\n  b.append(4) does NOT change a.",
    "False",
    "b = a is NOT a copy. Both point to the same list. Use b = a.copy() for a real copy."
)

# Statement 5: sort() vs sorted() — common confusion
# sort()   → rearranges the list IN PLACE, returns None (no new list created)
# sorted() → leaves the original alone and returns a brand-new sorted list
ask(
    "numbers.sort() returns a new sorted list without changing the original.",
    "False",
    "sort() sorts IN PLACE and returns None. Use sorted(list) to get a new sorted copy."
)

# Statement 6: empty list — important for checking if a list has anything in it
# if not items:  is the Pythonic way to check for an empty list
ask(
    "items = []\n  len(items) == 0 is True.",
    "True",
    "An empty list has length 0. Check with: if not items:"
)

# Statement 7: extend vs append with a list argument — the trickiest confusion
# extend([1, 2]) → unpacks: adds 1 and 2 separately → list grows by 2
# append([1, 2]) → adds the WHOLE list as one item  → list grows by 1 (nested!)
ask(
    "list.extend([1, 2]) and list.append([1, 2]) produce the same result.",
    "False",
    "extend adds 1 and 2 separately. append adds [1, 2] as ONE nested item."
)

print("Score:", score, "/ 7")
