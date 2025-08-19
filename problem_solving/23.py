'''6. Local vs Global variable
Create a global variable count = 0.
Write a function increment() that increases count by 1 and prints it. Try running it without global keyword and then with it.

'''



#without global keyword --> error

count = 0

def increment():
    global count
    count+=1
    print(count)

increment()