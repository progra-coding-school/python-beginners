# Program Code: CL-FC-02
# Title: Mental Flow Tracing
# Cognitive Skill: Focus and Concentration
# Topic: Classes and Objects in Python

# For each block, trace in your head WHICH object's data is used.
# Label each step: which object, which attribute, which method?

print("=== Flow Tracing Exercises ===\n")

# --- Exercise 1: Two objects, one class ---
print("Exercise 1: Trace each print — which object's name?")
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"  {self.name}: Meow")

c1 = Cat("Whiskers")
c2 = Cat("Mittens")
c1.speak()      # which cat?
c2.speak()      # which cat?
c1.name = "Luna"
c1.speak()      # what name now?
# Trace: Whiskers | Mittens | Luna

print()

# --- Exercise 2: Method modifies self step by step ---
print("Exercise 2: Trace score.points at each step")
class Score:
    def __init__(self, start=0):
        self.points = start
    def add(self, n):
        self.points += n
    def reset(self):
        self.points = 0

score = Score(10)
print(f"  After init    : {score.points}")    # 10
score.add(5)
print(f"  After add(5)  : {score.points}")    # 15
score.add(20)
print(f"  After add(20) : {score.points}")    # 35
score.reset()
print(f"  After reset() : {score.points}")    # 0
score.add(8)
print(f"  After add(8)  : {score.points}")    # 8

print()

# --- Exercise 3: Objects referencing each other ---
print("Exercise 3: Trace who borrows what")
class Book:
    def __init__(self, title):
        self.title     = title
        self.borrower  = None
    def borrow(self, member_name):
        self.borrower = member_name
    def show(self):
        who = self.borrower if self.borrower else "nobody"
        print(f"  '{self.title}' borrowed by: {who}")

b1 = Book("Python Basics")
b2 = Book("Cricket Code")
b1.borrow("Aarav")
b2.borrow("Diya")
b1.show()
b2.show()
b1.borrower = None    # returned
b1.show()
# Trace: Aarav | Diya | nobody

print()

# --- Exercise 4: Class attribute vs instance ---
print("Exercise 4: Trace class vs instance attribute")
class Lamp:
    power = "LED"   # class attribute

    def __init__(self, room):
        self.room = room

l1 = Lamp("Bedroom")
l2 = Lamp("Kitchen")
print(f"  l1.power: {l1.power}")      # LED
print(f"  l2.power: {l2.power}")      # LED
Lamp.power = "CFL"
print(f"  l1.power: {l1.power}")      # CFL — class changed
l2.power = "Incandescent"             # instance attribute on l2
print(f"  l2.power: {l2.power}")      # Incandescent — instance overrides
print(f"  Lamp.power: {Lamp.power}")  # CFL — class unchanged

# Think:
# 1. In Exercise 4, after l2.power = "Incandescent", what does Lamp.power still say?
# 2. In Exercise 3, how would you add a `return_book()` method that sets borrower to None?
