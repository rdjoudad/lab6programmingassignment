"""
Shopping Cart Program
rdjoudad
Simulate a shopping cart experience using dictionary 
No starter code 
2/21/2026
"""

grocery_items = {}

print("Welcome to the store!")

while input != "checkout":
    item = input("Enter an item, or 'view' to see your cart, or 'checkout' to finish.")
    if input == "view":
        for key, value in grocery_items:
            print(key, value)
    