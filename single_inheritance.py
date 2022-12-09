class A:
    x=0

class B(A):
    y=0

    def input(self):
        self.x=int(input("Enter the x: "))
        self.y=int(input("Enter the y: "))
    
    def output(self):
        print("x= ",self.x," y= ",self.y)

B = B()
B.input()
B.output()