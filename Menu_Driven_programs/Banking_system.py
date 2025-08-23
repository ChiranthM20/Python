Balance = 10000

while (True):
    print("\n***Banking System 🏦***")
    print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
    print()

    choice = int(input("Enter your choice : "))

    
    if choice == 1:
        print("\nYou have choosen to check your balance")
        print(f"\nYou have {Balance} rupees in your account")

    elif choice == 2:
        print("\nYou have choosen to Deposit Money")
        Deposit = int(input("\nEnter the money you need to deposit : "))
        if Deposit>0:
            Balance+=Deposit
            print(f"\nYou have deposited {Deposit} rupees\n\nNew Balance : {Balance}")
        else:
            print("\nInavalid deposit amount!")

    elif choice == 3:
        print("\nYou have choosen to withdraw your money")
        Withdraw = int(input("\nEnter the money you need to withdraw : "))
        if Withdraw>Balance:
            print("\nInsufficient Balance")
        elif Withdraw<=0:
            print("\nInvalid withdraw amount")
        else:
            Balance-=Withdraw
        print(f"\nYou withdrew {Withdraw} rupees")
        print(f"\nNew Balance : {Balance}")
        
    elif choice == 4:
        print("\nYou have choosen to exit")
        print("\nExitting...")
        break
    else:
        print("\nInvalid choice")
    


