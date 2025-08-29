def decorator_name(func):
    def wrapper():
        print("\nHello!")
        func()
        print("Take care!")
    return wrapper

@decorator_name
def intro():
    print("This is Chiranth")

@decorator_name
def name():
    print("This is Chiru")

name()
intro()