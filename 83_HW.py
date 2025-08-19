'''Count Vowels in a String:

Write a program that counts how many vowels are in a given string using a for loop.'''

text = input("Enter a string : ")

vowels = "aeiouAEIOU"
count = 0 

for character in text:
    if character in vowels:
        count+=1
print("Number of vowels is ",count)