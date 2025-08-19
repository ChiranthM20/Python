'''5. Return multiple values
Write a function math_operations(a, b) that returns their sum, difference, and product. Store results in three variables and print them.'''

def math_operations(a, b):
    add = a+b
    differnce = a-b
    product = a/b
    return(add, differnce, product)


result = math_operations(33,44)
print(result)