class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

s = Student("Joe", 3)
s.introduce()
