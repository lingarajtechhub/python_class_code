import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customer3"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customer_details (C_id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), address VARCHAR(255), PRIMARY KEY(C_id))")

mycursor.execute("INSERT INTO `cust_details`(`cust_id`, `cust_name`, `cust_wages`) VALUES (NULL,'QWERTY',2345.9)")

if(mycursor):
    print("Record Inserted Successfully.")
else:
    print("Record is not Insert.")
