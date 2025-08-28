day = input("Enter the day : ")

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Almost weekend")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Just a normal weekday")