Cricketers = {
    "Virat" : "No. 18",
    "Rohith" : "No. 45",
    "Dhoni" : "No. 7"
}

print(Cricketers)

# .get()

print("Virat --> " + Cricketers.get("Virat"))

print("Rohith --> " + Cricketers.get("Rohith" , "not found")) 

print("Jaiswal --> " + Cricketers.get("Jaiswal", " not found"))