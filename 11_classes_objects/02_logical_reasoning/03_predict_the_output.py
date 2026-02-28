# Program Code: CL-LR-03
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning
# Topic: Classes and Objects in Python

# Write your prediction on paper FIRST.
# Then run to verify.

# --- Challenge 1 ---
print("=== Challenge 1 ===")
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says Woof!")

d1 = Dog("Tommy")
d2 = Dog("Bruno")
d1.speak()
d2.speak()
d1.name = "Max"
d1.speak()
# Predict: ?
# Answers: Tommy says Woof! | Bruno says Woof! | Max says Woof!

print()

# --- Challenge 2 ---
print("=== Challenge 2 ===")
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def spend(self, cost):
        self.amount -= cost
        return self.amount

w = Wallet(100)
print(w.spend(30))
print(w.spend(20))
print(w.amount)
# Predict: ?
# Answers: 70 | 50 | 50

print()

# --- Challenge 3 ---
print("=== Challenge 3 ===")
class Counter:
    total = 0   # class attribute

    def __init__(self):
        Counter.total += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.total)
# Predict: ?
# Answer : 3  (every object creation increments the class counter)

print()

# --- Challenge 4 ---
print("=== Challenge 4 ===")
class Box:
    def __init__(self, items):
        self.items = items

    def add(self, item):
        self.items.append(item)

b1 = Box(["pen", "book"])
b2 = Box(["ruler"])
b1.add("eraser")
print(b1.items)
print(b2.items)
# Predict: ?
# Answers: ['pen', 'book', 'eraser'] | ['ruler']  — independent lists

print()

# --- Challenge 5 (tricky!) ---
print("=== Challenge 5 ===")
class Car:
    wheels = 4   # class attribute

c1 = Car()
c2 = Car()
c1.wheels = 6            # creates an INSTANCE attribute on c1
print(c1.wheels)         # 6 — instance attribute shadows class attribute
print(c2.wheels)         # 4 — class attribute unchanged
print(Car.wheels)        # 4 — class unchanged
# Predict: ?
# Answers: 6 | 4 | 4

print()

# --- Challenge 6 ---
print("=== Challenge 6 ===")
class Lamp:
    def __init__(self):
        self.on = False

    def toggle(self):
        self.on = not self.on
        return "ON" if self.on else "OFF"

l = Lamp()
print(l.toggle())
print(l.toggle())
print(l.toggle())
# Predict: ?
# Answers: ON | OFF | ON

# Think:
# 1. In Challenge 3, why does Counter.total count correctly across all objects?
# 2. In Challenge 5, what is the difference between c1.wheels and Car.wheels after c1.wheels = 6?
