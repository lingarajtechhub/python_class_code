class A:
    def __init__(self):
        print("This is base class.")
        
class B(A):
    def __init__(self):
        print("This is child class.")
        super().__class__.__init__()

B = B()