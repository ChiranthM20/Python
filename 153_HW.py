'''Append Marks

Ask for student name and marks.
Append the info to marks.txt in this format: Ravi - 85'''

with open("append.txt", "a") as file:
    for i in range(3):
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        print(f"{name} - {marks}")
        file.write(f"{name} - {marks}\n")
