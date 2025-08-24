# Grocery store

items = {
    "apple" : 20,
    "banana" : 10,
    "milk" : 25,
    "bread" : 30,
    "buiscuit" : 15
}

cart= {}

print("\n*** Grocery Store ***")
print("\nAvailable items:")

for item, value in items.items():
    print(f"{item} - {value} Rs")

print("\n1. Add items\n2. Remove items\n3. View total\n4. Exit")

while True:
    choice = int(input("\nEnter your choice : "))

    if choice == 1:
        item_name = input("Enter the item : ").lower()
        if item_name in items:
            quantity = int(input("Enter quantity : "))
            cart[item_name] = cart.get(item_name, 0) + quantity
            print(f"{quantity} {item_name}(s) added to cart")
        else:
            print("Invalid item")

    elif choice == 2:
        item_name = input("Enter the item : ").lower()
        if item_name in cart:
            qty = int(input("Enter quantity : "))
            if qty >= cart[item_name]:
                del cart[item_name]
                print(f"All {item_name}(s) removed from cart")
            else:
                cart[item_name] -= qty
                print(f"{qty} {item_name}(s) removed from the cart")
        else:
            print("Item not in cart")

    elif choice == 3:
        if not cart:
            print("Your cart is empty")
        else:
            total = 0
            print("\nItems in your cart:")
            for item_name, qty in cart.items():
                price = items[item_name] * qty 
                total += price
                print(f"{item_name} x {qty} = {price} Rs")
            print(f"Total price = {total} Rs")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")

    print(f"\nCart: {cart}")
