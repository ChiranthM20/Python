'''Inheritance:

Create a base class Vehicle with a start method. Then create a subclass Bike with an additional ride() method.
Demonstrate how the Bike can use both start and ride.
'''

class Vehicle:
    def start(self):
        print("Vehicle started")
    
class Bike(Vehicle):
    def ride(self):
        print("Bike is now riding")
    
my_bike=Bike()
my_bike.start()
my_bike.ride()