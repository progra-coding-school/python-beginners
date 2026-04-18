# Program Code: CL-PS-01
# Title: Student Report Card Class
# Cognitive Skill: Problem Solving
# Topic: Classes and Objects in Python

# Problem:
# Build a Student class that manages marks, calculates averages,
# assigns grades, and prints a full report card.

class Student:
    PASS_MARK = 50      # class attribute — same for all students

    def __init__(self, name, grade, roll_no):
        self.name    = name
        self.grade   = grade
        self.roll_no = roll_no
        self.marks   = {}

    def add_mark(self, subject, score):
        if not (0 <= score <= 100):
            print("  Invalid score", score, "for", subject + ". Must be 0-100.")
            return
        self.marks[subject] = score

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def letter_grade(self):
        avg = self.average()
        if avg >= 90: return "A+"
        if avg >= 80: return "A"
        if avg >= 70: return "B"
        if avg >= 60: return "C"
        return "D"

    def passed_all(self):
        return all(score >= self.PASS_MARK for score in self.marks.values())

    def best_subject(self):
        if not self.marks:
            return None
        return max(self.marks, key=self.marks.get)

    def report(self):
        print()
        print("  Progra School — Report Card")
        print("  Name    :", self.name)
        print("  Grade   :", self.grade, "  Roll No:", self.roll_no)
        print("  " + "-" * 38)
        print("  Subject        Score  Status")
        print("  " + "-" * 38)
        for subject, score in self.marks.items():
            status = "PASS" if score >= self.PASS_MARK else "FAIL"
            print("  " + subject.ljust(14), str(score).rjust(5), " ", status)
        print("  " + "-" * 38)
        print("  Average  :", str(round(self.average(), 1)) + " (" + self.letter_grade() + ")")
        print("  Best     :", self.best_subject())
        result = "PROMOTED" if self.passed_all() else "NEEDS IMPROVEMENT"
        print("  Result   :", result)

# --- Demo ---
aarav = Student("Aarav", 7, 101)
aarav.add_mark("Maths",   88)
aarav.add_mark("Science", 92)
aarav.add_mark("English", 74)
aarav.add_mark("History", 82)
aarav.add_mark("Tamil",   95)
aarav.report()

diya = Student("Diya", 6, 102)
diya.add_mark("Maths",   45)    # below pass mark
diya.add_mark("Science", 88)
diya.add_mark("English", 52)
diya.add_mark("History", 150)   # invalid — rejected
diya.report()

# Think:
# 1. Why is PASS_MARK a class attribute and not an instance attribute?
# 2. How would you add a method that returns all subjects where the student failed?
