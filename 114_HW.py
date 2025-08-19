'''Recursive Function: Write a recursive function that calculates the sum of the first n numbers.'''

def func(num):
    if num ==1:
        return 1
    return num + func(num - 1)

print(func(19))

