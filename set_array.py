s = {"Apple","Orange","Mango","QWERTY"}

print(s)

for x in s:
    print(x)


#add() = to add one item to a set
#update() = to add more than one item to a set


s.add("Pineapple")

print(s)

s.update(["QWERTY","KEYPAD"])

print(s)

#len() = to return number of items in a set

print(len(s))

#remove() and discard() both functions are used to remove
# an item  from a set. So difference is remove creates
# an error if item didn't exist as while discard() didn't 
# create any error.

s.remove("Apple")

print(s)

try:
    s.remove("Orange")
except KeyError:
    print("Element is not present.",KeyError)

print(s)


s.discard("Pineapple")

print(s)

s.discard("Pineapple")

print(s)

try:
    s.remove("Orange")
except:
    print("Element is not present.",KeyError)

#pop() = remove the item 
print(s)


s.pop()
s.pop()
print(s)
s.pop()

s = {"Qwerty","Apple","Pineapple","Orange","Mango"}
#clear() = it clears the set

s.clear()

print(s)

try:
    del s
except:
    print("Name 's' is not defined.",s)

#set() = act as a constructor.

s2 = set(("Qwerty","Apple","Pineapple","Orange","Mango"))

print(s2)
"""
#union() = return a set that contains all items from 
#both sets, duplicates are excluded.

x = {1,2,3,4,'a'}
y = {1,5,6,7,8}

z = x.union(y)

print(z)


#update() = insert the items from set x int set y
x = {1,2,3,4,'a'}
y = {1,5,6,7,8}
x.update(y)

print(x)

"""