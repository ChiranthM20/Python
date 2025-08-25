try:
    A = input("Is coding waste of time? - ")
    if A.lower()=="yes":
        raise Exception("No! Coding is not waste of time")
except Exception as E:
    print(f"Error: {E}")
else:
    print("Correct!! Coding is not waste of time")