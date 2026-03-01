# Mental List Tracking – Follow the List in Your Head
# Watch each operation and predict what the list looks like at every step.

score = 0
total = 0

def check(user_input, actual, explanation):
    global score, total
    total += 1
    correct = False
    try:
        if eval(user_input) == actual:
            correct = True
    except Exception:
        if user_input.replace(" ", "") == str(actual).replace(" ", ""):
            correct = True
    if correct:
        print("  Correct!")
        score += 1
    else:
        print("  Not quite.", explanation)
        print("  List is now:", actual)
    print()

print("Type your answer as a list, e.g. [1, 2, 3]")
print()

# Challenge 1 — append then pop
print("Challenge 1:")
lst = [1, 2, 3]
print("  numbers =", lst)
print()

print("  Operation: numbers.append(4)")
u = input("  What does the list look like now? ").strip()
lst.append(4)
check(u, lst, "append(4) adds 4 at the end → [1, 2, 3, 4]")

print("  Operation: numbers.pop()")
u = input("  What does the list look like now? ").strip()
lst.pop()
check(u, lst, "pop() removes the last item → [1, 2, 3]")

# Challenge 2 — insert then remove
print("Challenge 2:")
lst = ["a", "b", "c"]
print("  letters =", lst)
print()

print('  Operation: letters.insert(1, "x")')
u = input("  What does the list look like now? ").strip()
lst.insert(1, "x")
check(u, lst, 'insert(1, "x") puts "x" at index 1 — everything from 1 onwards shifts right.')

print('  Operation: letters.remove("b")')
u = input("  What does the list look like now? ").strip()
lst.remove("b")
check(u, lst, 'remove("b") finds and deletes the first "b".')

# Challenge 3 — sort then pop(0)
print("Challenge 3:")
lst = [5, 3, 8, 1]
print("  scores =", lst)
print()

print("  Operation: scores.sort()")
u = input("  What does the list look like now? ").strip()
lst.sort()
check(u, lst, "sort() rearranges smallest to largest.")

print("  Operation: scores.pop(0)")
u = input("  What does the list look like now? ").strip()
lst.pop(0)
check(u, lst, "pop(0) removes the item at index 0 — the FIRST item (not the last!).")

# Challenge 4 — append, sort, pop(-1)
print("Challenge 4:")
lst = ["Aarav", "Diya", "Kabir"]
print("  team =", lst)
print()

print('  Operation: team.append("Meera")')
u = input("  What does the list look like now? ").strip()
lst.append("Meera")
check(u, lst, 'append("Meera") adds at the end.')

print("  Operation: team.sort()")
u = input("  What does the list look like now? ").strip()
lst.sort()
check(u, lst, "sort() arranges names alphabetically (A to Z).")

print("  Operation: team.pop(-1)")
u = input("  What does the list look like now? ").strip()
lst.pop(-1)
check(u, lst, "pop(-1) removes the LAST item — index -1 always means last.")

# Challenge 5 — extend, pop(2), reverse (Boss)
print("Challenge 5 (Boss):")
lst = [10, 20, 30, 40, 50]
print("  scores =", lst)
print()

print("  Operation: scores.extend([60, 70])")
u = input("  What does the list look like now? ").strip()
lst.extend([60, 70])
check(u, lst, "extend([60, 70]) adds 60 and 70 at the end — like two appends.")

print("  Operation: scores.pop(2)")
u = input("  What does the list look like now? ").strip()
lst.pop(2)
check(u, lst, "pop(2) removes the item at index 2 (count from left: 0, 1, 2...).")

print("  Operation: scores.reverse()")
u = input("  What does the list look like now? ").strip()
lst.reverse()
check(u, lst, "reverse() flips the entire list — last becomes first, first becomes last.")

print("Score:", score, "/", total, "steps correct")
if score == total:
    print("Perfect! You tracked every step correctly.")
elif score >= int(total * 0.6):
    print("Good focus! Keep training your mental tracking.")
else:
    print("Keep practising — it gets easier each time!")
