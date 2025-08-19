'''Create a dictionary with three key-value pairs, update one value, and delete one key.
'''

my_dict = {
    "Key1" : "Value1",
    "Key2" : "Value2",
    "Key3" : "Value3"
}

my_dict["Key1"]="Hello"
del my_dict["Key2"]
print(my_dict)
