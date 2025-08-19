'''
Create a dictionary of 3 students (name → marks), add a new student, remove the one with lowest marks.
'''

# Initial dictionary
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90
}

# Add a new student
students["David"] = 88

# Find lowest marks
lowest_marks = min(students.values())

# Create new dictionary without the lowest marks student
students = {name: marks for name, marks in students.items() if marks != lowest_marks}

# Final dictionary
print(students)
