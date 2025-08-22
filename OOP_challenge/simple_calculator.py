def display_menu():
    print("****Simple Calculator📱****")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Modulus\n5. Quit")


while(True):
    display_menu()

    choice = int(input("Enter your choice: "))
    
    if choice in {1,2,3,4}:
        if choice == 1:
            print("You have choosen addition")
        elif choice == 2:
            print("You have choosen subtraction")
        elif choice == 3:
            print("You have choosen multiplication")
        elif choice == 4:
            print("You have choosen Modulus")
        elif choice == 5:
            print("You have choosen exit")

        
        a= int(input("Enter first number:"))
        b= int(input("Enter second number"))

    if choice == 1:
        print(f"a+b = {a+b}")
    elif choice == 2:
        print(f"a-b = {a-b}")
    elif choice == 3:
        print(f"a*b = {a*b}")
    elif choice == 4:
        print(f"a/b = {a/b}")
    elif choice == 5:
        print("Quitting...")
        break
    else:
        print("invalid choice🚫" )
    
    print()
