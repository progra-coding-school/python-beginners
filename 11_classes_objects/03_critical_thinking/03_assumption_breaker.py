# Program Code: CL-CT-03
# Title: Assumption Breaker
# Cognitive Skill: Critical Thinking
# Topic: Classes and Objects in Python

# Common wrong beliefs about classes and objects.
# Run each block to BUST or CONFIRM the assumption.

# --- Assumption 1: "All objects of the same class share the same data" ---
print("=== Assumption 1: Objects share data ===")
class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog("Tommy")
d2 = Dog("Bruno")
d1.name = "Max"
print(f"d1: {d1.name}  d2: {d2.name}")
print("BUSTED: Each object has its OWN instance attributes — fully independent.\n")

# --- Assumption 2: "A class attribute is safe to use as a default mutable value" ---
print("=== Assumption 2: Class attribute list is safe as a default ===")
class Team:
    members = []    # shared list — DANGEROUS!

    def add(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()
t1.add("Aarav")
print(f"t1.members: {t1.members}")
print(f"t2.members: {t2.members}")   # also has Aarav!
print("BUSTED: Mutable class attributes are shared. Use self.members = [] in __init__.\n")

# --- Assumption 3: "self is a keyword in Python" ---
print("=== Assumption 3: 'self' is a Python keyword ===")
class Cat:
    def __init__(me, name):   # 'me' instead of 'self' — works!
        me.name = name

    def speak(me):
        print(f"  {me.name} says Meow!")

c = Cat("Whiskers")
c.speak()
print("BUSTED: 'self' is just a CONVENTION, not a keyword. Any name works — but always use 'self'.\n")

# --- Assumption 4: "You can only create one object from a class" ---
print("=== Assumption 4: Only one object per class ===")
class Lamp:
    def __init__(self, room):
        self.room = room

lamps = [Lamp(r) for r in ["Living Room", "Bedroom", "Kitchen", "Study"]]
print(f"Created {len(lamps)} Lamp objects from one class.")
for l in lamps:
    print(f"  Lamp → {l.room}")
print("BUSTED: You can create as many objects as you need from one class.\n")

# --- Assumption 5: "Methods are the same as regular functions" ---
print("=== Assumption 5: Methods and functions are the same ===")
class Greeter:
    def greet(self, name):
        print(f"  Hello, {name}!")

g = Greeter()
g.greet("Aarav")            # Python passes g as 'self' automatically
Greeter.greet(g, "Aarav")   # equivalent — self passed manually

def regular_greet(name):
    print(f"  Hi, {name}!")

regular_greet("Aarav")
print("BUSTED: Methods always receive 'self' automatically. Regular functions do not.\n")

# --- Assumption 6: "print(object) shows the object's data" ---
print("=== Assumption 6: print(object) shows useful data by default ===")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print("Without __str__:", p)   # shows memory address — not useful!

class PointNice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p2 = PointNice(3, 4)
print("With __str__   :", p2)   # readable!
print("BUSTED: Define __str__ to make print(object) show meaningful output.")

# Think:
# 1. Which assumption surprised you most? Why?
# 2. How does defining __str__ improve the developer experience?
