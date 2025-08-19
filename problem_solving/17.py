'''Keep asking the user for a number between 1 and 10 until they guess the correct one.
'''

my_num = 9

guess = 0

while guess!=my_num:
    guess = int(input("Guess my number"))
    if guess!=my_num:
        print("no it is not my number")
    else:
        print("Good you guessed my number")

