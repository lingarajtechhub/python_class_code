l = [] #this is empty list

l = [1,2,3,4,5,6,7,8,9]

print(l)

print(l[5])

print(l[0:7])

print(l[-9:-6])

print(l[-9:])

l[5] = 'A'

print(l)

l[7] = "ASDFGHJKL:"

print(l)

for x in l:
    print(x)

if 'A' in l:
    print("PRESENT")
else:
    print("NOT PRESENT")

#len() = how many items a list has.

print(len(l))

#append() = To add an items to the end of the list

l.append("ASXCV")

print(l)

#insert() = To insert an element in a specific index number.

l.insert(4, '$')

print(l)

#remove() = this method removes the specified item

l.remove("ASDFGHJKL:")

print(l)

#pop() = this method removes the specified index, 
#if there is not given any index then last item 
#is going to be deleted.

l.pop()

print(l)

# del = removes the specified index

del l[4]

print(l)

# del = can use delete the entire list

#del l

#print(l)

l = ['a','b','c']

print(l.clear())

print(l)

l=[]

l2 = []

l=[1,2,3,4]

l2 = l.copy()

print(l2)

#list() = make a copy of a given list

l3=[]

l3 = list(l2)

print(l3)

#list() = this is used to new list and it is call a constructor

l5 = list(("A","B","C"))

print(l5)

#count() = this method return number of times the element is repeated

l6 = [1,2,1,2,3,4,5,6]

s = l6.count(1)

print(s)

#sort = this method sort the list in alphabetically

l7 = ['A','Z','S']

l7.sort()
print(l7) 