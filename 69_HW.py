'''Odd Numbers Printer:

Create a program that prints all odd numbers between 1 and 20 using a while loop.'''

i=1

while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1
    