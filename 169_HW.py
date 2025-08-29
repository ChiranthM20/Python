def login_required(func):
    def wrapper(*args, **kwargs):
        print("\nChecking if user is logged in...")
        func(*args, **kwargs)
    return wrapper

@login_required
def view_profile(name):
    print(f"{name}'s profile opened")


view_profile("Chiranth")
view_profile("Alice")