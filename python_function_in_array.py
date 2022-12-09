def list_fun(l):
    for x in l:
        print(x)


l = [1,2,3,'a','b','c']

list_fun(l)

def tup_fun(t):
    for x in t:
        print(x)

t = (1,2,3,4)

tup_fun(t)

def set_fun(s):
    for x in s:
        print(x)

s = {"QWERTY","KEYPAD"}

set_fun(s)

def dict_fun(d):
    for x,y in d.items():
        print(x," ",y)

d={1:'a',2:'b',3:'c'}

dict_fun(d)