languages = ["Python", "Java", "c"]
dictionary = {name:len(name) for name in languages}
print(dictionary)


cities_population = {
    "Bangalore" : "99999",
    "Mangalore" : "88888",
    "Mysore" : "55555"
}

large_cities = {key:value for key,value in cities_population.items() if value>="60000"}
print(large_cities)