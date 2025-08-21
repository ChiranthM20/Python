'''Method Overloading:

Write a class Calculator with a method multiply(). Allow it to take either two or three arguments to multiply two or three numbers.
'''

class Calculator:
    def multiply(self, a, b, c=0):
        return a*b*c
    
Multiply = Calculator()
print(Multiply.multiply(20,30))
print(Multiply.multiply(30,20,10))