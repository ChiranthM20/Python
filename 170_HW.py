'''Create a Decorator to Log Calls

Create a decorator called log_function_call that prints function name and when it was called.
Apply it to a function like add().'''

def log_function_call(func):
    def wrapper(a,b):
        print(f"Function '{func.__name__}' is being called")
        func(a,b)
    return wrapper

@log_function_call
def add(a,b):
    print(a+b)

add(139,27)






