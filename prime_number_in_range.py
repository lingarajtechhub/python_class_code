n1 = int(input("Enter the 1st range: "))
n2 = int(input("Enter the 2nd Range: "))
j=0
t=0
for k in range(n1, n2,1):
    for j in range(2, k+1, 1):
        if(k%j==0):
            break
    
    if(k==j):
        print("Prime No.",k)
        t+=1
    #else:
        #print("Not A Prime.",k)
print("Total Number OF Primes.",t)
