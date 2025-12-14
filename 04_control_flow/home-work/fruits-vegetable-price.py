# Simple program to get price of a fruit or vegetable in Indian Rupees

# Get input from the user
item = input("Enter the name of a fruit or vegetable: ").lower()

# Check item and print the price
if item == "apple":
    print("The price of an apple is ₹100 per kg.")
elif item == "banana":
    print("The price of a banana is ₹40 per dozen.")
elif item == "carrot":
    print("The price of a carrot is ₹30 per kg.")
elif item == "tomato":
    print("The price of a tomato is ₹25 per kg.")
elif item == "potato":
    print("The price of a potato is ₹20 per kg.")
else:
    print("Sorry, we don't have the price for that item.")
