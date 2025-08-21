'''Encapsulation:

Create a BankAccount class with private attributes for account_number and balance.
Add methods to check balance, deposit, and withdraw funds.
Try accessing the balance directly and observe the result.'''

class BankAccount:
    def __init__(self,acc_no,bal):
        self.__acc_no=acc_no
        self.__bal=bal
    
    def check_bal(self):
        print(f"Your balance is {self.__bal}")
    
    def deposit(self, amount):
        if amount>0:
            self.__bal+=amount
            print(f"You have deposited {amount} rupees and your new balnce is {self.__bal} rupees")
        else:
            print(f"Please enter +ve numbers only")
    
    def withdraw(self, amount):
        if amount>0:
            if amount<=self.__bal:
                self.__bal-=amount
                print(f"Withdrew --> {amount}  \nnew balance --> {self.__bal} ")
            else:
                print("Insufficient funds")

acc= BankAccount(12345678,5000)

acc.check_bal()
acc.deposit(10000)
acc.withdraw(9999999)
acc.withdraw(10000)
