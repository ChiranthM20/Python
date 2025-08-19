'''Print numbers 1 to 10, skip 5, and stop completely at 8.

'''

for i in range(1,11):
    if i==5:
        continue
    print(i)
    if i==8:
        break

