'''Search From File

Write a program that searches for a name in friends.txt
If found, print "Found!" else "Not Found!"'''
name = "chiranth"
with open("friends.txt","r") as file:
    if name + "\n" in file.readlines():
        print("Found")
    else:
        print("Not found")