'''8. Function with keyword arguments
Write a function introduce(name, age, city) and call it using keyword arguments in different orders.

'''

def introduce(name, age, city):
    print(f"Hello my name is {name}, i am {age} years old, i live in {city}")

introduce("chiranth", "19", "bengaluru")




def intro(name, age, city):
    print(name, age, city)

intro("Chiranth", "19", "Bengaluru")
intro(age = "19" , city = "Bengaluru", name = "Chiranth")