myself={
    "name":"Daniel",
    "age":44,
    "school":"Progra Kids Tech School"

}
#Get values by Key name
print(myself["name"])

#Update
myself["name"]="Alex"

print(myself["name"])

#Access using get method
print(myself.get("age"))

#Remove a item

myself.pop("age")

print(myself.get("age"))





