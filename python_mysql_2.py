import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW Databases")

for x in mycursor:
    print(x)
