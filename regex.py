import re
"""
txt = "018The rain xxx cccc vvv in Spain"
x = re.search("^[1-3].*Spain$", txt)

if (x):
    print("YES! We have a match!")
else:
    print("No match")"""

text = "hello"

x = re.search("^[1-9].*",text)

if (x):
    print("YES! We have a match!")
else:
    print("No match")

str = "The rain in Spain ai"
x = re.findall("ai", str)
print(x)
