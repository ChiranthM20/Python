age = int(input("Enter your age : "))
gender = input("Enter your gender : ").strip().lower()

if gender=="female":
    print("free")
else:
    if age<=5:
        print("free")
    elif age>5 and age<12:
        print("discount")
    else:
        if age>60:
            print("discount")
        else:
            print("full fair")