fruits = {"mango", "banana", "apple", "banana", "mango"}
print("Fruits set:", fruits)

#Get the number of items
print(len(fruits))

#add
fruits.add("guava")
print("Fruits set:", fruits)

#remove
fruits.remove("guava")
print("Fruits set:", fruits)

#remove
fruits.discard("apple")
print("Fruits set:", fruits)
fruits.remove("guava")
print("Fruits set:", fruits)