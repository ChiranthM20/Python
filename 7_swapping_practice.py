#Swap Two Variables, Write a Python program that swaps the values of two variables with and without using a third variable.


# swapping without using 3rd variable

a=10
b=20

a,b = b,a

print(a,b)


# swapping using 3rd variable

a=30
b=40

temp=a
a=b
b=temp

print(a,b)

print("a =",a,",b=",b)


