n = int(input("Enter the factorial of number:"))

def fact_re_fun(n):
    if(n>0):
        return n * fact_re_fun(n-1)# 5 * 4 * 3 * 2 * 1
    else:
        return 1
        
if n<0:
    print("Factorial is not possible.")

elif(n==0):
    print("factorial is One")

else:
    print("Factorial is= ",fact_re_fun(n))

