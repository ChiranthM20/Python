# for example doubling a list

list = [2,3,2,5,6]

dl = [num*2 for num in list]
print(dl)

dl = [num*6 for num in list]
print(dl)

dl = [num**2 for num in list]
print(dl)


l = [x for x in range(1,11)]
dl = [x*2 for x in l]

print(dl)


# to print only even numbers doubled between 1 and 20
l = [x for x in range(1,21)]
even_doubled = [x*2 for x in l if x%2==0]
print(even_doubled)