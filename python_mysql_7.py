import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="qwerty",
    passwd="",
    database="employee"
)

mycursor = mydb.cursor()

sql = "DELETE FROM employee_details WHERE address = 'Sideway 1633'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record deleted.")