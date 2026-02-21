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
    item = input("Enter an item, or 'view' to see your cart, or 'checkout' to finish. ")

    if item == "view":
        for key, value in grocery_items.items():
            print(key, value)

    if item == "checkout":
        for key, value in grocery_items:
            print(key, value)
            print("Thank you for shopping with us!")
            break

    else:
        number_of_items = input("How many? ")
        grocery_items[item] = number_of_items