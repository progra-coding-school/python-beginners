# Create a Student Object
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(self.name, "is studying!")

student_1 = Student("Alex", "Grade 4")
student_1.study()