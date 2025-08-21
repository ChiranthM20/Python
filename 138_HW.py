'''Method Overriding:

Create a parent class Shape with a method draw() that prints "Drawing shape".
Create a child class Circle that overrides draw() to print "Drawing circle".'''

class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

A = Circle()
A.draw()