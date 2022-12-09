d = {"roll":123,"name":"QWERTY","Add":"QWERTY-53426"}

print(d)

print(d["roll"])

print(d.get("name"))

print(d.keys())

print(d.values())

d["roll"]=5463

print(d)


#loop through dictionary
#keys return
for x in d:
    print(x)
   
#values return
for x in d:
    print(d[x])

for x in d.values():
    print(x)

#keys return 
for x in d.keys(): #d.items()
    print(x)

for x,y in d.items():
    print(x,":",y)


print(len(d))

d["age"]=54

print(d)



