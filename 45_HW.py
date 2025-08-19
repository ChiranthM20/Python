'''Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?'''


list = [1,2,3,4]
print(list)

my_tuple = tuple(list)
print(my_tuple)

my_set = set(list)
print(my_set)

# my_tuple.add(8)      gives error
my_set.add(8) 
print(my_set)

