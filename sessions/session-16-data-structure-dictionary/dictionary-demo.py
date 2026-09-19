myself={
    "name":"Daniel",
    "age":44,
    "school":"Progra Kids Tech School",
    "role":"Teacher",
    10:"Score",
    True:"IsActive",
    12.78:"MyAvg",
    "sports":"Cricket",
    "subject":"social"
}

#Add an item
myself["month"]="September"

#Display
print(myself)

#Get values by Key name
print(myself["name"])
print(myself["age"])
print(myself["role"])
print(myself["school"])
print(myself["subject"])

#Access using get method
print(myself.get("school"))

#Remove a item
myself.pop("age")
print(myself)

#Add an item
myself["marks"]=98
print(myself)

#Update an item
myself["marks"]=80
print(myself)





