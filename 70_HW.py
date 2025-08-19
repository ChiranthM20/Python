'''Ticket Booking Simulation:

Write a program that simulates a bus ticket booking system. 
The bus has 8 seats. Each time a seat is booked, the available seats decrease. 
When there are no seats left, the loop stops and displays a message saying "All seats are booked."'''


seats = 8

while seats>0:
    print(f"Seats available {seats}")

    num=int(input("Enter the number of seats : "))

    if num<=0:
        print("Enter only positive numbers")
        continue

    if num>seats:
        print(f"Only {seats} are available")
        continue

    seats-=num
    print("Booked succesfully")

print("all seats are booked")
