'''3. Function with default parameter
Write a function greet_user(name="Guest") that prints "Hello, <name>". If no name is given, it should print "Hello, Guest".'''

def greet_user(name="Guest"):
    print(f"Hello <{name}>")

greet_user()
greet_user("Chiranth")