'''
String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
'''

enter = input("Enter a sentence : ")

print(enter.upper())
print(enter.lower())
print(enter.replace(" ","_"))
print(enter.strip())

