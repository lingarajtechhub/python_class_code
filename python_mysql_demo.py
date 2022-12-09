import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)

if(mydb):
    print("Connection is OK.")
else:
    print("No connection")
    

mycursor = mydb.cursor() #mydb is connection object

mycursor.execute("INSERT INTO `student`(`roll`, `name`, `age`, `Address`) VALUES (NULL, 'QWERTY',23,'Q-90')")

if(mycursor):
    print("Record Inserted Successfull")
else:
    print("Record Not Created.")