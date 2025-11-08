'''
What is Difference:
Returns elements present in the first set but not in
the second.
'''

#Using - operator

first={1,2,3,4,5}
second={4,5,6}
print(first - second)

#using difference() method
fruits_a={"apple","orange","grapes"}
fruits_b={"guava", "banana","Pomegranate","apple"}

fruits=fruits_a.difference(fruits_b)
print(fruits)
