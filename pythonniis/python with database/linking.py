# import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="niis"
# )

# if con.is_connected():
#     print("Connected successfully")
cur = con.cursor()
cur.execute("SELECT * FROM student")

for row in cur.fetchall():
    print(row)

con.close()
