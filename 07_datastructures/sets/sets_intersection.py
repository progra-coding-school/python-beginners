'''
What is Intersection:
Returns elements that exist in both sets.
It returns the common elements exists in both sets.
'''

#Using & operator

first={1,2,3,4,5}
second={4,5,6}
print(first & second)



#using intersection() method
fruits_a={"apple","orange","grapes","banana"}
fruits_b={"guava", "banana","Pomegranate"}

fruits=fruits_a.intersection(fruits_b)
print(fruits)
