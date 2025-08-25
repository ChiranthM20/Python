'''Safe Divider:

Ask two numbers from the user and divide them.
Handle ZeroDivisionError and ValueError.'''

print("------------------------------")
A = int(input("Enter first number : "))
B = int(input("Enter second number : "))
print("------------------------------")
try:
    print(f"A/B = {A/B}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    print("Successful")
finally:
    print("------------------------------")
    