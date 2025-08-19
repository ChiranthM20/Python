'''Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.
'''


def average(*avg):
    return sum(avg)/len(avg)

print(average(1,4,6,8,22,677))