import mysql.connector

mydb = mysql.connector.connect(
   host= "localhost",
   user="root",
   passwd="mysql1"
)

print(mydb)