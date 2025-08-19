'''Ask the user for a number n and print its multiplication table from 1 * n to 10 * n.
'''

n = int(input("Enter a number"))

for i in range(1,11):
    print(f" {i} * {n} = {i*n}")
print()

