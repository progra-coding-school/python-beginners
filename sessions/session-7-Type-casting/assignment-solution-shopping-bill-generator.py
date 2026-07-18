# Shopping Bill Calculator

product1 = input("Enter Product 1 Name: ")
price1 = float(input("Enter Product 1 Price: "))
quantity1 = int(input("Enter Product 1 Quantity: "))

product2 = input("Enter Product 2 Name: ")
price2 = float(input("Enter Product 2 Price: "))
quantity2 = int(input("Enter Product 2 Quantity: "))

product3 = input("Enter Product 3 Name: ")
price3 = float(input("Enter Product 3 Price: "))
quantity3 = int(input("Enter Product 3 Quantity: "))

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

grand_total = total1 + total2 + total3

print(product1, ":", total1)
print(product2, ":", total2)
print(product3, ":", total3)
print("--------------------")
print("Grand Total:", grand_total)