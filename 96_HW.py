'''Dictionary Comprehension:

Create a dictionary where the keys are Kannada cities, and the values are their populations. 
Use dictionary comprehension to filter out cities with populations below 10 lakhs.'''

cities = {
    "Bangalore" : 6000000,
    "Mangalure" : 1000000,
    "Mysore" : 5000000
}

updated_cities = {key:value for key,value in cities.items() if value>2000000}
print(updated_cities)