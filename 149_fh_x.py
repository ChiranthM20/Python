students = open("students.txt", "x")
students.write("This file is created using 'x'")
# only runs one time 
# if we try to run once again it tells file already exists


students1 = open("students.txt", "a")
students1.write("\nCheck code 149")