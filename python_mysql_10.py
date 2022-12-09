import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customer3"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM `cust_details`")

for x in mycursor:
    print(x)