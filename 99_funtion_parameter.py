def marriage(boy, girl): #parameters
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")

marriage("Ram", "Sita")  #positional arguments
print()
marriage(girl = "Sita" , boy = "Ram") # keyword arguments