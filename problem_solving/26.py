'''9. Local variable shadowing global variable
Create a variable x = 10 outside a function. Inside a function test(), 
create a local variable x = 5 and print both inside and outside the function.

'''


x = 10

def test():
    x=5
    print(x)
    

print(x)
test()