names=["Daniel","Ashrith","Adwin","Frankin","Saashwin","Arjun","Samskriti","Adyan","Viyan","Katherine","Jaden"]
ages=[44,12,12,14,14,14,15,12,10,9,14]

#View
print(names)

#Access
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print(names[7])
print(names[8])
print(names[9])
print(names[10])

#count
print(len(names))

#Update
names[0]="Daniel J"
print(names)

#insert
names.insert(0,"Alex")
print(names)

#append
names.append("Raj")
print(names)

#remove
names.remove("Raj")
print(names)