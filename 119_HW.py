'''Create a Class:

Write a class Mobile with attributes brand and price.
Create two objects of the class and display their attributes using a method.'''

class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def info(self):
        print(f"Brand : {self.brand} ---- Price : {self.price}")

A = Mobile("Realme", "30,000")
B = Mobile("Redmi", "20,000")

A.info()
B.info()
    


