import mysql.connector
try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Raje@123",
    )
except:
    print("Connection Failed...")
try:   
    mycursor = conn.cursor()
    mycursor.execute('CREATE DATABASE pr05')
    print("Database created successfully done..")
except:
    print("Database creation failed...")