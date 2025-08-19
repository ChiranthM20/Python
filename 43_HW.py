'''Tuuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.'''


my_tuple = ("apple", "banana", "BMW", "Audi", 5)
my_tuple2 = ("Hello", "World")

# we cannot modify the tuples

print(my_tuple)

print(my_tuple[1:3])

my_tuple2 = ("Hello", "World")
new_tuple = my_tuple + my_tuple2
print(new_tuple)
