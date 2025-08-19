'''Write a Python program to create a class Laptop with the following:

A constructor (__init__) to initialize brand and price of a laptop.

A method show_info() to display the brand and price of the laptop.

Create two objects of the class with different values and display their details using the method.'''


class Laptop:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price

    def show_info(self):
        print(f"Brand : {self.brand}, Price : {self.price}")

A = Laptop("HP", 50000)
B = Laptop("ASUS", 70000)     

A.show_info()
B.show_info()