""" AUTHOR  - PRINCE SHARMA
    DATE    - 28/4/2024 10:22 PM
    WORKING - INVENTORY SYSTEM
"""

items = {"milk" : 3.50, "bread" : 2.00, "apples" : 1.50, "rice" : 1.00, "pasta" : 1.50, "patatoes" : 2.00, "cheese" : 4.00, "bananas" : 0.60, "cereal" : 3.50, "yogurt" : 1.00, "orange juice" : 2.50, "lettuce" : 1.50, "onions" : 0.75, "butter" : 3.00, "frozen pizza" : 5.00, "avocado" : 1.50, "chips" : 3.00, "soda" : 5.00, "ice cream" : 4.00}

money = float(input("How much money do you have? $"))
total_cost = 0
chosen_items = {}

print("Items available for purchase:")
for item, price in items.items():
    print(f"{item}: ${price}")

print("Enter the items you want to buy (type 'done' when finished):")
while True:
    item = input("Item name (for exit enter exit) - ").lower()
    
    if item == 'exit':
        break
    
    if item not in items:
        print("Item not available. Please choose again.")
        continue
    
    quantity = int(input("Quantity: "))
    
    if quantity <= 0:
        print("Quantity must be a positive number.")
        continue
    
    total_cost += items[item] * quantity
    chosen_items[item] = quantity

if total_cost <= money:
    print("Items purchased successfully!")
    print("Old amount:", money)
    print("New amount:", money - total_cost)
else:
    print("Insufficient money to purchase all items.")