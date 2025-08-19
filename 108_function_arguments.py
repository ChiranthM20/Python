
# * (arguments)

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result+=num
    return result
print(total_sum(2,5,1,3,99))



# **(kwargs) --> key word arguments

def info(**info):
    for key,value in info.items():
        print(f"{key} : {value}")
info(name = "Chiranth", age = "19")

def add(*numbers):
    
    return sum(numbers)

print(add(1,44,178))







def information(**info):
    print(info)
information(name = "Chiranth", age = "19")