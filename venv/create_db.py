# import
import mysql.connector

# connection
mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="mysql1")
# test if working or not
print(mydbconnection)


# create new databse
db_name = "python_test_db"

mycursor = mydbconnection.cursor()

sqlquery = "CREATE DATABASE " + db_name

mycursor.execute(sqlquery)
