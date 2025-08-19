my_dict = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

print(my_dict)

print(my_dict["key1"])

print("key1 = " + my_dict["key1"])

my_dict1 = dict( 
    {
        "key1" : "value1",
        "key2" : "value2",
        "key3" : "value3"
    }
)
print(my_dict1)

print(my_dict1["key2"])

print(type(my_dict))
print(type(my_dict1))

print(my_dict.get("key3"))

print(my_dict.get("key4", "not found"))