fruits = ["apple", "banana", "mango", "orange"]
print(fruits)
fruits.append("pineapple")
print(fruits)
fruits.insert(0,"kiwi1")
print(fruits)
fruits.insert(1,"kiwi1")

print(fruits)
fruits.extend(["grape", "melon"])
print(fruits)
removed_item = fruits.pop(2)
print(f"After pop index 2 (removed {removed_item}):", fruits)

