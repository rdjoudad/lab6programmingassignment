"""
Shopping Cart Program
rdjoudad
Simulate a shopping cart experience using dictionary 
No starter code 
2/21/2026
"""

grocery_items = {}

print("Welcome to the store!")

item = ""
while item != "checkout":
    print("Enter an item, or 'view' to see your cart, or 'checkout' to finish. ")
    item = input("What would you like? ").lower().strip()

    if item == "view":
        for key, value in grocery_items.items():
            print("-- YOUR CART --")
            print(f"{key}: {value}")
        print("---------------")
        continue

    if item == "checkout":
        print("-- CHECKOUT FINAL CART --")
        for key, value in grocery_items:
            print(f"{key}: {value}")
        print("---------------")
        print("Thank you for shopping with us!")
        break

    else:
        number_of_items = input("How many? ")
        if item in grocery_items:
            grocery_items[item] += number_of_items
        else: 
            grocery_items[item] = number_of_items
        print(f"> {number_of_items}x {item} added to the cart.")