
# add()

fruits = {"apple", "banana", "cherry"}
fruits.add("dragon fruit")
print(fruits)

# remove()

fruits.remove("banana")
#fruits.remove("papaya")   will raise error
print(fruits)


# discard

fruits.discard("papaya")
print(fruits)

# pop()  --> pops random element

fruits.pop()
print(fruits)

# clear()
fruits.clear()
print(fruits)