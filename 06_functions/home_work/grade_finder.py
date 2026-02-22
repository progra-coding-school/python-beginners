
def get_average(english, maths,science):
    average=(english+maths+science)/3
    print("Average is : ",average)
    return average

def get_grade(average):
    if average>90:
        return "Grade A++"
    elif average>80:
        return "Grade A"
    else:
        return "Grade B"

average=get_average(90,90,100)
print(average)
grade=get_grade(average)
print(grade)
