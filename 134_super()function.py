class Animal:  # parent
    def make_sound(self):
        print("Animal is making sound")
        
class Dog(Animal):  # Child
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} is Barking")

    def get_angry(self):
        super().make_sound()
        
        print(f"{self.name} is Angry")

 
A=Dog("Doggy")

A.make_sound()
A.get_angry()