fruits = ["apple", "banana", "chery", "papaya"]
cars = ["Audi", "BMW", "Benz", "Porsche"]
numbers = [1,2,3,4,5,5,]

print(fruits[2])
print(fruits[-3])


# Changing a specific element
cars[3]="swift"


# inserting element


# append()  --> inserts the element at the last

cars.append("Swift")
print(cars)

#insert()  --> inserts the element in specific index
fruits.insert(3,"Dragon fruit")
print(fruits)



# removing elements

# remove()  --> removes the first occurance of the element

letters = ["A","B","C","D","A","B","D"]
letters.remove("A")
print(letters)


# pop() --> removes the last index in index in not provided 

letters.pop(3)
print(letters)

letters.pop()
print(letters)