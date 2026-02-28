# Program Code: CL-LR-02
# Title: Pattern Detective
# Cognitive Skill: Logical Reasoning
# Topic: Classes and Objects in Python

# Spot the pattern in each class-based code block.
# Name the pattern, then complete the missing piece.

# --- Pattern 1: Accumulator object ---
print("=== Pattern 1: Accumulator ===")
class RunCounter:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, runs):
        self.total += runs
        self.count += 1

    def average(self):
        return self.total / self.count if self.count else 0

rc = RunCounter()
for runs in [45, 62, 18, 90, 33]:
    rc.add(runs)

print(f"  Total runs: {rc.total}")
print(f"  Matches   : {rc.count}")
print(f"  Average   : {rc.average():.1f}")
print("Pattern: object accumulates data over time via repeated method calls")

print()

# --- Pattern 2: Factory — class creates a collection of objects ---
print("=== Pattern 2: Creating many objects in a loop ===")
class Lamp:
    def __init__(self, room, brightness):
        self.room       = room
        self.brightness = brightness
        self.on         = False

    def toggle(self):
        self.on = not self.on

rooms      = [("Living Room", 80), ("Bedroom", 50), ("Kitchen", 100)]
lamps      = [Lamp(room, b) for room, b in rooms]

for lamp in lamps:
    lamp.toggle()   # turn all on

for lamp in lamps:
    print(f"  {lamp.room:<15} brightness={lamp.brightness}  on={lamp.on}")
print("Pattern: list comprehension creates many objects from the same class")

print()

# --- Pattern 3: Object as a data container with methods ---
print("=== Pattern 3: Data container + behaviour ===")
class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

shapes = [Rectangle(4, 6), Rectangle(5, 5), Rectangle(3, 8)]
for r in shapes:
    print(f"  {r.width}x{r.height}  area={r.area()}  square={r.is_square()}")
print("Pattern: class bundles related data + computations on that data")

print()

# --- Pattern 4: __str__ for readable output ---
print("=== Pattern 4: __str__ for readable printing ===")
class Student:
    def __init__(self, name, grade):
        self.name  = name
        self.grade = grade

    def __str__(self):
        return f"Student({self.name}, Grade {self.grade})"

s = Student("Aarav", 7)
print(s)            # calls __str__ automatically
print(str(s))       # same thing explicitly
print(f"Info: {s}") # also works in f-strings
print("Pattern: define __str__ so print(object) gives meaningful output")

# Think:
# 1. In Pattern 2, what does `not self.on` do to a boolean value?
# 2. In Pattern 4, what would print(s) show WITHOUT __str__ defined?
