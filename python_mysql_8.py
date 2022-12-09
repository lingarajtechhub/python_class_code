import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="qwerty",
    passwd="",
    database="employee"
)

mycursor = mydb.cursor()

sql = "ALTER TABLE employee_details ADD DA3 VARCHAR(32) After Email;"

mycursor.execute(sql)

if(mycursor):
    print("Column Added.")
else:
    print("Column Not Added.")