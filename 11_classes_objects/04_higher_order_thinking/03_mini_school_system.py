# Program Code: CL-HOT-03
# Title: Mini School System
# Cognitive Skill: Higher Order Thinking
# Topic: Classes and Objects in Python

# Design challenge:
# Three classes: Student, Teacher, Classroom.
# A Classroom holds students and a teacher.
# Support: enrol, take attendance, add marks, print class report.

class Student:
    def __init__(self, name, roll_no):
        self.name     = name
        self.roll_no  = roll_no
        self.marks    = {}
        self.present  = 0
        self.total_days = 0

    def add_mark(self, subject, score):
        self.marks[subject] = score

    def average(self):
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

    def attendance_pct(self):
        if self.total_days == 0:
            return 0
        return (self.present / self.total_days) * 100

    def __str__(self):
        return f"{self.name} (Roll {self.roll_no})"


class Teacher:
    def __init__(self, name, subject):
        self.name    = name
        self.subject = subject

    def __str__(self):
        return f"Teacher {self.name} [{self.subject}]"


class Classroom:
    def __init__(self, grade, section, teacher):
        self.grade    = grade
        self.section  = section
        self.teacher  = teacher
        self.students = []

    def enrol(self, student):
        self.students.append(student)
        print(f"  Enrolled: {student}")

    def take_attendance(self, present_names):
        for s in self.students:
            s.total_days += 1
            if s.name in present_names:
                s.present += 1

    def add_marks(self, subject, scores_dict):
        """scores_dict: {student_name: score}"""
        for s in self.students:
            if s.name in scores_dict:
                s.add_mark(subject, scores_dict[s.name])

    def topper(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())

    def report(self):
        print(f"\n{'═'*50}")
        print(f"  Grade {self.grade} — Section {self.section}")
        print(f"  {self.teacher}")
        print(f"  Students: {len(self.students)}")
        print(f"{'─'*50}")
        print(f"  {'Name':<14} {'Avg':>5} {'Attend':>8} {'Grade'}")
        print(f"  {'─'*14} {'─'*5} {'─'*8} {'─'*5}")
        for s in sorted(self.students, key=lambda x: x.average(), reverse=True):
            grade = "A+" if s.average()>=90 else "A" if s.average()>=80 else "B" if s.average()>=70 else "C"
            attend = f"{s.attendance_pct():.0f}%"
            print(f"  {s.name:<14} {s.average():>5.1f} {attend:>8} {grade}")
        t = self.topper()
        print(f"{'─'*50}")
        print(f"  Topper: {t.name} ({t.average():.1f})")
        print(f"{'═'*50}")

# --- Demo ---
teacher = Teacher("Mrs. Radha", "Maths")
classroom = Classroom(7, "A", teacher)

print("=== Enrolling Students ===")
students = [
    Student("Aarav",   101),
    Student("Diya",    102),
    Student("Karthik", 103),
    Student("Riya",    104),
    Student("Ananya",  105),
]
for s in students:
    classroom.enrol(s)

print("\n=== Taking Attendance (3 days) ===")
classroom.take_attendance(["Aarav", "Diya", "Karthik", "Riya", "Ananya"])
classroom.take_attendance(["Aarav", "Diya", "Karthik"])
classroom.take_attendance(["Aarav", "Riya", "Ananya"])

print("\n=== Adding Marks ===")
classroom.add_marks("Maths",   {"Aarav":85, "Diya":92, "Karthik":78, "Riya":88, "Ananya":95})
classroom.add_marks("Science", {"Aarav":90, "Diya":85, "Karthik":82, "Riya":76, "Ananya":91})
classroom.add_marks("English", {"Aarav":74, "Diya":88, "Karthik":70, "Riya":92, "Ananya":80})

classroom.report()

# Think:
# 1. Why is Classroom a separate class and not just a list of students?
# 2. How would you add a method that finds students with attendance below 75%?
