try:
    num = int(input("Enter a number : "))
    result = 10/num
    print("result : ",result)
except ZeroDivisionError:
    print("Cannot divede by zero")
except ValueError:
    print("enter valid number")
else:
    print("No errors")
finally:
    print("Program ended")