import mysql.connector

# Step 1: Create connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tcs"
)

# Step 2: Create cursor
cur = con.cursor()

# Step 3: Execute query
cur.execute("SELECT * FROM employee")

# Step 4: Fetch data
for row in cur.fetchall():
    print(row)

# Step 5: Close connection
con.close()