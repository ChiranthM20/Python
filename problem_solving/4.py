'''Ask for a number and print if it's even, odd, and if it's a multiple of 5.
'''

num = int(input(" Enter a number : "))

if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
if num%5==0:
    print(f"{num} is multiple of 5")
else:
    print(f"{num} is not a multiple of 5")