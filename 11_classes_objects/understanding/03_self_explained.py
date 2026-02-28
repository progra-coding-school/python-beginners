# Program Code: CL-UN-03
# Title: Understanding `self`
# Cognitive Skill: Understanding
# Topic: Classes and Objects in Python

# `self` is the FIRST parameter of every instance method.
# It refers to the SPECIFIC OBJECT the method is called on.
# Python passes it automatically — you never write it when calling.

print("=== What is self? ===")

class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

    def bark(self):
        # 'self' here means: the specific Dog object this was called on
        print(f"  {self.name} says: Woof! I am a {self.breed}.")

    def fetch(self, item):
        print(f"  {self.name} fetches the {item}!")

tommy = Dog("Tommy", "Labrador")
bruno = Dog("Bruno", "Poodle")

tommy.bark()    # Python translates this to: Dog.bark(tommy)
bruno.bark()    # Python translates this to: Dog.bark(bruno)

print()

# --- self is just a name convention ---
print("=== self is just a convention — you could name it anything ===")

class Cat:
    def __init__(this, name):   # 'this' works too — but don't do this!
        this.name = name

    def meow(this):
        print(f"  {this.name} says: Meow!")

c = Cat("Mittens")
c.meow()
print("  (But always use 'self' — it's the Python convention everyone expects.)")

print()

# --- How Python translates method calls ---
print("=== Under the hood ===")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return round(math.pi * self.radius ** 2, 2)

c1 = Circle(5)
c2 = Circle(3)

# These two are IDENTICAL:
print("Method call    :", c1.area())
print("Direct call    :", Circle.area(c1))   # Python does this internally!

print()

# --- self lets each object manage its own data ---
print("=== self keeps objects independent ===")
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1     # modifies THIS object's count, not all counters

    def value(self):
        return self.count

a = Counter()
b = Counter()

a.increment()
a.increment()
a.increment()
b.increment()

print(f"Counter a: {a.value()}")   # 3
print(f"Counter b: {b.value()}")   # 1 — independent!

# Think:
# 1. Why does Python require `self` as the first parameter but you don't pass it when calling?
# 2. What would happen if two methods both modified self.count — would they share the same count?
