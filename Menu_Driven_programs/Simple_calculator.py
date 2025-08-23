def display_menu():
    print("\n****Simple Calculator📱****")
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Modulus\n5. Quit")




while True:
    print("\n*** Calculator ***")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 5:
        print("Quitting...")
        break
    elif choice in {1, 2, 3, 4}:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print(f"{a} + {b} = {a+b}")
        elif choice == 2:
            print(f"{a} - {b} = {a-b}")
        elif choice == 3:
            print(f"{a} * {b} = {a*b}")
        elif choice == 4:
            if b == 0:
                print("Division by zero not allowed 🚫")
            else:
                print(f"{a} / {b} = {a/b}")
    else:
        print("Invalid choice 🚫")
