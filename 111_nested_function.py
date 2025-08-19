def outer_function(name):
    def inner_function():
        print(f"Hello {name}")
    print(f"Hi {name}")
    inner_function()

outer_function("Chiranth")
