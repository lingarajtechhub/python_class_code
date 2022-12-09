n = int(input("Enter a number:"))

rev=0
n1=n
a=0

while(n!=0):
    a=n%10
    rev=rev*10+a
    n=n//10

if(rev == n1):
    print("Pallindrome No.",n1)
else:
    print("Not a Pallindrome.",n)