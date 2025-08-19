'''
Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces.
'''

enter = input(" Enter the string : ")
print("you entered "+ enter)
enter = enter.replace(" ","")
print(f" the total length of the string is : ", len(enter))