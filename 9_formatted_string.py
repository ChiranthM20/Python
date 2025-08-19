boy_name = input("boy's name : ")
boy_age = int(input("boy's age :"))

girl_name = input("girl's name :")
girl_age = int(input("girl's age :"))

age_differnce = boy_age - girl_age 

#normal 
print(boy_name + " loves " + girl_name + ". And their age differnce is" + str(age_differnce) )

#using formatted string
print(f"{boy_name} loves {girl_name} and their age differnce is {age_differnce}")
