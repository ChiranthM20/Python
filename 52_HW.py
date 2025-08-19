'''Nested Dictionary Practice (Simple for now):

Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
Access and print the favorite food of one friend'''


my_friends = {
    "friend1" : {"name" : "Ram", "subject": "Maths" , "food": "Dosa"},
    "friend2" : {"name" : "Ramuu", "subject": "Science" , "food": "Chapathi"}
}

print(my_friends)

print(my_friends["friend1"]["name"])
