'''Sum of Prices:

Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.
'''

items_price = {
    "Bat" : 1000,
    "Ball" : 70,
    "Wickets" : 2000
}

total_price=0

for price in items_price.values():
    total_price+=price
print(total_price)