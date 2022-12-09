f = open("F:\lingaraj1234.txt","r")

print(f.read())

if f:
    print("Content display on console.")
else:
    print("Content is not display on console.")

f.close();