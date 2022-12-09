import python_module_test


print(python_module_test.expo(2,3))


from python_module_test import expo, floor_div

print(expo(2,3))

print("Floor Division: ",floor_div(2,3))

from python_module_test import mul

print(mul(2,3))

from python_module_test import*
import python_module_test
from python_module_test import person1

print(sub(2,3),sum(2,3),mul(3,2))

from math import*

print(pow(2,3))

a = python_module_test.person1["age"]

print(a)

for x,y in person1.items():
    print(x," : ",y)