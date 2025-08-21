class Calc:
    def add(self, a, b, c=0):
        return a+b+c  # works for both 2 parameter and 3 parameter 
    
A = Calc()
print(A.add(10,10)) 

print(A.add(20,5,8))


