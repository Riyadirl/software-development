# import
import mysql.connector

db_name = "python_test_db"
# connection
mydbconnection = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="mysql1", 
    database=db_name
)


mycursor = mydbconnection.cursor()  # same as create db
sqlquery = """
    CREATE TABLE Student
    (
        roll varchar(4),
        name varchar(100)
    )
    """
mycursor.execute(sqlquery)  # same as create db
