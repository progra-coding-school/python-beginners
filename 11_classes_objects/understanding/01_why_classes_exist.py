# Program Code: CL-UN-01
# Title: Why Classes Exist
# Cognitive Skill: Understanding
# Topic: Classes and Objects in Python

# WITHOUT classes: functions + dicts + variables everywhere — hard to organise.
# WITH classes: data and behaviour for ONE thing stay together.

# --- Problem: track 3 students WITHOUT a class ---
print("=== WITHOUT classes — scattered data ===")

# We need 3 separate dicts + separate functions
student1 = {"name": "Aarav",   "marks": [85, 90, 78]}
student2 = {"name": "Diya",    "marks": [92, 88, 95]}
student3 = {"name": "Karthik", "marks": [70, 75, 68]}

def average(student):
    return sum(student["marks"]) / len(student["marks"])

def introduce(student):
    print(f"I am {student['name']}, avg: {average(student):.1f}")

introduce(student1)
introduce(student2)
introduce(student3)

print()
print("Problems:")
print("  1. Functions are separate from the data they work on.")
print("  2. Easy to pass wrong dict to wrong function.")
print("  3. Adding a new field ('city') means updating every dict manually.")
print("  4. Does NOT scale to 100 students.")

print()

# --- Same program WITH a class ---
print("=== WITH classes — organised and scalable ===")

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def introduce(self):
        print(f"I am {self.name}, avg: {self.average():.1f}")

students = [
    Student("Aarav",   [85, 90, 78]),
    Student("Diya",    [92, 88, 95]),
    Student("Karthik", [70, 75, 68]),
]

for s in students:
    s.introduce()

print()
print("Benefits:")
print("  1. Data and behaviour are BUNDLED inside the class.")
print("  2. Each student object manages itself — no risk of mix-ups.")
print("  3. Adding 100 more students = just Student(...) 100 times.")
print("  4. Add a new field in __init__ once — all objects get it.")

print()
print("=== 3 Reasons Classes Exist ===")
print("1. ORGANISATION — group related data and behaviour together")
print("2. REUSABILITY  — create many objects from one blueprint")
print("3. CLARITY      — code reads like real-world concepts")

# Think:
# 1. What would you need to change to add a 'city' field to the non-class version vs the class version?
# 2. Name a real app that uses objects (e.g., Instagram, Maps). What are its classes?
