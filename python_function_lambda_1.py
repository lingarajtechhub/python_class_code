sum = lambda x,y : x+y

print(sum(2,3))

sum = lambda x,y,z:x+y+z
x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))
print(sum(x,y,z))

#x^3 + y^2+3q+2
sum_eq=lambda x,y,q:pow(x,3)+pow(y,2)+3*q+2

print(sum_eq(2,3,4))

def sum():
    return lambda x,y:x+y

s = sum()

print(s(2,3))

def area_of_circle():
    return lambda r: 3.141 * r * r 

area = area_of_circle()

print(area(2))