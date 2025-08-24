# Bank_System_Simulation

class Account:
    def __init__(self, id, holder_name):   # Fixed constructor
        self.id = id
        self.holder_name = holder_name
        self._balance = 0

    def check_balance(self):
        print(f"Balance : {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit successful. Updated balance: {self._balance}")
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated balance: {self._balance}")
        else:
            print("Balance is less than requested amount")

class SavingsAccount(Account):   # Inheritance
    
    def cal_interest(self):   # Fixed typo
        INTEREST_RATE = 0.05
        interest = self._balance * INTEREST_RATE
        print(f"Interest: {interest}")

class CurrentAccount(Account):   # Polymorphism
    
    def withdraw(self, amount):  
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated balance: {self._balance}")
        else:
            print("Balance is over limit")

class Bank:
    def __init__(self, name, city):   
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, id, holder_name, type):
        type = type.lower() 

        if type == "savings":
            new_account = SavingsAccount(id, holder_name)
        elif type == "current":
            new_account = CurrentAccount(id, holder_name)
        else:
            print("Invalid account type. Use 'savings' or 'current'.")
            return None

        self.__accounts[id] = new_account  
        print("✅ Account creation successful")
        return new_account
    
    def get_account(self, id):
        if id not in self.__accounts:
            print("Account not found")
            return None
        else:
            account = self.__accounts[id]
            print(f"\nID: {account.id}\nHolder Name: {account.holder_name}")
            return account


SBI = Bank("State Bank Of India", "Bangalore")

s1 = SBI.create_account("1", "Chiranth", "Savings")
c1 = SBI.create_account("2", "Chiru", "Current")

s1.deposit(1000)
c1.deposit(300)

s1.withdraw(3000)   # Should say insufficient
c1.withdraw(500)    # Should allow (with overdraft logic)

s1.cal_interest()
