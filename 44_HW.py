'''Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?'''


f1 = {"apple", "banana", "cherry", "papaya", "mango"}
f2 = {"blue berry", "papaya", "mango", "orange"}

print(f1 | f2)
print(f1 & f2)
print(f1 - f2)

f1.add("kiwi")
print(f1)

# remove gives error

f2.discard("black berry")  
print(f2)