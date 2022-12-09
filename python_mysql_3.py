import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Student1"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customer_details (C_id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), address VARCHAR(255), PRIMARY KEY(C_id))")

mycursor.execute("CREATE table cust_details ( cust_id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, cust_name varchar(30), cust_wages float(4.0))")

if(mycursor):
    print("Table Created Successfully.")
else:
    print("Table is not Created")

#Return customer details  
"""mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)"""
