a = int(input("Enter a 1st Number: "))
b = int(input("Enter a 2nd Number: "))
c = int(input("Enter a 3rd Number: "))

if (a>b):
    if(a>c):
        print("a is greater.")
    else:
        print("c is greater.")
else:
    if(b>c):
        print("b is greater.")
    else:
        print("c is greater.")