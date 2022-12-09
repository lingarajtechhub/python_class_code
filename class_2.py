class Sum:
    "This is a sum of two variables in python"
    a=0
    b=0
    count=0 #class variable or static variable
    def __init__(self):#calling by-default
        print("hello")
        Sum.count+=1
    
    def __str__(self):
        return "({0}  {1})".format(self.a,self.b)

    def sum(self,x,y):
        z = 6 #local variable
        self.a=x
        self.b=y
        z = z+1 #increment
        print("z= ",z)

    def show_result(self):
        print("Sum= ",self.a+self.b)
   
S = Sum()
S.sum(2,3)
print(str(S))
S.show_result()
print("Count= ",Sum.count)

S2 = Sum()
S2.sum(3,4)
S2.show_result()
print("Count= ",Sum.count)

S3 = Sum()
S3.sum(4,5)
S3.show_result()
print("Count= ",Sum.count)

print(Sum.__doc__)#To access the class strings


print(hasattr(S,'a'))#F
print(setattr(S, 'c', 6))#
print(hasattr(S,'c'))#T
print(getattr(S,'c'))#6
print(delattr(S,'c'))#
print(hasattr(S,'c'))#F

print(Sum.__dict__)
print(Sum.__name__)
print(Sum.__module__)
print(Sum.__bases__)
