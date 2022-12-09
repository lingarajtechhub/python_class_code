"""s =  ord("A")

print(s)"""

l = [1,2,3,4,'a','A','N','$']

w = len(l)

for i in range (0, w,1):
    ch = l[i]
    q = ord(ch)
    if(48<57):
        l.remove(l[i])

#print(w)