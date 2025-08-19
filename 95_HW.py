'''Student Data Task:

Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. 
Loop through the list and print each student's information.'''

student_info = [
    {
     "Name" : "Ram",
     "Age" : 20,
     "Marks" : 98
    },
    {
     "Name" : "Laxman",
     "Age" : 22,
     "Marks" : 95
    },
    {
     "Name" : "Bheem",
     "Age" : 30,
     "Marks" : 90
    }
]

for student in student_info:
    print("Name:", student["Name"])
    print("Age:", student["Age"])
    print("Marks:", student["Marks"])
    print()