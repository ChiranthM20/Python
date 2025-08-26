
# using "r"

file = open("file.txt", "r")
#  print(file.readlines())  --> this will print entire file in a list
print(file.readline())  # prints first line 

print(file.readline())  # prints next line


# using "w"

file_1 = open("student.txt", "w")
file_1.write("This is text file created using 'w'") # this will create a new file and adds the printed words


# using "a"

file_2 = open("student.txt", "a")
file_2.write("\nThis is added using 'a' ")


file_2.write("\n\nCheck out 147th program to understand the above lines")