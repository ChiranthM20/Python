a = int(input("A : "))
b = int(input("B : "))


try:
    print(a/b)          
except Exception as E:
    print(f"Error: {E}")
else:
    print("No error")
finally:
    print("program ended")
