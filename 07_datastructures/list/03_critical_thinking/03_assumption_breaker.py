# Assumption Breaker – True or False About Lists?
# Answer True or False — test what you think you know.

score = 0


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

ask(
    'fruits = ["Mango", "Apple", "Banana"]\n  fruits[3] gives "Banana"',
    "False",
    "fruits[3] causes IndexError! Valid indices are 0, 1, 2. 'Banana' is at index 2."
)

ask(
    "A list can hold both numbers and strings at the same time.",
    "True",
    'mixed = [1, "hello", 3.14] is valid. Lists hold any type.'
)

ask(
    "numbers = [5, 3, 8, 1]\n  numbers[-1] causes an error.",
    "False",
    "numbers[-1] gives 1 — the LAST item. Negative index -1 always means last."
)

ask(
    "a = [1, 2, 3]\n  b = a\n  b.append(4) does NOT change a.",
    "False",
    "b = a is NOT a copy. Both point to the same list. Use b = a.copy() for a real copy."
)

ask(
    "numbers.sort() returns a new sorted list without changing the original.",
    "False",
    "sort() sorts IN PLACE and returns None. Use sorted(list) to get a new sorted copy."
)

ask(
    "items = []\n  len(items) == 0 is True.",
    "True",
    "An empty list has length 0. Check with: if not items:"
)

ask(
    "list.extend([1, 2]) and list.append([1, 2]) produce the same result.",
    "False",
    "extend adds 1 and 2 separately. append adds [1, 2] as ONE nested item."
)

print("Score:", score, "/ 7")
