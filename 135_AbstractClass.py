from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        print("Engine stafrted")

class Bike(Vehicle):
    def __init__(self,name):
        self.name = name
        

    def start_engine(self):
        print("starting engine")
        print("Bike is riding")
    
b = Bike("Royal Enfield")
print(b.name)
b.start_engine()