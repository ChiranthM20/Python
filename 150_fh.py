students = ["Chiranth", "Chiru"]

file = open("class.txt", "w")

for student in students:
    file.write(f"{student}\n")
file.close()

file1 = open("class.txt", "a")
file1.write("Check code 150")
file1.close()



# using with  --> opens and closes file
with open("class1.txt", "w") as file:
    for student in students:
        file.write(f"{student}\n")
