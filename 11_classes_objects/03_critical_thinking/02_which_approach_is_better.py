# Program Code: CL-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking
# Topic: Classes and Objects in Python

# Two approaches solve the same problem.
# Read both, decide which is better and WHY.

# =========================================================
# Problem 1: Track 3 students' marks
# =========================================================

print("=== Problem 1: Student marks ===")

# Approach A: parallel lists
names  = ["Aarav", "Diya", "Karthik"]
marks  = [[85, 90], [92, 88], [78, 72]]
cities = ["Chennai", "Madurai", "Trichy"]

# To print Diya's average:
i = names.index("Diya")
avg_a = sum(marks[i]) / len(marks[i])
print(f"A — Diya's avg: {avg_a}")

# Approach B: class
class Student:
    def __init__(self, name, city):
        self.name  = name
        self.city  = city
        self.marks = []

    def add(self, m):
        self.marks.append(m)

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

diya = Student("Diya", "Madurai")
diya.add(92)
diya.add(88)
print(f"B — Diya's avg: {diya.average()}")

print()
print("Verdict: B is better.")
print("  A: 3 lists must stay in sync — one insert in the wrong list breaks everything.")
print("  B: all data about Diya lives on her object — impossible to desync.")

print()

# =========================================================
# Problem 2: Calculate a rectangle's area and perimeter
# =========================================================

print("=== Problem 2: Rectangle calculations ===")

# Approach A: standalone functions
def area_fn(w, h):       return w * h
def perim_fn(w, h):      return 2 * (w + h)
def is_square_fn(w, h):  return w == h

w, h = 5, 5
print(f"A — area={area_fn(w,h)}, perim={perim_fn(w,h)}, square={is_square_fn(w,h)}")

# Approach B: class
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)
    def is_square(self): return self.w == self.h

r = Rectangle(5, 5)
print(f"B — area={r.area()}, perim={r.perimeter()}, square={r.is_square()}")

print()
print("Verdict: depends on scale.")
print("  A: fine for a one-off calculation.")
print("  B: better when managing many rectangles or passing them around.")
print("  Classes shine when you need MULTIPLE instances with shared behaviour.")

print()

# =========================================================
# Problem 3: ATM — track balance
# =========================================================

print("=== Problem 3: ATM balance ===")

# Approach A: global variables + functions
balance = 1000

def deposit_a(amount):
    global balance
    balance += amount

def withdraw_a(amount):
    global balance
    if amount <= balance:
        balance -= amount

deposit_a(200)
withdraw_a(500)
print(f"A — balance: {balance}")
print("A problem: global variable — any function can corrupt it accidentally.")

# Approach B: class encapsulates the balance
class ATM:
    def __init__(self, initial):
        self._balance = initial
    def deposit(self, amt):
        self._balance += amt
    def withdraw(self, amt):
        if amt <= self._balance:
            self._balance -= amt
    @property
    def balance(self):
        return self._balance

atm = ATM(1000)
atm.deposit(200)
atm.withdraw(500)
print(f"B — balance: {atm.balance}")
print("B advantage: balance is protected — only accessible through defined methods.")

# Think:
# 1. What breaks in Approach A (Problem 1) if you insert a student into `names` but forget `marks`?
# 2. In Problem 3, what is the risk of using a global variable for the balance?
