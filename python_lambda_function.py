#lambda argument : expresion

x = lambda x,y:x+y
print(x(2,3))
print(x(4,5))


x = lambda a,b : print(f"{a} is greater i.e. a.") \
    if(a>b) else print(f"{b} is greater i.e. b.") 
x(2,3)

x = lambda a,b,c : print(f"{a} is greater i.e. a") \
    if(a>b and a>c) else (print(f"{b} is greater i.e. b") \
    if(b>a and b>c) else (f"{c} i greater. i.e. c.")) 
x(2,5,4)


def sum():
    return lambda x,y:x+y

s = sum()

print(s(2,3))

def sub(x):
    return lambda y:x-y

s = sub(4)

print(s(2))

