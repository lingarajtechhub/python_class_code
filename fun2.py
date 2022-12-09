def sum(a,b):
    return a+b

print(sum(2, 3))

def list_fun(l):
    for x in l:
        print(x)

l=[1,2,3,4]

list_fun(l)

def stud_fun(roll,name):
    print(roll," ",name)

stud_fun(roll=23,name="QWERTY")


def default_fun(a,b=2):
    print(a," ",b)

default_fun(2,5)