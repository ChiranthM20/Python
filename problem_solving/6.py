'''Given " Hello Python ", remove spaces, make uppercase, and replace "PYTHON" with "WORLD".'''

word = " Hello Python "


replaced = word.replace("Python", "World")
upper = word.upper()
spaces = word.strip()
print(f"upper case--> {upper}, removed spaces--> {spaces}, replaced--> {replaced}")