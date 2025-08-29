def logger(func):
    def wrapper(a,b):
        print(f"Function '{func.__name__}' is being called")
        func(a,b)
    return wrapper

@logger
def add(a,b):
    print(a+b)

@logger
def sub(a,b):
    print(a-b)

add(13,24)
sub(984,232)