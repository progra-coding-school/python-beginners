# Program Code: CL-ST-02
# Title: Naming Matters — Classes, Methods, Attributes
# Cognitive Skill: Structured Thinking
# Topic: Classes and Objects in Python

# Good naming makes class code readable and self-documenting.
# Python naming conventions everyone follows:

# ─── VERSION A: Poor naming ─────────────────────────────────────
print("=== Version A: Poor naming ===")

class s:
    def __init__(self, n, a, g):
        self.n = n
        self.a = a
        self.g = g

    def d(self):
        print(f"{self.n} - {self.a} - {self.g}")

x = s("Aarav", 13, 7)
x.d()
print("What does 's', 'n', 'a', 'g', 'd' mean? Impossible to know without reading deeply.\n")

# ─── VERSION B: Good naming ─────────────────────────────────────
print("=== Version B: Good naming ===")

class Student:
    def __init__(self, name, age, grade):
        self.name  = name
        self.age   = age
        self.grade = grade

    def display(self):
        print(f"{self.name} — Age {self.age}, Grade {self.grade}")

s = Student("Aarav", 13, 7)
s.display()
print("Immediately clear what every name means.\n")

# ─── Python naming rules for classes ────────────────────────────
print("=== Python Naming Conventions ===")
conventions = [
    ("Class names",       "PascalCase",       "Student, BankAccount, CricketPlayer"),
    ("Method names",      "snake_case",        "add_mark(), get_balance(), display()"),
    ("Attribute names",   "snake_case",        "self.total_marks, self.first_name"),
    ("Private (internal)","_leading_underscore","self._balance, self._history"),
    ("Constants",         "UPPER_SNAKE_CASE",  "PASS_MARK = 50, MAX_SCORE = 100"),
]
print(f"  {'Type':<22} {'Convention':<22} {'Example'}")
print(f"  {'─'*22} {'─'*22} {'─'*30}")
for name, convention, example in conventions:
    print(f"  {name:<22} {convention:<22} {example}")

print()

# ─── Method naming: verbs for actions ───────────────────────────
print("=== Methods should be VERBS (actions) ===")
print("  Good: deposit(), withdraw(), get_balance(), add_student(), display()")
print("  Bad : balance(), student(), report_card()")

print()

# ─── Attribute naming: nouns for data ───────────────────────────
print("=== Attributes should be NOUNS (data) ===")
print("  Good: self.balance, self.student_count, self.is_open")
print("  Bad : self.doing_balance, self.counting_students")

print()

# ─── Practice ───────────────────────────────────────────────────
print("=== Practice: What would you rename? ===")
bad_names = [
    ("class", "acct",      "→ BankAccount"),
    ("method","do_thing",  "→ withdraw() or deposit()"),
    ("attr",  "self.x",    "→ self.balance or self.amount"),
    ("method","info",      "→ display() or report()"),
    ("class", "mgr",       "→ LibraryManager"),
]
for kind, bad, good in bad_names:
    print(f"  [{kind}] '{bad}' {good}")

# Think:
# 1. Why do class names use PascalCase while method names use snake_case?
# 2. What is the purpose of the single underscore prefix on _balance?
