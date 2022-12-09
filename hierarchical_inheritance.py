class A:
    x=0

class B(A):
    y=0
    
    def B_input(self):
        self.x=int(input("Enter the x: "))
        self.y=int(input("Enter the y: "))

    def B_output(self):
        print("x= ",self.x," y= ",self.y)

class C(A):
    z=0
    pass
    def C_input(self):
        self.x=int(input("Enter the x: "))
        self.z=int(input("Enter the z: "))

    def C_output(self):
        print("x= ",self.x," z= ",self.z)

class D(A):
    m=0

    def D_input(self):
        self.x=int(input("Enter the x: "))
        self.m=eval(input("Enter the m: "))
    
    def D_output(self):
        print("x= ",self.x, " m= ",self.m)

B = B()
C = C()
D = D()

B.B_input()
B.B_output()

C.C_input()
C.C_output()

D.D_input()
D.D_output()
