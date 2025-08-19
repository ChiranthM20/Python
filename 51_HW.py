'''Basic Dictionary Operations:

Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary.'''


cities = {
    "Bengaluru" : " Bisi Bele Bath ",
    "Mysuru" : " Mysore Pak ",
    "Mangaluru" : " Neer Dosa ",
    "Hubballi" : "Dharwad Peda ",
    "Hampi" : " Ragi Mudde "
}

print(" Cities in Karnataka and their famous dishes ")
print(cities)

cities["Udupi"]= "Masala Dosa"
print(cities)



cities["Bengaluru"] = "Chow chow bath"
print(cities)

cities.pop("Mangaluru")
print(cities)

del cities["Mysuru"]
print(cities)

print(cities.keys())
print(cities.values())

