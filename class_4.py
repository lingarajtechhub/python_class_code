class A:#base,super,parent
    x=0

class B(A):#class B:public A// class B extends A
       #derive, sub, child
    y=0
    def input(self):
        self.x=int(input("Enter the value of x: "))
        self.y=int(input("Enter the value of y: "))
    
    def display(self):
        print("x= ",self.x," y= ",self.y)
    
B = B()
B.input()
B.display()