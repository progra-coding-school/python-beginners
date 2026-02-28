# Program Code: CL-KN-02
# Title: Creating Objects with __init__
# Cognitive Skill: Knowledge
# Topic: Classes and Objects in Python

# __init__ is the CONSTRUCTOR — it runs automatically when an object is created.
# It sets up each object's starting data (attributes).

class Student:
    def __init__(self, name, grade, city):
        self.name  = name      # store name on this specific object
        self.grade = grade
        self.city  = city

# --- Creating objects ---
print("=== Creating Student objects ===")
s1 = Student("Aarav",   7, "Chennai")
s2 = Student("Diya",    6, "Madurai")
s3 = Student("Karthik", 8, "Coimbatore")

# --- Accessing attributes ---
print(f"s1: {s1.name}, Grade {s1.grade}, {s1.city}")
print(f"s2: {s2.name}, Grade {s2.grade}, {s2.city}")
print(f"s3: {s3.name}, Grade {s3.grade}, {s3.city}")

print()

# --- Each object is independent ---
print("=== Objects are independent ===")
s1.grade = 8          # promote Aarav
print(f"After update: s1.grade = {s1.grade}")
print(f"s2.grade unchanged : {s2.grade}")   # Diya's grade not affected

print()

# --- Creating many objects in a loop ---
print("=== Creating a class roster ===")
roster_data = [
    ("Riya",   5, "Trichy"),
    ("Ananya", 7, "Chennai"),
    ("Vivek",  8, "Madurai"),
]

roster = []
for name, grade, city in roster_data:
    roster.append(Student(name, grade, city))

for student in roster:
    print(f"  {student.name:<12} Grade {student.grade}  {student.city}")

print()

# --- Default parameter values ---
print("=== Default values in __init__ ===")
class Book:
    def __init__(self, title, author, pages=100):
        self.title  = title
        self.author = author
        self.pages  = pages

b1 = Book("Python Basics", "Progra Team")        # uses default pages
b2 = Book("Cricket Rules", "BCCI", 250)           # overrides default

print(f"b1: '{b1.title}' — {b1.pages} pages")
print(f"b2: '{b2.title}' — {b2.pages} pages")

# Think:
# 1. What happens if you create a Student object without passing all 3 arguments?
# 2. Why use __init__ instead of just setting attributes after creating the object?
