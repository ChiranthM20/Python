# Let’s ask the user for a PIN until they enter the correct one:

pin =""
correct_pin = "1234"

while pin!=correct_pin:
    pin = input("Enter the pin :")
    if pin!=correct_pin:
        print("Wrong pin, please try again")
        continue
    print("Pin Correct")

