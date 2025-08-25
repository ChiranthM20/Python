'''Age Verifier:

Ask the user for their age.
If age is valid (number), show in how many years they will be 100 years old.
Handle invalid input gracefully.'''

try:
    Age = int(input("Enter your age : "))
    print(f"You are {Age} years old")
except:
    print("Error: Enter valid number")
    Age = int(input("Enter valid number : "))
    print(f"You will become 100 years old in {100 - Age} years")
else:
    print(f"You will become 100 years old in {100 - Age} years")
