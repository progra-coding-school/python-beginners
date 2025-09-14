#Dictionary Demo

student = {
    "name": "Raj Kumar",
    "school":"The School for Understanding",
    "age": 15,
    "syllabus": "CBSE",
    "father-name": "Prabhu",
    "mother-name":"Rani",
    "address":"3,4th Cross Street,Periyar Nager, Chennai ",
    "name":"Daniel"
}

print(student.keys())

print(student)

#Explanation
# 1.student = {...}
# This is the dictionary assigned to the variable student.

# Key-Value Pairs
# Each line inside the {} is a key-value pair, separated by a colon :.
#Ex:"name": "Raj Kumar" → Key = "name", Value = "Raj Kumar" (string)


#Accessing Values by Key
print(student["name"])
print(student["school"])
print(student["age"])
print(student["syllabus"])

""" How it works?
---------------
student["name"]
Here, student is your dictionary.
"name" is the key you want to access.
student["name"] retrieves the value associated with that key, which in this
case is "Raj Kumar".Think of it as looking up "name" in a table of 
information about the student."""

# Updating Values

student["age"] = 16
student["school"] = "Advanced Learning School"
print(student["age"])
print(student["school"])

"""
How it works?
student → this is your dictionary.
"age" → this is the key.
= → assignment operator. It means we are changing (or adding) a value.
16 → this is the new value.
 What this line does:
It updates the value of "age" in the dictionary from 15 to 16.
If "age" didn’t already exist, this line would create a new key-value pair.
"""

"""Pop"""

student = {"name": "Alice", "age": 21}
print(student.pop("age"))   # 21
print(student)              # {'name': 'Alice'}


""" Get number of items """
print(len(student))  # 3


""" Get values """

print(student.values())
# dict_values(['Alice', 21, 'A'])


""" Get all Keys"""
print(student.keys())
# dict_keys(['name', 'age'])



""" Clear method"""
student.clear()
print(student)  # {}

"""" Iterate"""
for k in student:
    print(k)   # name, grade, etc.
