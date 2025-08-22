Balance = 10000

while (True):
    print("***Banking System 🏦***")
    print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
    print()

    choice = int(input("Enter your choice : "))
    print()

    
    if choice == 1:
        print("You have choosen to check your balance")
        print(f"You have {Balance} rupees in your account")

    elif choice == 2:
        print("You have choosen to Deposit Money")
        Deposit = int(input("Enter the money you need to deposit : "))
        Balance+=Deposit
        print(f"You have deposited {Deposit} rupees\nNew Balance : {Balance}")

    elif choice == 3:
        print("You have choosen to withdraw your money")
        Withdraw = int(input("Enter the money you need to with draw : "))
        print(f"You withdrew {Withdraw} rupees")
        Balance-=Withdraw
        print(f"New Balance : {Balance}")
        
    elif choice == 4:
        print("You have choosen to exit")
        print("Exitting...")
        break
    else:
        print("Invalid choice")
    print()


