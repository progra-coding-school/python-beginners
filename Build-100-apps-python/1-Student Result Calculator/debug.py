def get_student_calculator():

 name=(input("enter your name:"))

 mathematics=int(input("enter your mathematics mark"))
 science=int(input("enter your science mark:"))
 english=int(input("enter your english mark:"))

 return name,mathematics,science,english

my_name,mathematics_mark,english_mark,science_mark=get_student_calculator()

print("my name is:",my_name)

print("my mathematics mark is:",mathematics_mark)

print("my science mark is:",science_mark)

print("my english mark is:",english_mark)

def calculate_total(mathematics_mark,english_mark,science_mark):
    total= mathematics_mark+english_mark+science_mark
    return total

total_marks=calculate_total(mathematics_mark,english_mark,science_mark)
print("my total mark is:",total_marks)