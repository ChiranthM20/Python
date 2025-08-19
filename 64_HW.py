'''Write a Python program that prints numbers from 1 to 20, 
but skips printing numbers that are multiples of 4.
Use a while loop and the continue statement.'''

i = 1

while i<=20:
    
    if i%4==0:
        i+=1
        continue
    print(i)
    i+=1