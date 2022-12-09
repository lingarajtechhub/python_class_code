from conn import *

mycursor = 0  mydb.cursor()

mycursor.execute("SHOW Databases") 

for x in  mycursor:
    print(x,end=" ")