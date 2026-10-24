name = input("Hello what is your name? ")
engmarks = int(input("ok, enter your english marks please: "))
scimarks = int(input("ok, enter your science marks please: "))
mathmarks = int(input("ok, enter your math marks please: "))

totalmarks = scimarks + engmarks + mathmarks
print("Great! Your total marks are:", totalmarks)

average = totalmarks / 3
print("Your average is:", average)

# Calculate the grade
if average >= 90:
    grade = "Excellent, you got an A+"
elif average >= 80:
    grade = "Great, you got an A"
elif average >= 70:
    grade = "Good enough, you got a B"
elif average >= 60:
    grade = "Could do better, you got a C"
elif average >= 50:
    grade = "Improvement needed, you got a D"
else:
    grade = "Failing grade, you got an F"

# Calculate and store the pass/fail status in a variable
if average >= 40:
    passorfail = "PASSED"
else:
    passorfail = "FAILED"

# Final summary print statement
print(f"\n{name}, your total marks are: {totalmarks} and your average is: {average:.2f} and your grade is: {grade} and your status is: {passorfail}")

