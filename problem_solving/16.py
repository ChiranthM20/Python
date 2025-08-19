'''From a list of integers, create a new list of only even numbers using list comprehension.
'''

my_list = [2,1,2,3,4,5,3,2,5,87,56,2,33,557,1231]

new_list = [num for num in my_list if num % 2==0]
print(new_list)