# Program Code: 07-realworld-03
# Title: Attendance Tracker

# Problem:
# A teacher marks attendance for the class.
# P = Present, A = Absent
# Find how many students are present and absent.

students = ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Priya", "Arjun"]
attendance = ["P", "P", "A", "P", "A", "P", "P"]

print("--- Attendance Report ---")
for i in range(len(students)):
    status = "Present" if attendance[i] == "P" else "Absent"
    print(students[i], ":", status)

present_count = attendance.count("P")
absent_count = attendance.count("A")

print("\nTotal students:", len(students))
print("Present:", present_count)
print("Absent:", absent_count)

# List of absent students
print("\nAbsent students:")
for i in range(len(students)):
    if attendance[i] == "A":
        print(" -", students[i])
