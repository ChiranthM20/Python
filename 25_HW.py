'''
Logical Operator Practice: 


Write a Python program that takes two numbers as input from the user and checks if:
Both numbers are greater than 10 (using and).

'''

a= int(input("Enter first number : "))
b= int(input("Enter second number : "))

print("a>10 and b>10 -->", a>10 and b>10)


'''At least one of the numbers is less than 5 (using or).'''

print("a<5 or b<5 -->",a<5 or b<5)

'''The first number is not greater than the second (using not).'''

print("not(a>b) --> ",not(a>b))
