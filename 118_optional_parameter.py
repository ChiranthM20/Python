class Laptop:
    def __init__(self, brand, price, ram="Unknown"):
        self.brand=brand
        self.price=price
        self.ram = ram

    def show_info(self):
        print(f"Brand : {self.brand}, Price : {self.price}, Ram : {self.ram}")

A = Laptop("HP", 50000, "16GB")
B = Laptop("ASUS", 70000)     


print("1-->",A.brand)
print("2-->",B.brand)

A.show_info()
B.show_info()

print(f"{B.brand}'s Ram is {B.ram}")