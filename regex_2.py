import re

str = "The rain in Spain aalls mainly in the plain!"

# Check if the string contains either "falls" or "stays":

x = re.findall("[A-G]alls|[a-f]alls|stays", str)

print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
