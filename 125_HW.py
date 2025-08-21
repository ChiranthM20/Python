'''Abstraction:

Design a Phone class with methods to call_contact and take_picture. Abstract away any internal processing details and focus on creating a user-friendly interface.'''


class Phone:
    def __init__(self,brand):
        self.brand=brand

    def call_contact(self,name):
        print(f"Calling {name}...")
        self.__connect_call()

    def take_picture(self):
        print(f"Opening Camera")
        self.__process_camera()
        print("Picture taken")
    
    def __connect_call(self):
        print("Connecting the call securely...")

    def __process_camera(self):
        print("Processing image with lens and sensors...")


    
my_phone = Phone("Realme")
my_phone.call_contact("Chiranth")
print()
my_phone.take_picture()

