signal = input("Enter the colour :")

if signal == "red":
    print("STOP🚫🚫")
elif signal == "yellow":
    print("READY👊👊")
elif signal == "green":
    print("GO💨💨")
else:
    print("Error🤖🤖")



meals = int(input("Enter the time : "))

if meals==8:
    print("Breakfast Time")
elif meals==14:
    print("Lunch time")
elif meals==17:
    print("Snacks time")
elif meals==20:
    print("Dinner time")
else:
    print("it's not a meal time")
