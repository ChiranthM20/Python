'''Add Default Parameters:

Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
Write a method that displays the details of each employee.
Create multiple Employee objects with different values for name and designation, and test the default salary behavior.'''

class Employee:
    def __init__(self, name, designation, salary="30,000"):
        self.name=name
        self.designation=designation
        self.salary=salary
    
    def display(self):
        print(f"Employee Name : {self.name} \nDesignation : {self.designation} \nSalry : {self.salary} ")

E1 = Employee("Henry", "SDE", "50K")
E2 = Employee("Bob", "FSD", "40K")
E3 = Employee("Franklin", "Front End Developer")

E1.display()
print()
E2.display()
print()
E3.display()
