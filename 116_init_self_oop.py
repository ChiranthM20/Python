class Human:

    def __init__(self, name, age, code):
        self.name=name
        self.age=age
        self.code=code
    
    def greet(self):
        print(f"Hello {self.name} you are {self.age} years old")

    def studies(self):
        print(f"{self.name} is expert in {self.code}")

        
print()

C = Human("Chiranth", 19, "Python") 
A = Human("Alice", 30, "")

C.greet()
A.greet()

print()

C.studies()