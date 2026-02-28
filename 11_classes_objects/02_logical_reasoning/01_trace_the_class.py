# Program Code: CL-LR-01
# Title: Trace the Class
# Cognitive Skill: Logical Reasoning
# Topic: Classes and Objects in Python

# Read each block carefully.
# PREDICT the output BEFORE running it.
# Trace: which object's data is being used at each step?

# --- Trace 1: __init__ runs at creation ---
print("=== Trace 1 ===")
class Box:
    def __init__(self, label):
        print(f"  Box '{label}' created")
        self.label = label

b1 = Box("A")
b2 = Box("B")
# Predict: ?
# Actual : Box 'A' created | Box 'B' created

print()

# --- Trace 2: each object has independent attributes ---
print("=== Trace 2 ===")
class Jar:
    def __init__(self, contents, amount):
        self.contents = contents
        self.amount   = amount

j1 = Jar("cookies", 10)
j2 = Jar("sweets",   5)
j1.amount -= 3
print(j1.amount)
print(j2.amount)
# Predict: ?
# Actual : 7 | 5  (j2 unchanged)

print()

# --- Trace 3: method modifies self ---
print("=== Trace 3 ===")
class Score:
    def __init__(self):
        self.points = 0

    def add(self, n):
        self.points += n

    def show(self):
        print(f"  Points: {self.points}")

s = Score()
s.add(10)
s.add(5)
s.show()
s.add(20)
s.show()
# Predict: ?
# Actual : Points: 15 | Points: 35

print()

# --- Trace 4: class vs instance attribute ---
print("=== Trace 4 ===")
class Animal:
    category = "Living thing"

    def __init__(self, name):
        self.name = name

a1 = Animal("Dog")
a2 = Animal("Cat")
print(Animal.category)
print(a1.name)
Animal.category = "Mammal"
print(a2.category)     # changed for all
# Predict: ?
# Actual : Living thing | Dog | Mammal

print()

# --- Trace 5 (tricky!) ---
print("=== Trace 5 ===")
class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.level    = 0

    def fill(self, amount):
        self.level = min(self.level + amount, self.capacity)

    def drain(self, amount):
        self.level = max(self.level - amount, 0)

t = Tank(100)
t.fill(60)
t.fill(70)      # would exceed capacity
t.drain(20)
print(t.level)
# Predict: ?
# Actual : 80  (min(60+70,100)=100, then 100-20=80)

# Think:
# 1. In Trace 4, why does changing Animal.category affect a2.category?
# 2. In Trace 5, why use min() and max() instead of if statements?
