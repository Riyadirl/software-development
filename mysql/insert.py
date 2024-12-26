import mysql.connector

db_name = "python_test_db"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql1",
    database=db_name
)

mycursor = mydbconnection.cursor()

sqlquery = """
            INSERT INTO Student(Roll, Name)
            VALUES('101', 'Kawshik Kumar Paul')
            """
mycursor.execute(sqlquery)
mydbconnection.commit()# commit for save

print("Insert table successful")