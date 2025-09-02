# 3. Develop a Python program that uses brute force to find the first number divisible by 17 between 1 and 100.


def devby_17():
    for i in range(1,100):
        if i%17==0:
            print(f"The first number divisible by 17 is {i}")
            break
        

devby_17()