'''Getters and Setters:

Create a class BankAccount with a private attribute balance.
Write a getter method to retrieve the balance and a setter method to update it, ensuring the balance never goes below zero.
'''

class BankAcoount:

    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
        if balance>=0:
            self.__balance=balance
        else:
            print("Error: Balance cannot be negative")


B = BankAcoount(200)
print(B.get_balance())

B.set_balance(-300)
print(B.get_balance())
