import python_module_test as py

print(py.person1["name"])

from python_module_test import mul, div
print(mul(2,3))
print(div(2,3))

from python_module_test import *
print(sum(2,3))
print(person1["age"])

