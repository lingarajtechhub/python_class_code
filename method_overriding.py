class A:
    x=0

    def MyParent(self): #overridden
        print("This is Parent Class")

class B(A):
    y=0

    def MyParent(self): #overridding
        print("This is Child Class")

B = B()
B.MyParent()
