def get_student_details():
    name=input("Please enter your name : ")
    maths=int(input("Please enter your maths mark: "))
    science=int(input("Please enter your science marks: "))
    english=int(input("Please enter your english marks:"))
    return name,maths,science,english

my_name,maths_mark,science_mark,english_mark=get_student_details()
print("My name is : ",my_name)
print("My maths_mark is : ",maths_mark)
print("My science_mark is : ",science_mark)
print("My english_mark is : ",english_mark)

def calculate_total(maths_mark,science_mark,english_mark):
    total=maths_mark+science_mark+english_mark
    return total

total_marks=calculate_total(maths_mark,science_mark,english_mark)
print("My total marks is : ",total_marks)
