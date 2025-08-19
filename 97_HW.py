'''Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

Prints the entire matrix row by row.
Prints the sum of each row in the matrix.'''

# Example 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print each row
print("Matrix:")
for row in matrix:
    print(row)

# Print sum of each row
print("\nSum of each row:")
for row in matrix:
    row_sum = sum(row)
    print(row_sum)
