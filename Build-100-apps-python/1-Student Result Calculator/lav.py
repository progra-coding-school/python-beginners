#Students Result Calculator
#Step 1: Get the name of the student
#Step 2: Get the maths mark
#Step 3: Get the science mark
#Step 4: Get the english mark
#Step 5: Get the total mark (Using addition operator)
#Step 6: Get the average
#Step 7: Check if any of the subject is below 35 marks then its fail and grade "F"
#Step 8: Check if average >=90 means A+
#Step 9: Check if average >=80 means A
#Step 10: Check if average >=70 means B
#Step 11: Check if average >=60 means C
#Step 12: Check if average <=50 means D
#Step 13: Display the name,total, average, grade, Pass/Fail


name =input("please enter your name:")
maths_marks=int(input("please enter your maths marks"))
science_marks=int(input("please enter your science marks"))
english_marks=int(input("please enter your english marks"))


total_marks=science_marks +english_marks+maths_marks
print(total_marks)

average=total_marks/3
print(average)

if science_marks <=35 or maths_marks <=35 or english_marks  <=35:
  print("you failed!")
  print("your grade if f")
else:
  print("you pass")

  if average >= 90:
    print("your grade is a+")
  elif average  >= 80:
    print("your grade is a")
  elif average  >=70:
    print("your grade is b")
  elif average >= 60:
    print("your grade id c")
  elif average >= 50:
    print("your grade is d")
  else:
    print("your grade is f")
  Result="pass"


