import mysql.connector

# connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",        # your username
    password="root",    # your password
    database="tcs"      # your database name
)

print("Connected successfully")