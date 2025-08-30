def show_result(func):
    def wrapper(a,b):
        print("result: ",end="")
        func(a,b)
    return wrapper

@show_result
def add(a,b):
    print(a+b)
@show_result
def sub(a,b):
    print(a+b)
@show_result
def mult(a,b):
    print(a+b)

add(10,20)
sub(392,249)
mult(23,2)