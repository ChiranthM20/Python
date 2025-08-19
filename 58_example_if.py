'''
Let's create an example based on ticket prices for a Karnataka KSRTC bus. 
If the passenger is under 5 years old, the ticket is free. 
If the passenger is between 5 and 12 years old, they get a child discount. 
If the passenger is 60 years or older, they get a senior citizen discount. 
Otherwise, they pay the full fare.'''

age = int(input("Enter your age: "))
gender = input("Enter gender (male/female): ")

if gender == "female":
    print("Free Ticket")
elif age <= 5:
    print("Free Ticket")
elif 5 < age <= 12:
    print("Child discount")
elif age > 60:
    print("Senior citizen discount")
else:
    print("Full fare")
