student = {
    "name":   "Alex",
    "age":    13,
    "grade":  7,
    "city":   "Chennai",
    "price":10.50,
    "is_active":True,
    "name":"Adwin"
}

#Printing the values
#print(student)

# Accessing a value — use the key inside square brackets
# dict["key"] looks up the key and returns its value
print("Name:", student["name"])     # Alex
print("Age:", student["age"])       # 13
print("Grade:", student["grade"])   # 7

#Adding new key values
student["country"]="India"
print(student)

#Check if key exist
print("age" in student)      # True
print("score" in student)    # False