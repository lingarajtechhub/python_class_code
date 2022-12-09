f = open("E:\python\lingaraj1.txt","r")

if f:
    print("Content display on console.")
else:
    print("Content is not display on console.")

print(f.readline())

f.close()