'''10. Function that calls another function
Write two functions:

square(num) → returns the square of a number

sum_of_squares(a, b) → returns square(a) + square(b)'''

def square(num):
    return num**2

res = square(8)
print(res)

def sum_of_squares(a, b):
    return a**2 + b**2

res2 = sum_of_squares(2,4)
print(res2)