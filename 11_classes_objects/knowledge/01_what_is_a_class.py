# Program Code: CL-KN-01
# Title: What Is a Class?
# Cognitive Skill: Knowledge
# Topic: Classes and Objects in Python

# A CLASS is a BLUEPRINT — a template for creating things.
# An OBJECT is a real thing created FROM that blueprint.

# Real-life analogy:
#   Class  → the DESIGN of a school ID card
#   Object → each student's ACTUAL ID card

# --- Defining a class ---
class Student:
    pass        # empty class for now

# --- Creating objects from the class ---
student1 = Student()
student2 = Student()
student3 = Student()

print("=== Creating Objects ===")
print("student1:", student1)
print("student2:", student2)
print("Are they the same object?", student1 is student2)   # False — different objects

print()

# --- Giving objects their own data (attributes) ---
print("=== Adding data to objects ===")
student1.name  = "Aarav"
student1.grade = 7

student2.name  = "Diya"
student2.grade = 6

print(f"Student 1: {student1.name}, Grade {student1.grade}")
print(f"Student 2: {student2.name}, Grade {student2.grade}")

print()

# --- More real-life analogies ---
print("=== More analogies ===")
print("Class 'Dog'    → objects: Tommy, Bruno, Max (all dogs, each different)")
print("Class 'Phone'  → objects: iPhone, Samsung, Nokia (all phones)")
print("Class 'Book'   → objects: each book in a library")
print()
print("The CLASS defines WHAT all dogs have (name, breed, age).")
print("Each OBJECT holds the actual values for ONE specific dog.")

print()

# --- Checking types ---
print("=== type() and isinstance() ===")
print("type(student1)  :", type(student1))
print("Is Student?     :", isinstance(student1, Student))

# Think:
# 1. What are 3 real-life classes (blueprints) and give 2 objects for each?
# 2. Why is a class called a "blueprint" and not the actual thing?
