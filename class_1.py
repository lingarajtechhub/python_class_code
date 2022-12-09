class Sum:
    a=0
    b=0
    def add(self):
        a=0
        b=0
        self.a=int(input("Enter the value of a: "))
        self.b=int(input("Enter the value of b: "))
    
    def show_result(self):
        print("Sum= ",self.a+self.b)
    
S = Sum() #Object 
S.add()
S.show_result()
print(type(S))
print(Sum.a)
                  