'''Polymorphism:

Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area. Each class should calculate area differently based on its shape.
Create a loop to calculate areas for both Circle and Rectangle objects.'''

import math

# Base class
class Shape:
    def calculate_area(self):
        return 0  # Default behavior if not overridden

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# List of shape objects
shapes = [
    Circle(7),
    Rectangle(5, 3),
    Circle(2.5),
    Rectangle(10, 4)
]

# Loop to calculate and display areas
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.calculate_area():.2f}")