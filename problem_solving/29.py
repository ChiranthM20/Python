'''Problem 2:
Write a function that accepts any number of keyword arguments and prints them in key: value format.'''

def information(**info):
    for key,value in info.items():
        print(f"{key} : {value}")

information(name="Chiranth", age="19")