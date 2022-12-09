n = int(input("Enter a number: "))
i=2

while(n!=0):
    if(n%i==0):
        break
    i+=1

if(n == i):
        print("Prime Number.",n) 
else:
    print("Not a Prime.",n)