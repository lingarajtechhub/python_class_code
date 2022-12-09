f = open("F:\lingaraj1234.txt","w")

f.write("This is a python text file. \
It is created for testing purposes.")

if f:
    print("Content written inside the file.")
else:
    print("Content is not written.")

f.close();