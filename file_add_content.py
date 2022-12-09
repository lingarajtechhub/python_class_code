f = open("E:\python\lingaraj1.txt","a")

f.write("This is an extra cotent \n written inside the file.")

if f:
    print("Extra Content written inside file.")
else:
    print("Extra Content is not written inside file.")

f.close()