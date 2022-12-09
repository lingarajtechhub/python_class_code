from functools import reduce
li2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
list = reduce(lambda x, y:x + y, li2)
print(list)