import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customer3"
)

mycursor = mydb.cursor()

sql = "INSERT INTO `cust_details` (`cust_id`, `cust_name`, `cust_wages`) VALUES (NULL, %s, %s);"

val =  [
  ('Peter123', '5543.0'),
  ('Amy321', '343.90'),
  ('Hannah123', '632.87'),
  ('Michael543', '7682.89'),
  ('Sandy456', '8743.08'),
  ('Betty678', '6437.09')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, " records was inserted.")