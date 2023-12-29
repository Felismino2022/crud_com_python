import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_python"
)

cursor = connection.cursor()
