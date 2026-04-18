
#Creating a Set
fruits = {"mango", "banana", "apple", "banana", "mango","mango"}
print("Fruits set:", fruits)

#Access by index does not works as set does not have an index
#print(fruits[0])

#Iterate and access the elements
for item in fruits:
    print(item)

#Length of unique values
print(len(fruits))

#Check if an element exist in a set
print( "orange" in fruits)

#Add a new items in a set
fruits.add("Grapes")
print("Fruits set:", fruits)

#Update a existing items in a set
fruits.update(["Grapes","Grapes New"])
print("Fruits set:", fruits)

#remove a existing items in a set
fruits.remove("Grapes New")
print("Fruits set:", fruits)

#Sets operation: Union
subjects1={"English","Maths","Science"}
subjects2={"Tamil","Physics","Chemistry","English"}
print(subjects1 | subjects2)

#Sets operation: Intersection
print(subjects1 & subjects2)

#Sets operation: Difference
print(subjects1 - subjects2)
