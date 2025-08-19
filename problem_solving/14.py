'''Create two sets of numbers and print their union, intersection, and difference (first minus second).
'''

set_1 = { 1,3,5,6,7,9,3,1,4,68,8,4,2}
set_2 = { 3,5,7,8,9,32,5,6,8,9,5,24,234,24,23,4,5,6,7}

print(f" Union --> {set_1 | set_2}")
print(f" Intersection --> {set_1 & set_2}")
print(f" differnce --> {set_1 - set_2}")