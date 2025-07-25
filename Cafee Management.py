# Menu dictionary with items and prices
menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80
}

# Greet
print("Welcome to Bunny Restaurant")
print("pizza:40\npasta:50\nburger:60\nsalad:70\ncoffee:80\n")

order_total = 0

# First item
item_1 = input("Enter the name of item you want to order: ").lower()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available!")

# Ask if another item is needed
another_order = input("Do you want to add another item? (Yes/No): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

# Final bill
print(f"The total amount of items to pay is: ₹{order_total}")