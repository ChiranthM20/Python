'''Ask for two numbers and display sum, difference, product, quotient, and comparison result.
'''

num1 = int(input("Enter first number : "))
num2= int(input("Enter second number : "))

print(f"num 1 + num 2 is {num1 + num2}")
print(f"num 1 - num 2 is {num1 - num2}")
print(f"num 1 % num 2 is {num1 % num2}")
print(f"num 1 / num 2 is {num1 / num2}")

if num1>num2:
    print("Num 1 is grater")
elif num1<num2:
    print("Num is grater")
else:
    print("Both are equal")