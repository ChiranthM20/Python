from currency_converter import CurrencyConverter
from datetime import date


c = CurrencyConverter()
amount = float(input("Enter the amount in USD: "))
new_amount = c.convert(amount, "USD", "INR", date = date(2025, 8,28))

print(f"Amount in INR: {new_amount}")
