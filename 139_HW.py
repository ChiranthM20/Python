'''Abstract Classes:

Define an abstract class Employee with an abstract method calculate_salary().
Create a subclass Manager that implements calculate_salary() based on working hours and rate per hour.'''

from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def claculate_salary(self): 
        pass

class Manager:
    def __init__(self, working_hours, rate_per_hour):
        self.working_hours = working_hours
        self.rate_per_hour = rate_per_hour

    # Implement abstract method
    def calculate_salary(self):
        salary = self.working_hours * self.rate_per_hour
        return salary


# Usage
m = Manager(160, 400)   # 160 hours, 400 per hour
print("Manager Salary:", m.calculate_salary())