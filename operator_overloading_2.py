print("======================addition======================")
class Point:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x,y,z)

P1 = Point(2,3,4)
P2 = Point(-1,2,5)
P3 = Point(3,2,4)
print(P1+P2+P3)

print("=========================subtraction=============================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __sub__(self,other):
        x = self.x - other.y
        y = self.y - other.y
        return Point(x,y)

P1 = Point(2,4)
P2 = Point(1,3)
print(P1 - P2)

print("==========================multiplication==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
print(P1 * P2)



print("==========================division==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __truediv__(self,other):
        x = self.x / other.x
        y = round((self.y / other.y),2)
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
print(P1 / P2)

print("=========================floordivision===========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __floordiv__(self,other):
        x = self.x // other.x
        y = self.y // other.y
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
print(P1 // P2)

print("==========================power==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __pow__(self,other):
        x = self.x ** other.x
        y = self.y ** other.y
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
print(P1 ** P2)

print("==========================modulus==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __mod__(self,other):
        x = self.x % other.x
        y = self.y % other.y
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
print(P1 % P2)

print("==========================left shift==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __lshift__(self,other):
        x = self.x << other.x
        y = self.y << other.y
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
print(P1 << P2)

print("==========================right shift==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __rshift__(self,other):
        x = self.x >> other.x
        y = self.y >> other.y
        return Point(x,y)
P1 = Point(4,9)
P2 = Point(2,3)
print(P1 >> P2)

print("==========================And==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __and__(self,other):
        x = self.x & other.x
        y = self.y & other.y
        return Point(x,y)
P1 = Point(1,0)
P2 = Point(1,1)
print(P1 & P2)

print("==========================OR==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __or__(self,other):
        x = self.x | other.x
        y = self.y | other.y
        return Point(x,y)
P1 = Point(0,0)
P2 = Point(1,0)
print(P1 | P2)

print("==========================XOR==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __xor__(self,other):
        x = self.x ^ other.x
        y = self.y ^ other.y
        return Point(x,y)
P1 = Point(0,1)
P2 = Point(1,1)
print(P1 ^ P2)

print("==========================not=========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __invert__(self):
        x = ~self.x 
        y = ~self.y  
        return Point(x,y)
P1 = Point(1,0)
print(~P1)

print("==========================less than==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __lt__(self,other):
        x = self.x < other.x
        y = self.y < other.y
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
if(P1 < P2):
    print("P1 is less than P2")
else:
    print("P1 is greater than P2")


print("==========================greater than==========================")

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __gt__(self,other):
        x = self.x < other.x
        y = self.y < other.y
        return Point(x,y)
P1 = Point(2,4)
P2 = Point(1,3)
if(P1 > P2):
    print("P1 is greater than P2")
else:
    print("P1 is less than P2")