'''Ask the user for 5 numbers, store them in a list, and print the largest, smallest, and sum.
'''

# Ask for 5 numbers and store in a list
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find largest, smallest, and sum
largest = max(numbers)
smallest = min(numbers)
total_sum = sum(numbers)

# Display results
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of numbers:", total_sum)
