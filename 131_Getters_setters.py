class Human:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    def get_name(self):  # getter
        return self.__name
        
    def get_age(self):   # getter
        return self.__age
    
    def set_name(self,name):   # setter
        self.__name=name

human = Human("Chiranth", 20)
print(f"Name: {human.get_name()}")
print(f"Age: {human.get_age()}")

human = Human("Chiru", 19)
print(human.get_name())