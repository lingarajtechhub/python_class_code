import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="asdf",
    passwd="qwerty"
)

if(mydb):
    print("Connection is OK.")
else:
    print("No connection")


mycursor = mydb.cursor() #mydb is connection object


sql = "CREATE DATABASE Student4"

mycursor.execute(sql)

if(mycursor):
    print("Database created successfully.")
else:
    print("Database not created successfully.")
