'''
Create a simple in-memory Database class in Python that simulates storing and retrieving key-value pairs.

 Requirements:
  The class should have a private storage (dictionary) to hold the data.
  Implement a method write(key, value) to add or update data in the storage.
  Implement a method read(key) to retrieve the value for a given key:
  If the key exists, print the stored value.
  If the key does not exist, print "DB item not available".

  Demonstrate the functionality by:
    Writing "subscribers" → "100k" into the database.
    Writing "name" → "EIK" into the database.
    Reading and displaying the value for "name".'''


class Database:
    def __init__(self):
        self.__storage={}  # private attribute

    def write(self,key,value):
        self.__storage[key] = value

    def read(self,key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("Key not found")


db = Database()
db.write("name", "age")
db.write("Chiranth", 20)

#  print(db.__storage)  here we cannot access database directcly , it gives error

# we can only access throug read

db.read("Chiranth")
db.read("Chiru")
    