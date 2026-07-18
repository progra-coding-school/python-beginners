print("welcome to ashrith super market")
print("list of items apple,eggs,meat,milk")
print("price of apples is 50,price of eggs is 20,price of meat is 150,price of milk is 30")
apple=50
eggs=20
meat=150
milk=30
product_1= input("plese enter product1 details")
product_price_1=int(input(f"plese enter price of{product_1}: "))
product_1_qty=int(input(f"plese enter the quantity{product_1}"))
product_1_total=product_price_1*product_1_qty
print("the total value of product 1",product_1_total)

product_2=input("plese enter product2 details")
product_price_2=int(input(f"plese enter price of{product_2}:"))
product_2_qty=int(input(f"plese enter the quantity{product_2}"))
product_2_total=product_price_2*product_2_qty
print("the total value of product 2",product_2_total)

product_3=input("plese enter product3 details")
product_price_3=int(input(f"plese enter price of{product_3}:"))
product_3_qty=int(input(f"plese enter the quantity{product_3}"))
product_3_total=product_price_3*product_3_qty
print("the total value of product 3",product_3_total)

product_4=input("plese enter product4 details")
product_price_4=int(input(f"plese enter price of{product_4}:"))
product_4_qty=int(input(f"plese enter the quantity{product_4}"))
product_4_total=product_price_4*product_4_qty
print("the total value of product 4",product_4_total)

total_product=product_1_total+product_2_total+product_3_total+product_4_total
print("the total price of all product is",total_product)
print("thanks for visiting ashrith super market plese visit again")