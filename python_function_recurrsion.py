def recur_fun(n):
    if(n>0):
        return n + recur_fun(n-1)#6 + 5 + 4 + 3 + 2 + 1
    else:
        n = 0
        return n   


print("Recursion: ")

print(recur_fun(6))

