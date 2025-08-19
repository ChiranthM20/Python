def calc(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mult():
        print(a*b)
    
    add()
    mult()
    sub()

calc(10,20)