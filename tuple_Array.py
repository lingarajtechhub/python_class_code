t = (1,2,3,'a',"A")

print(t)

print(t[0:3])

print(t[-5:])

for x in t:
    print(x, end=" ");
print();

if "A" in t:
    print("Element present in a tuple.")
else:
    print("Element is not present in a tuple.")

print(len(t)) #len() function return number elements in a tuple.ArithmeticError

#del t

#print(t)

t = ()

t = tuple((1,2,3,'a','b','c',"ABC")) #tuple() uses as constructor

print(t)

#count() this function uses for count the number items repeat.

t2 = (1,1,1,2,3,3,4,4,5)

x = t2.count(1)

print(x)


#index() this function return the position of element where it is found.

y = t2.index(3)

print(y)