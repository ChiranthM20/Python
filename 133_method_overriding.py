class Animal:  # parent
    def make_sound(self):
        print("Animal is making sound")
    

class Dog(Animal):  # Child
    def make_sound(self):
        print("Bark")

d = Dog()
d.make_sound()

A=Animal()
A.make_sound()