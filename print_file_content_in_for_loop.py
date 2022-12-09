

f = open("E:\python\lingaraj1.txt","r")

for x in f:
    print(x)

if f:
    print("Content display on console.")
else:
    print("Content is not display on console.")

f.close()