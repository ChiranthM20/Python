'''Method Definition:

Define a class Student with attributes name and marks.
Write a method display_info() that prints the student's name and marks.
Create multiple objects of the Student class and call the method on each.
'''

class Students:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    
    def display_info(self):
        print(f"{self.name} has got {self.marks} marks")

A = Students("Chiranth",90)
B = Students("Alice", 95)
C = Students("Bob", 100)

A.display_info()
B.display_info()
C.display_info()
