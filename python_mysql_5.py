import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customer3"
)

mycursor = mydb.cursor()

sql = "UPDATE `cust_details` SET `cust_name`='Peter123', `cust_wages`= 5543.768 WHERE `cust_id`= 15"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record updated.")