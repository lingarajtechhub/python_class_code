class A:#PARENT
    x=0

class B(A):
    y=0

class C(B):
    z=0

    def input(self):
        self.x=int(input("Enter the x: "))
        self.y=int(input("Enter the y: "))
        self.z=int(input("Enter the z: "))
    
    def output(self):
        print("x= ",self.x," y= ",self.y," z= ",self.z)

C = C()
C.input()
C.output()