# Program Code: CL-FC-01
# Title: Spot the Difference
# Cognitive Skill: Focus and Concentration
# Topic: Classes and Objects in Python

# Two versions of similar class code are shown.
# Find every difference — some are bugs, some are style choices.

# ─── Pair 1 ─────────────────────────────────────────────────────
print("=== Pair 1 ===")

# Version A — correct __init__
class DogA:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"  A: {self.name} says Woof!")

# Version B — missing self. on attribute
class DogB:
    def __init__(self, name):
        name = name          # Bug! Local variable, not stored on object
    def speak(self):
        try:
            print(f"  B: {self.name} says Woof!")
        except AttributeError as e:
            print(f"  B: AttributeError — {e}")

DogA("Tommy").speak()
DogB("Tommy").speak()
# Difference: A uses self.name; B uses a local variable that disappears after __init__.

print()

# ─── Pair 2 ─────────────────────────────────────────────────────
print("=== Pair 2 ===")

# Version A — instance list (correct)
class TeamA:
    def __init__(self):
        self.members = []
    def add(self, name):
        self.members.append(name)

# Version B — class list (shared — bug!)
class TeamB:
    members = []
    def add(self, name):
        self.members.append(name)

t1 = TeamA(); t2 = TeamA()
t1.add("Aarav"); t2.add("Diya")
print(f"  A: t1={t1.members}, t2={t2.members}")   # independent

b1 = TeamB(); b2 = TeamB()
b1.add("Aarav"); b2.add("Diya")
print(f"  B: b1={b1.members}, b2={b2.members}")   # both share same list!
# Difference: A initialises list in __init__ (per object). B uses class attribute (shared).

print()

# ─── Pair 3 ─────────────────────────────────────────────────────
print("=== Pair 3 ===")

class Counter:
    def __init__(self):
        self.n = 0
    def up(self):
        self.n += 1
    def value(self):
        return self.n

c = Counter()
c.up(); c.up(); c.up()

# Version A: calling the method
print("  A:", c.value())      # 3

# Version B: referencing the method object (not calling it)
print("  B:", c.value)        # <bound method ...>
# Difference: A calls value() with (). B just references the method without calling it.

print()

# ─── Pair 4 ─────────────────────────────────────────────────────
print("=== Pair 4 ===")

# Version A — with __str__
class PointA:
    def __init__(self, x, y):
        self.x = x; self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

# Version B — without __str__
class PointB:
    def __init__(self, x, y):
        self.x = x; self.y = y

print("  A:", PointA(3, 4))    # readable: (3, 4)
print("  B:", PointB(3, 4))    # memory address: <__main__.PointB object at 0x...>
# Difference: A defines __str__ for readable output. B shows raw memory address.

# Think:
# 1. In Pair 2, how would you fix TeamB so each team has its own independent list?
# 2. In Pair 3, what is the TYPE of c.value (without parentheses)?
