try:
    a = int(input("A = "))
    print(10/a)
except ZeroDivisionError:    # only catches ZeroDivisionError
    print("can't divide by zero")



