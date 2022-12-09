import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="qwerty",
    passwd="",
    database="employee"
)

mycursor = mydb.cursor()

