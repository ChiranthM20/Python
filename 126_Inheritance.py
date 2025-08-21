class User:
    def __init__(self, username):
        self.username=username
    
    def login(self):
        print(f"{self.username} logged in")


class Admin(User):
    def delete_user(self):
        print("Admin deleted the user")

a= Admin("Chiranth")

print(a.username)

a.login()

a.delete_user()