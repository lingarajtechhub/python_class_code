import re;

text = "The rain in spain"

x = re.search("\AThe.*in$",text)

if(x):
    print("Yes! We have a match.")
else:
    print("No Match.")

"""
1. search
2. findall
3. split
4. sub : Replaces one or more matches with  a string
"""