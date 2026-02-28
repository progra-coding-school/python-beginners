# Program Code: CL-UN-02
# Title: Class vs Object — Blueprint vs Instance
# Cognitive Skill: Understanding
# Topic: Classes and Objects in Python

# CLASS  = the blueprint / template (defined once)
# OBJECT = a specific instance created from the blueprint (can make many)

print("=== The Blueprint Analogy ===")
print("  Class  → ID card DESIGN (one design, used for everyone)")
print("  Object → each student's ACTUAL printed ID card")
print()

# --- The class is defined ONCE ---
class IDCard:
    school = "Progra School"   # class attribute — same for all

    def __init__(self, name, roll_no, grade):
        # instance attributes — unique per object
        self.name    = name
        self.roll_no = roll_no
        self.grade   = grade

    def display(self):
        print(f"  [{IDCard.school}]  {self.name}  |  Roll: {self.roll_no}  |  Grade {self.grade}")

# --- Many objects from the same blueprint ---
print("=== Printing ID Cards (creating objects) ===")
card1 = IDCard("Aarav",   101, 7)
card2 = IDCard("Diya",    102, 6)
card3 = IDCard("Karthik", 103, 8)

card1.display()
card2.display()
card3.display()

print()

# --- Class vs instance: what's shared vs unique ---
print("=== What is shared vs unique ===")
print(f"School name (class attr)  : {IDCard.school}")       # same for all
print(f"card1 name (instance attr): {card1.name}")           # unique to card1
print(f"card2 name (instance attr): {card2.name}")           # unique to card2

print()

# --- Changing a class attribute affects ALL objects ---
print("=== Class attribute change affects all ===")
IDCard.school = "Progra Thinkers Lab"
card1.display()
card2.display()
card3.display()

print()

# --- Changing an instance attribute affects ONLY that object ---
print("=== Instance attribute change affects only one ===")
card1.grade = 8     # Aarav promoted
card1.display()
card2.display()     # Diya unchanged

print()
print("Summary:")
print("  Class attribute  → shared across ALL objects (change class → affects all)")
print("  Instance attribute → belongs to ONE object  (change object → only that one)")

# Think:
# 1. How many times is the class IDCard defined? How many times can objects be created?
# 2. What would happen if you defined `name` as a class attribute instead of instance attribute?
