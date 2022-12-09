class Point:
    def __init__(self, x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)

    def __mul__(self,other): #P1.__sub__(P2,P3)
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Point(x,y,z)

    def __sub__(self,other): #P1.__sub__(P2,P3)
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x,y,z)



P1 = Point(2,3,4)
P2 = Point(-1,2,5)
P3 = Point(3,2,4)
print(P1*P2*P3)

print(P1-P2-P3)