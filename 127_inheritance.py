class Family:
    def __init__(self,surname):
        self.surname=surname
    
class Child(Family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name=name

child = Child("M", "Chiranth")
print(f"{child.name} {child.surname}")