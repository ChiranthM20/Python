'''Create a File and Write

Ask user for 3 friend names.
Write them into friends.txt, one per line.'''


with open("write.txt", "w") as file:
    for i in range(3):
        name = input("Enter: ")
        file.write(f"{name}\n")