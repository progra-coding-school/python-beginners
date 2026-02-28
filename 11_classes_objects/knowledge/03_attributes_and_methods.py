# Program Code: CL-KN-03
# Title: Attributes and Methods
# Cognitive Skill: Knowledge
# Topic: Classes and Objects in Python

# ATTRIBUTES — data stored on an object (what it HAS)
# METHODS    — functions defined inside a class (what it CAN DO)

class Student:
    def __init__(self, name, age, grade):
        # Attributes — each object's own data
        self.name  = name
        self.age   = age
        self.grade = grade
        self.marks = {}         # starts empty

    # Method — action the object can perform
    def introduce(self):
        print(f"Hi! I am {self.name}, age {self.age}, studying in Grade {self.grade}.")

    def add_mark(self, subject, score):
        self.marks[subject] = score

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def report(self):
        print(f"--- {self.name}'s Report ---")
        for subject, score in self.marks.items():
            print(f"  {subject:<12}: {score}")
        print(f"  Average     : {self.average():.1f}")

# --- Using attributes and methods ---
print("=== Attributes ===")
s = Student("Aarav", 13, 7)
print("Name :", s.name)
print("Age  :", s.age)
print("Grade:", s.grade)

print()

print("=== Methods ===")
s.introduce()

print()

s.add_mark("Maths",   85)
s.add_mark("Science", 92)
s.add_mark("English", 78)
s.report()

print()

# --- Multiple objects, same methods ---
print("=== Multiple objects ===")
diya = Student("Diya", 12, 6)
diya.add_mark("Maths", 95)
diya.add_mark("Science", 88)
diya.introduce()
print(f"  Diya's average: {diya.average():.1f}")

print()

# --- Class attribute (shared by ALL objects) ---
print("=== Class attribute (shared) ===")
class School:
    school_name = "Progra School"   # class attribute — same for all

    def __init__(self, teacher):
        self.teacher = teacher      # instance attribute — unique per object

t1 = School("Mrs. Radha")
t2 = School("Mr. Kumar")

print(f"t1: {School.school_name} — {t1.teacher}")
print(f"t2: {School.school_name} — {t2.teacher}")

# Think:
# 1. What is the difference between an attribute and a method?
# 2. If you change School.school_name, does it affect all existing objects?
