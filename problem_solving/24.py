'''7. Function using default and non-default parameters
Write a function calculate_price(price, tax=5) that returns the price after adding tax (percentage). Call it with and without giving tax.'''

# Function definition
def calculate_price(price, tax=5):
    final_price = price + (price * tax / 100)
    return final_price

# Calling with default tax
result1 = calculate_price(1000)
print("Price with default tax:", result1)

# Calling with custom tax
result2 = calculate_price(1000, 10)
print("Price with custom tax:", result2)
