# Program Code: CL-CT-01
# Title: Spot the Bug
# Cognitive Skill: Critical Thinking
# Topic: Classes and Objects in Python

# Each block has ONE bug. Find it, explain WHY it is wrong, then fix it.

# --- Bug 1: Missing self parameter ---
print("=== Bug 1 ===")
class Greeter:
    def greet():        # Bug! Missing 'self'
        print("Hello!")

# Fix:
class GreeterFixed:
    def greet(self):
        print("Hello!")

g = GreeterFixed()
g.greet()
print("Fixed: added 'self' as first parameter\n")

# --- Bug 2: Forgetting self. when setting attributes ---
print("=== Bug 2 ===")
class Point:
    def __init__(self, x, y):
        x = x           # Bug! This creates a LOCAL variable, not self.x
        y = y           # Same bug

# Fix:
class PointFixed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = PointFixed(3, 4)
print(f"Fixed: x={p.x}, y={p.y}\n")

# --- Bug 3: Mutable class attribute shared by all objects ---
print("=== Bug 3 ===")
class Student:
    marks = []          # Bug! Shared list — ALL students share this!

    def __init__(self, name):
        self.name = name

    def add_mark(self, m):
        self.marks.append(m)   # modifies the CLASS list!

s1 = Student("Aarav")
s2 = Student("Diya")
s1.add_mark(85)
print("s1 marks:", s1.marks)
print("s2 marks:", s2.marks)   # oops — s2 also has 85!

# Fix: create a new list per object in __init__
class StudentFixed:
    def __init__(self, name):
        self.name  = name
        self.marks = []        # new list for EACH object

    def add_mark(self, m):
        self.marks.append(m)

s3 = StudentFixed("Aarav")
s4 = StudentFixed("Diya")
s3.add_mark(85)
print("s3 marks:", s3.marks)
print("s4 marks:", s4.marks, "← now empty as expected\n")

# --- Bug 4: Calling a method without () ---
print("=== Bug 4 ===")
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        import math
        return round(math.pi * self.r**2, 2)

c = Circle(5)
print(type(c.area))     # Bug! c.area without () is the METHOD OBJECT, not the result
print(c.area())         # Fix: add ()
print("Fixed: must call method with ()\n")

# --- Bug 5: Using class name instead of self inside a method ---
print("=== Bug 5 ===")
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{Dog.name} says Woof!")   # Bug! Dog.name is not defined on the class

# Fix:
class DogFixed:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says Woof!")   # use self.name

d = DogFixed("Tommy")
d.speak()

# Think:
# 1. In Bug 3, why is a mutable class attribute so dangerous?
# 2. In Bug 2, what does `x = x` actually do inside __init__?
