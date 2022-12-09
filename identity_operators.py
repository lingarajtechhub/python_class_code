l = "ASDF"
a = "ASDF"
if (l is a):
    print("same identity")
else:
    print("Not having same identity.")

if(l is not a):
    print("Not having same identity.")
else:
    print("same identity")