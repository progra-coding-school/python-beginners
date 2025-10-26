'''
What is Union:
Combines elements from both sets (removes duplicates).
'''

#Using | operator

first={1,2,3}
second={4,5,6}
print(first | second)

#Removes the duplicates
first={1,2,3,4}
second={3,4,5,6,1}
print(first | second)

#using union() method
fruits_a={"apple","orange","grapes"}
fruits_b={"guava", "banana","Pomegranate"}

fruits=fruits_a.union(fruits_b)
print(fruits)
